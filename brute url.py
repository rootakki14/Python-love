import requests
file = open("list.txt", "r")
lines = file.read().split(',')
for lines in lines:
    url = 'example.com/xyz/parameter'+ lines
    r = requests.get(url)
    print url
    print r.headers.get('content-length')