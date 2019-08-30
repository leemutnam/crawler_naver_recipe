from bs4 import BeautifulSoup


def get_recipe(name, link, desc):
    return {'name': name, 'link': link, 'desc': desc}


def parse(data):
    bs_object = BeautifulSoup(data, 'html.parser')
    ul = bs_object.find('ul', {'class': 'content_list'})
    strong = ul.select('li > div.info_area > div.subject > strong')
    summary_list = ul.find_all('p', {'class': 'desc __ellipsis'})
    food = []
    for index, tag in enumerate(strong):
        food_name = tag.select_one('a').text
        food_detail_link = tag.find('a')['href']
        food_summary = summary_list[index].text
        food_dictionary = get_recipe(food_name, food_detail_link, food_summary)
        food.append(food_dictionary)
    return food
