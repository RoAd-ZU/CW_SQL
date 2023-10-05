import os
import requests
from exeption import ParsingError
class Get_api_HH():
    """Обращается к сайту HeadHunter и возвращает данные для парсинга по указанным критериям"""
    url = 'https://api.hh.ru/vacancies'

    def __init__(self, keyword, salary_show: bool):
        self.keyword = keyword
        self.salary_show = salary_show
        self.parametrs = {'per_page': 100,
                          'text': self.keyword,
                          'only_with_salary': self.salary_show,
                          'archived': False}

    def get_datas(self):
        response = requests.get(self.url, params=self.parametrs)
        if response.status_code != 200:
            raise ParsingError(f"Возникла ошибка {response.status_code}")
        return response.json()['items']