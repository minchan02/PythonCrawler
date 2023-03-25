# 웹툰 평점들 긁어오기
import requests

import bs4



URL = 'https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon'

raw = requests.get(URL)



html = bs4.BeautifulSoup(raw.text, 'html.parser')



target= html.find('div', {'class':'webtoon'})

scores = target.find_all('strong')



i = 71

for score in scores:

  print("%d화 평점 : %s" %(i, score.text))

  i-=1
