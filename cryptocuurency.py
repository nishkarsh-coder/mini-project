from bs4 import BeautifulSoup
import requests
import time


def crypto():
    # coin= input("enter the coin name")

    url= "https://www.google.co.in/search?q=bitcoin+price&sxsrf=ALeKk03KL-DJ0aeN4o95t7FMeHN3CBo6Mw%3A1625601533099&source=hp&ei=_bXkYO2DBNOprtoP2NaF6As&iflsig=AINFCbYAAAAAYOTEDQRrp5l23CLCv2OsHNgV7x6EuJvI&oq=&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzoGCCMQJxATOgQIIxAnOgUIABCxAzoICAAQsQMQgwE6AggAOgQIABBDOgoILhDHARCjAhBDOgQILhBDOg4ILhCxAxCDARDHARCjAjoHCAAQsQMQQzoKCAAQsQMQgwEQQ1CQDlixH2DzNGgDcAB4AIABugGIAfQDkgEDMC4zmAEAoAEBqgEHZ3dzLXdperABCg&sclient=gws-wiz"

    HTML = requests.get(url)
    # print(HTML.content)
    soup =  BeautifulSoup(HTML.content, "html.parser")
    # print(soup.prettify())
    value= soup.find('span',attrs= {'class':'DFlfde SwHCTb'})
    # print(value.get_text())
    return value.get_text()

last_price=0
while True:
  price= crypto()
  if last_price!=price:
    print(price)
    last_price=price
  time.sleep(3)




