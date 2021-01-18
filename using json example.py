import requests


r = requests.get("https://coreyms.com")
print(r.status_code)
# print(os.getcwd())
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
