import requests as rq

print('The requests version in this environment is ', rq.__version__)


hp = rq.get('http://www.google.com/')

print('The status code is ', hp.status_code)
print('The content is ',hp.content)