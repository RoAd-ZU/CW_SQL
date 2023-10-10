import psycopg2
from get_api import Get_employers, Get_vacancies

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
    def __init__(self, password, employer_id, emp_name, open_vacancies):
        self.password = password
        self.employer_id = employer_id
        self.emp_name = emp_name
        self.open_vacancies = open_vacancies

    def adding_data(self):
        conn = psycopg2.connect(host='localhost', database='cw5', user='postgres', password=self.password)
        datas = (self.employer_id, self.emp_name, self.open_vacancies)
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('CREATE TABLE employers (employer_id int PRIMARY KEY, name varchar(100), open_vacancies int)')
                    cursor.execute(f'INSERT INTO employers (employer_id, name, open_vacancies) VALUES {datas}')
                    cursor.execute('CREATE TABLE vacancy (vacancy_id int PRIMARY KEY, employer_id int, name varchar(300), salary int, url varchar)')
                    cursor.execute('ALTER TABLE vacancy ADD CONSTRAINT fk_vacancy_employers FOREIGN KEY(employer_id) REFERENCES employers(employer_id)')


        finally:
            conn.close()

# passw = '1234509876'
# pppou = Create_DB(passw)
# pppou.create_db()
# ppou = Adding_data(passw)
# ppou.adding_data()