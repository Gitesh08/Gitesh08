class StatsGenerator:
    @staticmethod
    def get_language_stats(repositories):
        language_stats = {}
        for repo in repositories:
            if 'languages' in repo:
                for lang_edge in repo['languages']['edges']:
                    lang_name = lang_edge['node']['name']
                    lang_size = lang_edge['size']
                    language_stats[lang_name] = language_stats.get(lang_name, 0) + lang_size
        
        total = sum(language_stats.values())
        if total > 0:
            language_stats = {k: round((v/total)*100, 2) for k, v in language_stats.items()}
        
        return dict(sorted(language_stats.items(), key=lambda x: x[1], reverse=True)[:8])

    @staticmethod
    def calculate_total_stats(user_data):
        repos = user_data['repositories']['nodes']
        return {
            'total_stars': sum(repo['stargazers']['totalCount'] for repo in repos),
            'total_repos': user_data['repositories']['totalCount'],
            'followers': user_data['followers']['totalCount'],
            'contributions': user_data['contributionsCollection']['contributionCalendar']['totalContributions']
        }
