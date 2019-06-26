import requests
url = "https://jsonplaceholder.typicode.com/todos/1"
res = requests.get(url, headers = {
	"Accept": "application/json"
})

print(f"your request to {url} come back w/ status code {res.status_code}")

text = res.text
data = res.json()
print(type(text))
print(type(data))
print(text)
print(data)
