from parsers.hh_parser import get_hh_vacancies
from parsers.superjob_parser import get_superjob_vacancies
from storage.json_saver import save_to_json
from analysis.salary_analyzer import analyze_salaries

def main():
    hh_vacancies = get_hh_vacancies()
    sj_vacancies = get_superjob_vacancies()
    all_vacancies = hh_vacancies + sj_vacancies

    save_to_json(all_vacancies, "all_vacancies.json")

    salary_stats = analyze_salaries(all_vacancies)
    print("Средние зарплаты:")
    for city, salary in salary_stats.items():
        print(f"{city}: {salary:.2f} руб.")

if __name__ == "__main__":
    main()