import psycopg2

class Create_DB:
    def __init__(self, password):
        self.password = password

    def create_db(self):

        conn = psycopg2.connect(dbname="postgres", user="postgres", password=self.password, host='localhost')
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute('CREATE DATABASE cw5')
        cursor.close()
        conn.close()


class Adding_data:
    def __init__(self, password):
        self.password = password


    def create_table(self):
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)

        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('CREATE TABLE employers (employer_id int PRIMARY KEY, name varchar(100), open_vacancies int)')
                    cursor.execute('CREATE TABLE vacancy (vacancy_id int PRIMARY KEY, employer_id int, name varchar(300), salary_from int, salary_to int, url varchar)')
                    cursor.execute('ALTER TABLE vacancy ADD CONSTRAINT fk_vacancy_employers FOREIGN KEY(employer_id) REFERENCES employers(employer_id)')


        finally:
            conn.close()
    def adding_employers(self, data):
        self.data = data
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
        data_e = (self.data[0], self.data[1], self.data[2])
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(f'INSERT INTO employers VALUES {data_e}')

        finally:
            conn.close()

    def adding_vacancy(self, data):
        self.data = data
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
        if self.data[3] == None:
            self.data[3] = 0
        if self.data[4] == None:
            self.data[4] = 0
        data_v = (self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5])
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(f'INSERT INTO vacancy VALUES  {data_v}')

        finally:
            conn.close()


# class DBManager:
#     def __init__(self, password):
#         self.password = password
#         self.conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
#
#     def get_companies_and_vacancies_count():
#         '''получает список всех компаний и количество вакансий у каждой компании.'''
#         try:
#             with self.conn:
#
#     def get_all_vacancies():
#         '''получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.'''
#
#
#     def get_avg_salary():
#         '''получает среднюю зарплату по вакансиям.'''
#
#
#     def get_vacancies_with_higher_salary():
#         '''получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.'''
#
#
#     def get_vacancies_with_keyword():
#         '''получает список всех вакансий, в названии которых содержатся переданные в метод слова'''

