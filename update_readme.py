import datetime
import logging
import os
from typing import Dict, Any
import requests

# Configure logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GitHubProfileGenerator:
    def __init__(self, username: str):
        self.username = username
        self.headers = {'Authorization': f"token {os.environ.get('PAT_TOKEN', '')}"}
        self.logger = logging.getLogger(__name__)

    def get_github_stats(self) -> Dict[str, Any]:
        """Fetch GitHub statistics using GraphQL API for GitHub Stats section."""
        query = '''
        query($login: String!) {
            user(login: $login) {
                repositories(first: 100, ownerAffiliations: OWNER) {
                    totalCount
                    nodes {
                        stargazers { totalCount }
                        languages(first: 5, orderBy: {field: SIZE, direction: DESC}) {
                            nodes { name }
                        }
                    }
                }
                contributionsCollection {
                    totalCommitContributions
                }
            }
        }
        '''
        try:
            response = requests.post(
                'https://api.github.com/graphql',
                json={'query': query, 'variables': {'login': self.username}},
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()['data']['user']

            languages = []
            for repo in data['repositories']['nodes']:
                for lang in repo['languages']['nodes']:
                    if lang['name'] not in languages:
                        languages.append(lang['name'])

            return {
                'repos': data['repositories']['totalCount'],
                'stars': sum(repo['stargazers']['totalCount'] for repo in data['repositories']['nodes']),
                'commits': data['contributionsCollection']['totalCommitContributions'],
                'languages': languages[:6]  # Include TypeScript, Python, JavaScript, HTML, CSS
            }
        except requests.RequestException as e:
            self.logger.error(f"Error fetching GitHub stats: {e}")
            return {
                'repos': '?',
                'stars': '?',
                'commits': '?',
                'languages': ['TypeScript', 'Python', 'JavaScript', 'HTML', 'CSS']
            }

    def generate_github_stats(self) -> str:
        """Generate GitHub Stats section with compact stats, languages, and streak."""
        return f"""## 📊 GitHub Stats
<table align="center" style="background: linear-gradient(145deg, #1e0707, #345a54); padding: 10px; border-radius: 10px; margin: 15px 0; box-shadow: 0 6px 20px rgba(52, 90, 84, 0.3); border: none;">
  <tr style="border: none;">
    <td colspan="2" align="center" style="padding: 5px;">
      <img src="https://github-readme-stats.vercel.app/api?username={self.username}&show_icons=true&bg_color=00000000&text_color=94bcbc&title_color=b85c51&icon_color=345a54&hide_border=true&include_all_commits=false&count_private=false&hide=stars,issues&custom_title=Activity" alt="GitHub Stats" style="border-radius: 6px; box-shadow: 0 4px 10px rgba(148, 188, 188, 0.2); max-width: 400px;">
    </td>
  </tr>
  <tr style="border: none;">
    <td width="50%" align="center" style="padding: 5px;">
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={self.username}&langs_count=6&layout=compact&bg_color=00000000&text_color=94bcbc&title_color=b85c51&icon_color=345a54&hide_border=true&hide=jupyter%20notebook&custom_title=Top%20Languages" alt="Top Languages" style="border-radius: 6px; box-shadow: 0 4px 10px rgba(148, 188, 188, 0.2); max-width: 250px;">
    </td>
    <td width="50%" align="center" style="padding: 5px;">
      <img src="https://github-readme-streak-stats.herokuapp.com/?user={self.username}&background=00000000&border=345a54&stroke=b85c51&ring=94bcbc&fire=94bcbc&currStreakNum=94bcbc&sideNums=94bcbc&currStreakLabel=b85c51&sideLabels=b85c51&dates=345a54&hide_border=true" alt="GitHub Streak" style="border-radius: 6px; box-shadow: 0 4px 10px rgba(148, 188, 188, 0.2); max-width: 250px;">
    </td>
  </tr>
</table>
<div align="center" style="background: rgba(30, 7, 7, 0.4); padding: 10px; border-radius: 10px; margin: 15px 0; border: 1px solid rgba(181, 92, 81, 0.2); backdrop-filter: blur(5px); transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
  <p style="color: #b85c51; text-shadow: 0 0 4px #b85c51; margin: 5px 0; font-size: 1em;">Top 3 Repos</p>
  <img src="https://github-contributor-stats.vercel.app/api?username={self.username}&limit=3&theme=transparent&combine_all_yearly_contributions=true" alt="Top Contributed Repos" style="border-radius: 6px; box-shadow: 0 4px 10px rgba(148, 188, 188, 0.2); max-width: 400px;">
</div>"""

    def update_readme(self) -> None:
        """Update README.md by replacing the GitHub Stats section."""
        try:
            with open('README.md', 'r', encoding='utf-8') as f:
                content = f.read()

            # Define the placeholder for the GitHub Stats section
            start_marker = '<!-- GITHUB_STATS_START -->'
            end_marker = '<!-- GITHUB_STATS_END -->'
            new_stats = self.generate_github_stats()

            # Find and replace the GitHub Stats section
            start_idx = content.find(start_marker) + len(start_marker)
            end_idx = content.find(end_marker)
            if start_idx == -1 or end_idx == -1:
                self.logger.error("GitHub Stats markers not found in README")
                return

            new_content = content[:start_idx] + '\n' + new_stats + '\n' + content[end_idx:]

            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(new_content)
            self.logger.info("Successfully updated GitHub Stats section in README")
        except Exception as e:
            self.logger.error(f"Error updating README: {e}")

if __name__ == "__main__":
    generator = GitHubProfileGenerator(os.environ.get('GITHUB_USERNAME', 'Gitesh08'))
    generator.update_readme()
