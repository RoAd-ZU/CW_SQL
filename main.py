from get_api import Get_employers, Get_vacancies
from sql import Create_DB, Adding_data, DBManager


def main():
    password = input("Введите свой пароль postgresql\n")
    dbm = DBManager(password)
    try:
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
    except:
        print('База данных уже существует, можете приступить к выборке данных.')

    inp = input('Для получения списка компаний с указанием количества вакансий у каждой компании, введите цифру 1.\n')
    if inp == '1':
        print(dbm.get_companies_and_vacancies_count())
    inp = input('Для получения списка всех вакансий с указанием названия компании, зарплаты от, зарплаты до '
                'и ссылки на вакансию, введите цифру 1.\n')
    if inp == '1':
        print(dbm.get_all_vacancies())
    inp = input(
        'Для получения информации о средней мнимальной и максимальной зарплаты по всем вакансиям, введите цифру 1.\n'
        'Стоит учесть, что если минимальная или максимальная зарплата не указана, значение приравнивается к нулю.\n')
    if inp == '1':
        rows = dbm.get_avg_salary()
        print(f'Средняя минимальная зарплата - {rows[0][0]}\nCредняя максимальная зарплата - {rows[0][1]}')
    inp = input('Для получения списка всех вакансий, у которых минимальная зарплата выше средней минимальной '
                'по всем вакансиям, введите цифру 1\n')
    if inp == '1':
        print(dbm.get_vacancies_with_higher_salary())
    inp = input('Для поиска вакансий по ключевому слову (в названии вакансии), введите ключевое слово\n')
    if inp != '':
        print(dbm.get_vacancies_with_keyword(inp))


if __name__ == '__main__':
    main()
