#!/usr/bin/env python
"""
This program takes in a public github repo and lets you know
how many stars and watchers they have.

To run this code, you can run python3 alta3research-request02.py --help
"""


import argparse

import requests

parser = argparse.ArgumentParser()

# We use type annotations here.
def get_repo_info(author: str, repo: str) -> str:
    PREFIX = 'https://api.github.com/repos'
    req = requests.get(f'{PREFIX}/{author}/{repo}')
    if req.ok:
        data = req.json()
        watchers = data["watchers"]
        stars = data["stargazers_count"]
        msg = f'''
Looks like I have {watchers} watchers and {stars} stars for this repo.
Are you going to help out? :D
        '''
        return msg


def main():
    # Defined the arguments for the program
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repo", type=str, help="Select a repo")
    parser.add_argument("-a", "--author", type=str, help="Select an author")
    args = parser.parse_args()
    print(get_repo_info(author=args.author, repo=args.repo))


if __name__ == '__main__':
    main()
