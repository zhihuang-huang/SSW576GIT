"""
read the repository of Github and read the sum of commit of each repository
author: zhiqiang huang
date: 04/06/2020
"""

import requests as requests
import json


def git_reader(username):
    r = requests.get("https://api.github.com/users/" + username + "/repos")
    if r.status_code != 200:
        raise ValueError("User name is invalid")
    else:
        pretty_json = json.loads(r.text)
        repo = []
        for item in pretty_json:
            repo.append(item['name'])

    result = []
    for item in repo:
        r = requests.get("https://api.github.com/repos/" + username + '/' + item + "/commits")
        pretty_json = json.loads(r.text)
        result.append("Repo: " + item + " Number of commits: " + str(len(pretty_json)))

    return result


print(git_reader("richkempinski"))