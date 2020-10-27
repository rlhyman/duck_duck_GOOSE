import requests
from bs4 import BeautifulSoup


def main():

    def get_response():
        url = 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json'
        response = requests.get(url)
        final = response.json()
        return final
    get_response()

    def show_page():
        page = requests.get("https://api.duckduckgo.com/?q=presidents+of+the+united+states")
        page_content = BeautifulSoup(page.content, "html.parser")
        print("Here are your results! \n " + page_content.prettify())
    show_page()


main()
