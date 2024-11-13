import requests
from .config import Config

class GitHubAPI:
    def __init__(self):
        self.headers = {'authorization': f'token {Config.GITHUB_TOKEN}'}
        self.username = Config.GITHUB_USERNAME

    def fetch_user_details(self):
        query = '''
        query($login: String!) {
            user(login: $login) {
                name
                bio
                company
                location
                websiteUrl
                twitterUsername
                email
                repositories(first: 100, ownerAffiliations: OWNER, privacy: PUBLIC) {
                    totalCount
                    nodes {
                        name
                        stargazers {
                            totalCount
                        }
                        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
                            edges {
                                node {
                                    name
                                }
                                size
                            }
                        }
                    }
                }
                followers {
                    totalCount
                }
                following {
                    totalCount
                }
                contributionsCollection {
                    totalCommitContributions
                    restrictedContributionsCount
                    contributionCalendar {
                        totalContributions
                    }
                }
            }
        }
        '''
        
        try:
            response = requests.post(
                Config.GITHUB_API_URL,
                json={'query': query, 'variables': {'login': self.username}},
                headers=self.headers
            )
            
            if response.status_code == 200:
                return response.json()['data']['user']
            else:
                print(f"Error: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching user details: {e}")
            return None
