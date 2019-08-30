import requests


def crawl(select_page):
    if select_page == 1:
        url = 'https://terms.naver.com/list.nhn?cid=48156&categoryId=48156'
        data = requests.get(url)  # get() 으로 전체 데이터를 가져온다
        print(str(select_page) + '요청 주소: ' + url)
        return data.content  # 그 중 content 를 return 한다
    else:
        url = 'https://terms.naver.com/list.nhn?cid=48156&categoryId=48156'
        page = f'&page={select_page}'
        page_url = url + page
        data = requests.get(page_url)  # get() 으로 전체 데이터를 가져온다
        print(str(select_page) + '요청 주소: ' + page_url)
        return data.content  # 그 중 content 를 return 한다
