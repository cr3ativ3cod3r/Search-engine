import requests

def search_google(query, api_key, cx):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])
    else:
        print("ERROR: ", response.status_code)
        return None



cx = "d4a044f0660af4275"
query = ""

while True:
    query = input("[SEARCH INPUT]\n>> ")
    if (query == "!exit"):
        break
    results = search_google(query, api_key, cx)

    if results:
        print("\n[SEARCH RESULTS]")
        for i, item in enumerate(results, 1):
            print(f"{i}. {item['title']}: {item['link']}")
    else:
        print("NO RESULTS FOUND.")
    print("")