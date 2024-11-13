import datetime
from .badge_generator import BadgeGenerator
from .stats_generator import StatsGenerator
from ..utils.helpers import load_ascii_art

class ReadmeGenerator:
    def __init__(self, user_data):
        self.user_data = user_data
        self.stats = StatsGenerator.calculate_total_stats(user_data)
        self.languages = StatsGenerator.get_language_stats(user_data['repositories']['nodes'])
        self.ascii_art = load_ascii_art()

    def generate(self):
        return f"""<div align="center">

# Hi there 👋, I'm {self.user_data.get('name', self.user_data['login'])}

```
{self.ascii_art}
```

{self.user_data.get('bio', 'Full Stack Developer | Open Source Enthusiast')}

<p align="center">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=2E98FF&center=true&vCenter=true&width=435&lines=Developer;Open+Source+Enthusiast;Always+Learning" alt="Typing SVG" />
</p>

## 📊 GitHub Statistics

<p align="center">
    <img src="https://komarev.com/ghpvc/?username={self.user_data['login']}&color=blueviolet" alt="Profile Views" />
    <img src="https://img.shields.io/github/followers/{self.user_data['login']}?style=social" alt="GitHub followers" />
    <img src="https://img.shields.io/github/stars/{self.user_data['login']}?style=social" alt="GitHub stars" />
</p>

<p align="center">
    <img height="160px" src="https://github-readme-stats.vercel.app/api?username={self.user_data['login']}&show_icons=true&theme=radical&count_private=true" />
    <img height="160px" src="https://github-readme-stats.vercel.app/api/top-langs/?username={self.user_data['login']}&layout=compact&theme=radical" />
</p>

[... rest of the README template ...]
"""