import os

class Config:
    GITHUB_TOKEN = os.environ.get('ACCESS_TOKEN')
    GITHUB_USERNAME = os.environ.get('Gitesh08')
    GITHUB_API_URL = "https://api.github.com/graphql"
    UPDATE_INTERVAL = 6  # hours