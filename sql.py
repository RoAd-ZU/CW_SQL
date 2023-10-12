import psycopg2


class Create_DB:
    '''Создаёт локальную базу данных с названием "cw5"'''

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
    '''Создаёт таблицы в БД cw5 и заполняет их данными из api.hh.ru'''

    def __init__(self, password):
        self.password = password

    def create_table(self):
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        'CREATE TABLE employers (employer_id int PRIMARY KEY, name varchar(100), open_vacancies int)')
                    cursor.execute(
                        'CREATE TABLE vacancy (vacancy_id int PRIMARY KEY, employer_id int, name varchar(300), salary_from int, salary_to int, url varchar)')
                    cursor.execute(
                        'ALTER TABLE vacancy ADD CONSTRAINT fk_vacancy_employers FOREIGN KEY(employer_id) REFERENCES employers(employer_id)')


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


class DBManager:
    '''Подключается к БД cw5 и производит работу с данными'''

    def __init__(self, password):
        self.password = password

    def get_companies_and_vacancies_count(self):
        '''Получает список всех компаний и количество вакансий у каждой компании.'''
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('SELECT * FROM employers')
                    rows = cursor.fetchall()
                    company_dict = {}
                    for row in rows:
                        key = row[1]
                        value = row[2]
                        company_dict[key] = value
                    return company_dict
        finally:
            conn.close()

    def get_all_vacancies(self):
        '''Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.'''
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('SELECT employers.name, vacancy.name, salary_from, salary_to, url FROM vacancy '
                                   'INNER JOIN employers USING(employer_id)')
                    rows = cursor.fetchall()
                    return rows
        finally:
            conn.close()

    def get_avg_salary(self):
        '''Получает среднюю зарплату по вакансиям.'''
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('SELECT AVG(salary_from), AVG(salary_to) FROM vacancy')
                    rows = cursor.fetchall()
                    return rows
        finally:
            conn.close()

    def get_vacancies_with_higher_salary(self):
        '''Получает список всех вакансий, у которых минимальная зарплата выше средней по всем вакансиям.'''
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
        dbm = DBManager(self.password)
        avg_salary_f = dbm.get_avg_salary()[0][0]
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(f'SELECT * FROM vacancy GROUP BY vacancy_id HAVING salary_from > {avg_salary_f}')
                    rows = cursor.fetchall()
                    return rows
        finally:
            conn.close()

    def get_vacancies_with_keyword(self, keyword):
        '''Получает список всех вакансий, в названии которых содержатся переданные в метод слова'''
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        f"SELECT vacancy.name, salary_from, salary_to, url FROM vacancy WHERE vacancy.name ILIKE '%{keyword}%'")
                    rows = cursor.fetchall()
                    return rows
        finally:
            conn.close()
