from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def class_filter(media_name):
    class_name = ""
    element_selector = ""

    if media_name == "kompas":
        class_name = "hlTitle"
        element_selector = "h1"
    elif media_name == "detik":
        class_name = "media__title"
        element_selector = "h2"
    elif media_name == "tribun":
        class_name = "hltitle"
        element_selector = "div"

    return [class_name, element_selector]

def scrape_news(name, url):
    detector = class_filter(name)
    class_name, element_selector = detector[0], detector[1]

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    headline_element = soup.find(element_selector, class_=class_name)
    return headline_element.text.strip() if headline_element else "Headline tidak ditemukan"

@app.route("/")
def main():
    kompas = scrape_news("kompas", "https://www.kompas.com/")
    detik = scrape_news("detik", "https://news.detik.com/")
    tribun = scrape_news("tribun", "https://www.tribunnews.com/")

    return render_template("index.html", news1=kompas, news2=detik, news3=tribun)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
