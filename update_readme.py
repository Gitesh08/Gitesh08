import datetime
import requests
import os

class GitHubProfileGenerator:
    def __init__(self, username):
        self.username = username
        self.headers = {'Authorization': f"token {os.environ.get('GITHUB_TOKEN', '')}"}
        
    def get_ascii_banner(self):
        """Read ASCII banner from assets folder"""
        try:
            with open('/assets/ascii_art.txt', 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return """
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣷⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⠛⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣶⣶⣿⣶⣤⠀⣼⣿⣷⣮⡓⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠿⣿⣿⠟⢋⠀⠘⠛⠛⠋⠁⢹⣗⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡀⠀⠀⣴⣽⣄⣬⡵⢤⡀⢀⣾⣍⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣆⣶⣾⣿⠯⠽⢿⡿⠗⠘⣿⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⣿⣿⣆⠙⢿⣭⣿⡿⠁⣠⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⣄⣀⣤⣤⣾⡿⢋⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿⠟⠁⣸⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⣿⢻⡏⢛⡏⠀⢀⡀⢠⠃⣿⣿⣷⡒⠦⠤⠤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠚⠉⣰⣿⣿⣿⠀⠙⢦⡀⠀⠀⡰⠃⠀⣿⣿⣿⣷⡀⠀⠀⠀⠀⠈⠉⠉⠉⠑⢆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠔⠒⠉⠁⠀⠀⠀⠀⢰⣿⣿⣿⣿⣧⠀⣀⣽⣒⣾⣁⡀⠀⣿⠈⠙⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀
⠀⠀⠀⣞⡀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡻⣿⠛⡏⠻⣿⣴⡿⠛⠉⢹⢿⡀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠀
⠀⠀⠀⣯⡇⠀⠀⠀⠀⠀⠀⠀⡟⢏⠀⡀⣿⠆⢹⡀⣿⣿⡇⠀⢀⡏⠚⡇⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣇⠀⠀⠀⠀
⠀⠀⢠⣣⢧⢀⠀⠀⠀⠀⠀⠀⣇⠈⢂⠁⣿⡆⠀⢳⣿⣿⣿⠀⣼⠀⠀⡇⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢸⡀⠀⠀⠀
⠀⠀⢸⡟⣘⢸⡀⠀⠀⢸⡆⠀⢻⠀⠀⠸⣿⡏⠁⣄⣿⣿⡟⣴⢣⠀⠀⣿⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀
⠀⠀⡯⣧⣏⠀⣧⠀⠀⢸⠁⠀⢸⠀⠀⠀⣾⡄⣶⣿⣿⣿⣷⠃⠀⠂⠀⢻⠀⠀⠀⣿⣇⠉⠉⠉⠿⢇⠀⠀⠀⠀⠀⢸⠀⠀⠀
⠀⢸⢒⡿⠛⠀⢻⠀⠀⣿⠀⠀⢸⠤⠀⠀⣿⣷⣽⣿⣿⣿⣷⣶⣶⠀⣀⢸⡆⠀⠀⣿⡇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀
⠀⠸⣾⠇⢀⠀⠸⡇⢠⣿⢀⠀⢸⣼⣦⣼⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠆⠂⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀
⠀⠀⣿⣾⠁⠀⠀⢧⣼⠇⣐⠂⢸⣿⣿⣿⣿⣿⣷⣌⣻⣿⣿⣿⣿⣿⣿⣿⣏⢡⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠀⢸⣀⡏⠀⠀⠀⢸⡟⠛⠟⠋⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣷⡿⡀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⣇⠀
⠀⠘⡿⠃⠀⠀⠀⣿⠃⠂⡁⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠯⡇⠉⠀⠀⠀⠀⠀⠀⠿⡀⠀⠀⡀⠀⠸⡄
⠀⡼⣠⣠⣤⠀⠀⣿⠠⠀⠀⠀⠀⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣠⡇⠀⠀⠀⠀⠀⠀⠀⣆⣤⡶⠾⠲⠶⠤⢷
⠀⣧⢏⣁⣈⣤⣤⣸⡀⠀⠀⠀⠄⡯⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠄⠀⠀⠀⠀⢄⣸⠛⠁⠀⠀⠀⠀⠀⡞
⢸⠻⠦⠤⠄⠀⠀⢻⡇⠀⠀⠉⠀⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡷⠀⠀⠀⠀⠀⠀⣹⠀⠀⠀⠀⠀⠀⢸⠁
⠸⣕⠀⠀⠐⠀⠀⠈⡇⠀⠀⣀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⡸⠀
⠀⢯⡧⠀⠀⠀⠀⠀⢿⠀⠀⠈⠳⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠀⢸⣿⡂⠀⠀⠀⠀⠘⡇⡄⠐⠰⣄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⢰⠁⠀⠀⢀⣤⣤⡄⣺⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

    def get_github_stats(self):
        """Fetch GitHub statistics using the GraphQL API"""
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
                followers { totalCount }
                following { totalCount }
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
                headers=self.headers
            )
            
            if response.status_code == 200:
                data = response.json()['data']['user']
                
                # Get frequently used languages
                languages = []
                for repo in data['repositories']['nodes']:
                    for lang in repo['languages']['nodes']:
                        if lang['name'] not in languages:
                            languages.append(lang['name'])
                
                return {
                    'repos': data['repositories']['totalCount'],
                    'stars': sum(repo['stargazers']['totalCount'] for repo in data['repositories']['nodes']),
                    'followers': data['followers']['totalCount'],
                    'following': data['following']['totalCount'],
                    'commits': data['contributionsCollection']['totalCommitContributions'],
                    'languages': languages[:5]  # Top 5 languages
                }
        except Exception as e:
            print(f"Error fetching GitHub stats: {e}")
        return {
            'repos': '?', 'stars': '?', 'followers': '?', 
            'following': '?', 'commits': '?', 'languages': []
        }

    def generate_readme(self):
        """Generate README content with GitHub stats and ASCII banner"""
        stats = self.get_github_stats()
        banner = self.get_ascii_banner()
        
        tech_stack = {
            'Python': '🐍',
            'JavaScript': '📜',
            'Java': '☕',
            'HTML': '🌐',
            'CSS': '🎨',
            'TypeScript': '📘',
            'React': '⚛️',
            'Node.js': '💚'
        }
        
        return f"""<div align="center">

```
{banner}
```

# Hi there, I'm {self.username} 👋

[![Profile Views](https://komarev.com/ghpvc/?username={self.username}&color=blueviolet)](https://github.com/{self.username})
[![GitHub followers](https://img.shields.io/github/followers/{self.username}?style=social)](https://github.com/{self.username})

## About Me 💻

```python
class SoftwareDeveloper:
    def __init__(self):
        self.name = "{self.username}"
        self.role = "AI Engineer"
        self.languages = {', '.join(stats['languages'])}
        self.interest = ["AI/ML", "Cloud", "Web Development", "Open Source"]
    
    def say_hi(self):
        print("Thanks for visiting my GitHub profile!")

me = SoftwareDeveloper()
me.say_hi()
```

## 📊 GitHub Statistics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={self.username}&show_icons=true&theme=tokyonight" alt="GitHub Stats" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={self.username}&theme=tokyonight" alt="GitHub Streak" />
</p>

## 🏆 Quick Stats
📦 **Repositories**: {stats['repos']}
⭐ **Stars Earned**: {stats['stars']}
👥 **Followers**: {stats['followers']}
🤝 **Following**: {stats['following']}
🔄 **Commits**: {stats['commits']}

## 🛠️ Technologies & Tools
{' '.join(f"`{lang}` {tech_stack.get(lang, '🔧')}" for lang in stats['languages'])}

## 📫 Connect With Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gitesh-mahadik-7487961a0/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gmahadik8080@gmail.com)

---
<p align="center">
  <i>Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC</i>
</p>
</div>"""

    def update_readme(self):
        """Update README.md file"""
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(self.generate_readme())

if __name__ == "__main__":
    generator = GitHubProfileGenerator(os.environ.get('GITHUB_USERNAME', 'Gitesh08'))
    generator.update_readme()