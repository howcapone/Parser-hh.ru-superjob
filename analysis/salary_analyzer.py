def analyze_salaries(vacancies):
    city_salaries = {}

    for vacancy in vacancies:
        city = vacancy["city"]
        salary = vacancy.get("salary")

        if not salary:
            continue
        try:
            salary_value = int(salary.split()[0].replace(" ", ""))
        except (ValueError, AttributeError):
            continue
        if city not in city_salaries:
            city_salaries[city] = []
        city_salaries[city].append(salary_value)
    result = {}
    for city, salaries in city_salaries.items():
        result[city] = sum(salaries) / len(salaries)
    return result