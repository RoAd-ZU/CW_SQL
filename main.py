from get_api import Get_employers, Get_vacancies
from sql import Create_DB, Adding_data
import psycopg2

# input("Введите свой пароль postgresql\n")
def main():
    password = '1234509876'
    db = Create_DB(password)
    db.create_db()
    company = {'ЭкоПоинт': '5864001',
               'ПАО ВТБ': '4181',
               'Алабуга': '68587',
               'Алгоритмика': '2657797',
               'Lad': '93051',
               'NAUMEN': '42600',
               'Тензор': '67611',
               'Positive Technologies': '26624',
               'Риверстарт': '1262880',
               'Сбер': '3529'}
    for i in company:
        data = Get_employers(company[i])
        data = data.get_datas()
        empl_id = data['id']
        empl_name = data['name']
        open_vacancies = data['open_vacancies']
        sql = Adding_data(password, empl_id, empl_name, open_vacancies)
        sql.adding_data()


        # tyu = Get_employers('2657797')
        # yet = tyu.get_datas()['vacancies_url']
        # tre = Get_vacancies(yet)
        # print(tre.get_datas())

if __name__ == '__main__':
    main()
