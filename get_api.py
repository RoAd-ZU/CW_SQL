import requests
from exeption import ParsingError


class Get_employers():
    """Обращается к сайту HeadHunter и возвращает информацию о работодателе"""

    def __init__(self, emp_id: str):
        self.url = 'https://api.hh.ru/employers/' + emp_id

    def get_datas(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ParsingError(f"Возникла ошибка {response.status_code}")
        return response.json()


class Get_vacancies():
    """Обращается к сайту HeadHunter и возвращает информацию о вакансиях выбранных работодателей"""
    url = 'https://api.hh.ru/vacancies'

    def __init__(self, employer_id):
        self.employer_id = employer_id
        self.parametrs = {'per_page': 50,
                          'employer_id': self.employer_id,
                          "currency": "RUR",
                          'only_with_salary': True,
                          'archived': False}

    def get_datas(self):
        response = requests.get(self.url, params=self.parametrs)
        if response.status_code != 200:
            raise ParsingError(f"Возникла ошибка {response.status_code}")
        return response.json()['items']
