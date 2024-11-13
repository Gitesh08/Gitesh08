import datetime
import requests
import os

class HumanBrain:
    def __init__(self):
        self.coffee_level = 0
        self.debugging = True
        self.stack_overflow_visits = float('inf')
    
    def train_neural_network(self):
        if self.coffee_level < 80:
            return "Error: Coffee level too low ☕"
        elif self.debugging:
            return "It's not a bug, it's a feature! 🐛"
        else:
            return "Model's accuracy: 99.9% (in my dreams) 😴"

    def daily_routine(self):
        return [
            "Wake up 😴",
            "Coffee ☕",
            "Train AI 🤖",
            "Coffee ☕",
            "Debug 🐛",
            "Coffee ☕",
            "Pretend to understand transformers 🤔",
            "More coffee ☕"
        ]

class GitHubProfileGenerator:
    def __init__(self, username):
        self.username = username
        self.headers = {'Authorization': f"token {os.environ.get('GITHUB_TOKEN', '')}"}
        self.brain = HumanBrain()
        
    def get_ascii_banner(self):
        """Read ASCII banner from assets folder"""
        try:
            with open('assets/ascii_art.txt', 'r', encoding='utf-8') as f:
                return f.read()
        except:
            print("Error: Could not load ASCII art file")
            return "<!-- ASCII art could not be loaded -->"

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

    def generate_fun_stats(self):
        """Generate fun AI Engineer stats with CSS animations"""
        return f"""
<div align="center">
<style>
@keyframes fillBar {{
    from {{ width: 0; }}
    to {{ width: var(--fill-percentage); }}
}}

.skill-bar {{
    background: linear-gradient(90deg, var(--bar-color) var(--fill-percentage), #2d2d2d var(--fill-percentage));
    height: 20px;
    border-radius: 10px;
    margin: 5px 0;
    animation: fillBar 1.5s ease-out forwards;
    display: inline-block;
    width: 200px;
}}

.stats-container {{
    background: #1a1b27;
    border-radius: 10px;
    padding: 20px;
    margin: 20px 0;
    color: #fff;
    font-family: 'Courier New', monospace;
}}

.skill-label {{
    text-align: left;
    margin-right: 10px;
    min-width: 200px;
    display: inline-block;
}}

.skill-row {{
    margin: 10px 0;
    display: flex;
    align-items: center;
}}

.percentage {{
    margin-left: 10px;
    min-width: 60px;
}}
</style>

<div class="stats-container">
    <h2>🎮 AI Engineer Stats</h2>
    <div style="text-align: center; margin-bottom: 20px;">
        <h3>PLAYER 1: {self.username.upper()}</h3>
        <h4>LEVEL: AI ENGINEER</h4>
    </div>
    
    <div class="skill-row">
        <span class="skill-label">➤ Coffee Drinking</span>
        <div class="skill-bar" style="--fill-percentage: 120%; --bar-color: #9f3;"></div>
        <span class="percentage">120%</span>
    </div>
    
    <div class="skill-row">
        <span class="skill-label">➤ Bug Creating</span>
        <div class="skill-bar" style="--fill-percentage: 90%; --bar-color: #f93;"></div>
        <span class="percentage">90%</span>
    </div>
    
    <div class="skill-row">
        <span class="skill-label">➤ Bug Fixing</span>
        <div class="skill-bar" style="--fill-percentage: 40%; --bar-color: #f39;"></div>
        <span class="percentage">40%</span>
    </div>
    
    <div class="skill-row">
        <span class="skill-label">➤ Stack Overflow Searching</span>
        <div class="skill-bar" style="--fill-percentage: 120%; --bar-color: #93f;"></div>
        <span class="percentage">120%</span>
    </div>
    
    <div class="skill-row">
        <span class="skill-label">➤ Documentation Reading</span>
        <div class="skill-bar" style="--fill-percentage: 20%; --bar-color: #3f9;"></div>
        <span class="percentage">20%</span>
    </div>
    
    <div class="skill-row">
        <span class="skill-label">➤ AI Hype Generation</span>
        <div class="skill-bar" style="--fill-percentage: 120%; --bar-color: #f33;"></div>
        <span class="percentage">120%</span>
    </div>
</div>
</div>
"""

    def generate_fun_badges(self):
        """Generate fun custom badges"""
        return """
<div align="center">
  <img src="https://forthebadge.com/images/badges/powered-by-coffee.svg" />
  <img src="https://forthebadge.com/images/badges/contains-technical-debt.svg" />
  <img src="https://forthebadge.com/images/badges/works-on-my-machine.svg" />
</div>
"""

    def generate_readme(self):
        """Generate README content with GitHub stats, ASCII banner, and fun elements"""
        stats = self.get_github_stats()
        banner = self.get_ascii_banner()
        daily_routine = self.brain.daily_routine()
        
        tech_stack = {
            'Python': '🐍',
            'JavaScript': '📜',
            'C++': '☕',
            'HTML': '🌐',
            'CSS': '🎨',
            'TypeScript': '📘',
            'React': '⚛️',
            'Node.js': '💚'
        }
        
        # Convert daily routine list to string representation
        daily_routine_str = str(daily_routine).replace("'", '"')
        
        return f"""<div align="center">

{banner}

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Press+Start+2P&size=25&duration=4000&pause=1000&color=00FFB9&center=true&vCenter=true&random=false&width=600&lines=%F0%9F%A4%96+BEEP+BOOP+BEEP!;LOADING+AI+ENGINEER...;NEURAL+NETS+GO+BRRR...;%F0%9F%A7%A0+BRAIN.EXE+ACTIVATED!" alt="Typing SVG" />
</div>

## About Me 💻

```python
class AIEngineer(HumanBrain):
    def __init__(self):
        super().__init__()
        self.name = "{self.username}"
        self.role = "AI Engineer"
        self.languages = {str(stats['languages'])}
        self.interest = ["AI/ML", "Cloud", "Web Development", "Open Source"]
        self.current_status = "{self.brain.train_neural_network()}"
    
    def daily_routine(self):
        return {daily_routine_str}

me = AIEngineer()
```

{self.generate_fun_badges()}

## 📊 GitHub Statistics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={self.username}&show_icons=true&theme=tokyonight" alt="GitHub Stats" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={self.username}&theme=tokyonight" alt="GitHub Streak" />
</p>

{self.generate_fun_stats()}

## 🎯 When I'm Not Training Neural Networks...

| Probably... | Because... |
|-------------|------------|
| 🛠️ Building Skynet | Someone's gotta do it! |
| 🤔 Explaining to GPT why it's wrong | And losing the argument... |
| ☕ Drinking coffee | My neural networks run on caffeine |
| 🐛 Creating bugs | I mean... "features" |
| 📚 Reading documentation | Just kidding, Stack Overflow FTW! |

## 🛠️ Technologies & Tools
{' '.join(f'`{lang}` {tech_stack.get(lang, "🔧")}' for lang in stats['languages'])}

## 📫 Connect With Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gitesh-mahadik-7487961a0/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gmahadik8080@gmail.com)

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=Gitesh08&label=Human+Visitors&color=blueviolet&style=flat-square" />
  <img src="https://komarev.com/ghpvc/?username=Gitesh08&label=Robot+Visitors&color=blue&style=flat-square" />
</div>

```python
# Error 418: I'm a teapot... I mean, an AI Engineer
```

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