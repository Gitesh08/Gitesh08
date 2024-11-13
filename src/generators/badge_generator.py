class BadgeGenerator:
    @staticmethod
    def generate_language_badges(languages):
        color_map = {
            "Python": "3776AB",
            "JavaScript": "F7DF1E",
            "HTML": "E34F26",
            "CSS": "1572B6",
            "Java": "007396",
            "TypeScript": "3178C6",
            "C++": "00599C",
            "Ruby": "CC342D",
            "PHP": "777BB4",
            "Swift": "FA7343",
            "Go": "00ADD8",
            "Rust": "000000",
        }
        
        badges = []
        for lang, percentage in languages.items():
            color = color_map.get(lang, "2bbc8a")
            badge = f"![{lang}](https://img.shields.io/badge/{lang}-{percentage}%25-{color}?style=flat-square&logo={lang.lower()}&logoColor=white)"
            badges.append(badge)
        
        return "\n".join(badges)