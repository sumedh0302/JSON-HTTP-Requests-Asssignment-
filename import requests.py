import requests

# 1 Fetch data and print titles of the first 10 posts
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    print(" Titles of the first 10 posts:")
    for post in posts[:10]:
        print("-", post["title"])
else:
    print(" Failed to fetch posts, Status Code:", response.status_code)

print("\n" + "="*50 + "\n")

# 2 Send a POST request with custom JSON data
post_url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "My Custom Post",
    "body": "This is a test post using Python requests.",
    "userId": 1
}

post_response = requests.post(post_url, json=data)
print(" Response from POST request:")
print(post_response.json())

print("\n" + "="*50 + "\n")

# 3 Check if a given website returns status code 200
website = "https://www.google.com"  # You can replace this with any website
check = requests.get(website)

if check.status_code == 200:
    print(f" {website} is reachable (Status Code 200).")
else:
    print(f" {website} returned Status Code:", check.status_code)
