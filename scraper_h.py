# imports
from bs4 import BeautifulSoup
import requests
from operator import itemgetter


# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

# Scraper für website: heise.de
def main():
    d =[]
    for page in range(1,5,1):

        # alle https Titel
        heise_https_url = "https://www.heise.de/thema/https?seite=" + str(page)

        # https topics
        content = getPage(heise_https_url).find("div", {"class":"keywordliste"})
        content = content.findAll("header")

        for c in content:
            d.append(c)

        print(d)

    print("\nDONE !\n\nTopic https on heise.de was scraped completely.\n")



# main program
if __name__ == '__main__':
    main()