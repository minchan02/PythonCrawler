# 파이썬으로 HTML 코드 가져오기
import requests
URL = 'https://comic.naver.com/webtoon/detail?titleId=758037&no=1'
raw = requests.get(URL)

print(raw.text)
