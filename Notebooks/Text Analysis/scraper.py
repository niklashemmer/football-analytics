from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import time
import pandas as pd

comments_list = []
class1 = "cPost ipsBox ipsResponsive_pull ipsComment ipsComment_parent ipsClearfix "
class2 = class1 + "ipsClear ipsColumns ipsColumns_noSpacing ipsColumns_collapsePhone"

def get_comment(page):
    url = "https://www.foxestalk.co.uk/topic/123624-youri-tielemans/page/"

    html = requests.get(url + str(page) + "/#comments").text
    soup = BeautifulSoup(html, "lxml")
    #soup = BeautifulSoup(html, "html.parser")

    # Ignore all blockquotes
    for blockquote in soup(["blockquote"]):
        blockquote.decompose()

    # Find all Comments

    posts = soup.select('article[id^="elComment"]')

    # Print all comments
    for post in posts:
        try:
            comments_list.append({
                'Username': post.h3.text.strip(),
                "User": post.h3.a["href"],
                'PostCount': post.select_one('ul ul li').text.strip(),
                "Date": post.find("div", class_="ipsType_light ipsType_reset").time["title"], # time is a tag with the attribute "title"
                "Comment": post.p.text.strip()
            })
        except:
            pass
    return

for x in range(1,211):
    get_comment(x)

df = pd.DataFrame(comments_list)
print(df)
df.to_csv("tielemans_general.csv")