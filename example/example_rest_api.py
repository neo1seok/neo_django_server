import requests



#r = requests.get("http://127.0.0.1:8080/api/webtoon/?status=active")
r = requests.get("http://127.0.0.1:8080/api/webtoon/?status=active")

print(r)
print(r.text)