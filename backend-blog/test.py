import requests

response = requests.post('http://127.0.0.1:5000/posts', json={'title': 'Test', 'content': 'Content'})
print(response.status_code)
print(response.json())
