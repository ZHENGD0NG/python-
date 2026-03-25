import requests
requests.get("http://books.toscrape.com/")
if response.ok:
    print(response.text)
else:
    print("请求失败")