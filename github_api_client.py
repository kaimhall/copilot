# github_api_client.py

import os

GITHUB_API_TOKEN = os.environ.get("GITHUB_API_TOKEN")


# get repository names for a given github user from the github api
def get_repo_names(user):
    import requests

    url = f"https://api.github.com/users/{user}/repos"
    headers = {"Authorization": f"token {GITHUB_API_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return [repo["name"] for repo in response.json()]
