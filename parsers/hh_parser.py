import requests
from config import HH_API_URL, HH_PARAMS

def get_hh_vacancies():
    response = requests.get(HH_API_URL, params=HH_PARAMS)
    if response.status_code != 200:
        raise Exception(f"Ошибка запроса: {response.status_code}")

    data = response.json()
    vacancies = []

    for item in data["items"]:
        vacancy = {
            "title": item["name"],
            "salary": item.get("salary"),
            "city": item["area"]["name"],
            "url": item["alternate_url"]
        }
        vacancies.append(vacancy)
    return vacancies

if __name__ == "__main__":
    print(get_hh_vacancies()[:2])