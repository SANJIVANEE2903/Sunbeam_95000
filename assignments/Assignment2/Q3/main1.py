import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for post in data:
        print("User ID:", post["userId"])
        print("Post ID:", post["id"])
        print("Title:", post["title"])
        print("Body:", post["body"])
        print("------------------------")
else:
    print("Error:", response.status_code)
