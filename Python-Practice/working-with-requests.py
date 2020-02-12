"""

The help() method gives us more verbose information about a function, while the dir() function just states the methods
supported by function

"""


import requests


r = requests.get('https://xkcd.com/353/')

# TODO print out status code for requests

print(r.status_code)

# TODO print out text of the image

print(r.text)

# TODO print out headers of the request

print(r.headers)

# TODO print out comic image and write it to a file
r = requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic.png', 'wb') as f:
    f.write(r.content)

# TODO get response for user query

payload = {'count': '2', 'page': '25'}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.text)

# TODO submit some data

payload = {'username': 'harshit', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

print(r.text)

# TODO print output in json
payload = {'username': 'harshit', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
r_dict = r.json()
print(r_dict['form'])

# TODO basic auth
r = requests.get('https://httpbin.org/basic-auth/harshit/testing', auth=('harsh','testing'))
print(r.status_code)
