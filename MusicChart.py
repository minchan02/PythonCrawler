# 벅스, 멜론, 지니 3사의 통합 음악 차트

# 1위부터 100위까지 가중치를 매겨 가중치가 높은 순으로 정렬



import requests

import bs4



SongDict = {}



def GetReadyCrawling(URL):

    raw = requests.get(URL)

    global html

    html = bs4.BeautifulSoup(raw.text, 'html.parser')



def SolveReadyCrawling(URL):

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

    hdr = {'User-Agent':user_agent}

    raw = requests.get(URL, headers=hdr)

    global html2

    html2 = bs4.BeautifulSoup(raw.text, 'html.parser')



def AddSongDict(title, rank):

    if title not in SongDict.keys():

        SongDict[title] = rank

    else:

        SongDict[title] += rank



#벅스 크롤링

BUGS = "https://music.bugs.co.kr/chart"

GetReadyCrawling(BUGS)



box = html.find('table', {'class':'list trackList byChart'})

songs = box.find_all('tr', {'rowtype':'track'})



rank = 100

for song in songs[:100]:

    title_box = song.find('p', {'class':'title'})

    title = title_box.find('a').text

    title = title.strip()



    AddSongDict(title, rank)



    rank -= 1



# 멜론 크롤링 : (참고) https://kin.naver.com/qna/detail.naver?d1id=1&dirId=104&docId=390515161&qb=66mc66Gg7LCo7Yq4IO2BrOuhpOungQ==&enc=utf8&section=kin.ext&rank=2&search_sort=0&spq=0

MELON = "https://www.melon.com/chart/"

SolveReadyCrawling(MELON)



songs = html2.find_all('div', {'class':'ellipsis rank01'})



rank = 100

for song in songs[:100]:

    title = song.find('a').text

    title = title.strip()



    AddSongDict(title, rank)



    rank -= 1



# 지니 크롤링

GENIE = "https://www.genie.co.kr/chart/top200"

SolveReadyCrawling(GENIE)



songs = html2.find_all('tr', {'class':'list'})



rank = 100

for song in songs[:100]:

    title = song.find('a', {'class':'title ellipsis'}).text

    title = title.strip()



    AddSongDict(title, rank)



    rank -= 1



SortedSong = sorted(SongDict.items(), key = lambda x:x[1], reverse = True)



rank = 1

for RankedSong in SortedSong:

    print("%d위 : %s" %(rank, RankedSong[0]))

    

    if rank >= 100:

        break



    rank += 1

