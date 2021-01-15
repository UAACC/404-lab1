import requests as rq

print('The requests version in this environment is ', rq.__version__)


hp = rq.get('http://www.google.com/')

print('The status code is ', hp.status_code)
print('The content is ',hp.content)


cd = rq.get('https://raw.githubusercontent.com/UAACC/404-lab1/main/q2.py')
f = open("lab1_code.txt", "w")
f.write(cd.text)
f.close()


f = open("lab1_code.txt", "r")
print('THE CODE BELOW:',f.read())

