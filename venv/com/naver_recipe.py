import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from libs.naver_recipe.crawler import crawl
from libs.naver_recipe.parser import parse
from libs.naver_recipe.save import save_excel

all_food = []
end_page = 594


def pipe(end):
    for page_number in range(1, end + 1):
        page_string = crawl(page_number)
        foods = parse(page_string)
        for food in foods:
            all_food.append(food)


pipe(end_page)
save_excel(all_food)
