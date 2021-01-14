from bs4 import BeautifulSoup
import requests

search = "business"
params = {"q": search}
url = ("https://www.bing.com/search")
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
headers = {"user-agent": USER_AGENT}
# create a variable for the requests
r = requests.get(url, params=params, headers=headers)


def bing_webcrawler():
    # Content of the request(variable r)
    soup = BeautifulSoup(r.text, "html.parser")
    # This must be a dictionary
    results = soup.find("ol", {"id": "b_results"})
    # This must be a dictionary
    links = results.find_all("li", {"class": "b_algo"})

    for i in links:
        # Variables for the information we want to get from the links
        item_text = i.find("a").text
        item_link = i.find("a").attrs["href"]
        if item_text and item_link:
            print(item_text)
            print(item_link)


bing_webcrawler()
