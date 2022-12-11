import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

response_dict = r.json()
repo_dicts = response_dict['items']

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
