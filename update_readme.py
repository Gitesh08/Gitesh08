from src.github_api import GitHubAPI
from src.generators.readme_generator import ReadmeGenerator

def main():
    # Initialize GitHub API
    github_api = GitHubAPI()
    
    # Fetch user data
    user_data = github_api.fetch_user_details()
    
    if user_data:
        # Generate README
        generator = ReadmeGenerator(user_data)
        readme_content = generator.generate()
        
        # Save README
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print("README updated successfully!")
    else:
        print("Failed to fetch user data")

if __name__ == "__main__":
    main()