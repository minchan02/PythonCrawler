# 벅스차트 크롤링
import requests

import bs4



def ReadyCrawling(URL):

    raw = requests.get(BUGS)

    global html

    html = bs4.BeautifulSoup(raw.text, 'html.parser')





#벅스 크롤링

BUGS = "https://music.bugs.co.kr/chart"

ReadyCrawling(BUGS)



box = html.find('table', {'class':'list trackList byChart'})

songs = box.find_all('tr', {'rowtype':'track'})



print("벅스 차트")

rank = 1

for song in songs[:10]:

    title_box = song.find('p', {'class':'title'})

    title = title_box.find('a').text



    print("%d위 :" %rank,title)



    rank += 1
