from get_api import Get_employers, Get_vacancies
from sql import Create_DB, Adding_data

def main():
    password = input("Введите свой пароль postgresql\n")
    db = Create_DB(password)
    db.create_db()
    tbl = Adding_data(password)
    tbl.create_table()

    company = {'ЭкоПоинт': '5864001',
               'ООО АСД Технолоджиз': '5088268',
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
        data = Get_vacancies(company[i])
        data = data.get_datas()
        data_e = [empl_id, empl_name, open_vacancies]
        tbl.adding_employers(data_e)

        for i in data:
            vacancy_id = i['id']
            employer_id = i['employer']['id']
            vac_name = i['name']
            salary_from = i['salary']['from']
            salary_to = i['salary']['to']
            url = i['alternate_url']
            data_v = [vacancy_id, employer_id, vac_name, salary_from, salary_to, url]
            tbl.adding_vacancy(data_v)


if __name__ == '__main__':
    main()
