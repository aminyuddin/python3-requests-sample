import requests

response = requests.get('https://api.github.com/users/mohdaminyuddin/repos')

if (response.status_code != 200):
    print (response.status_code)
else:
    for repo in response.json():
        print ('[{}] {} by {}'.format(repo['language'], repo['name'], repo['owner']['login']))
