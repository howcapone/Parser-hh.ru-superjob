import requests
from bs4 import BeautifulSoup
from time import sleep
from config import SUPERJOB_URL


def get_superjob_vacancies():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "ru-RU,ru;q=0.9"
    }

    try:
        response = requests.get(SUPERJOB_URL, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        soup = BeautifulSoup(response.text, "html.parser")

        vacancies = []
        # Ищем все карточки вакансий по общему родительскому тегу (например, div с вакансиями)
        for card in soup.select('div[class*="vacancy-item"]'):  # Ищем div, где класс содержит "vacancy-item"
            title_elem = card.find('a', {'target': '_blank'})  # Ссылка с target="_blank" — обычно это заголовок
            salary_elem = card.find('span', string=lambda t: 'руб.' in t if t else False)  # Ищем span с текстом 'руб.'
            city_elem = card.find(
                attrs={"class": lambda x: x and "location" in x})  # Ищем элемент, где в классе есть 'location'

            if not all([title_elem, salary_elem, city_elem]):
                continue  # Пропускаем неполные карточки

            vacancies.append({
                "title": title_elem.get_text(strip=True),
                "salary": salary_elem.get_text(strip=True),
                "city": city_elem.get_text(strip=True),
                "url": "https://www.superjob.ru" + title_elem['href']
            })

        return vacancies

    except Exception as e:
        print(f"Ошибка при парсинге SuperJob: {e}")
        return []

if __name__ == "__main__":
    print(get_superjob_vacancies()[:2])