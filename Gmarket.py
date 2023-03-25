# G마켓 크롤링
import requests
import bs4



arr = {1:"낮은 가격 순", 2:"높은 가격 순", 8:"판매 인기 순", 13:"상품평 많은 순", 3:"신규 상품 순"}

print("<G마켓의 마스크 상품 정보>")

for key in arr.keys():
    URL = "https://browse.gmarket.co.kr/search?keyword=마스크&s=" + str(key)
    raw = requests.get(URL)

    html = bs4.BeautifulSoup(raw.text, 'html.parser')

    box = html.find('div', {'class':'section__module-wrap', 'module-design-id':15})

    items = box.find_all('div',{"class":'box__item-container'})

    print("<"+arr[key]+">")

    for item in items[:4]:

        title = item.find('span', {'class':'text__item'})

        price = item.find('strong', {'class' :'text__value'})

        print("이름: ", title.text)

        print("가격: ",price.text)

        print()

