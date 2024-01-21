import requests

def hit_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website hit successful!")
        else:
            print("Website hit failed. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
website_url = "https://github.com/EmirhanBarlas"
for _ in range(10000):
    hit_website(website_url)
