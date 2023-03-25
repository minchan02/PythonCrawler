# csv라이브러리를 활용한 기사 제목 크롤링
import csv



f = open('./covid19_articles.csv', 'r')



rdr = csv.reader(f)



ans = 0



next(rdr)



for row in rdr:

    if '[속보]' in row[2]:

        ans += 1

        print(row[2])



print("속보 기사 개수 : ", ans)
