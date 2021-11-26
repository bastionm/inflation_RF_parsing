import requests
from bs4 import BeautifulSoup
import csv

# Ссылка на нашу страниццу для парсинга
url = "https://уровень-инфляции.рф/таблицы-инфляции"

# Пробрасываем заголовки, чтобы сайт не подумал, что мы бот
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36"
}

# req возвращает результат работы метода .get
req = requests.get(url, headers=headers)
src = req.text
# print(src)

# Сохраняем получившуюся страницу в файл
with open ("inflation.html", "w", encoding = "utf-8") as file:
    file.write(src)

# Прочитаем файл и сохраним в переменную
with open ("inflation.html", encoding = "utf-8") as file:
    src = file.read()

# Создадим объект супа и передадим переменную src, парсер lxml
soup = BeautifulSoup(src, "lxml")

# Спарсим конкретный блок. Далле будем по каждым мини-блокам проходить
items = soup.find("table", class_="table table-hover table-sm").find("tbody").find_all("tr")
year_inflation = []

# Спарсили мини блоки и сохранили их в список. И все списки сохранили в один большой список
for item_1 in items:
        x = item_1.find_all("td")
        for item_2 in range(len(x)):
            x[item_2] = x[item_2].text
        year_inflation.append(x)
print(year_inflation)


# Сохраняем все это дело в CSV файл
CSV = 'inflation.csv'

with open (CSV, 'w', newline='', encoding="utf-16") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["Year", "January", "February", "March", "April", "May",
                     "June", "July", "August", "September", "October", "November",
                     "December", "General"])
    for item in year_inflation:
        writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5],
                         item[6], item[7], item[8], item[9], item[10], item[11],
                         item[12], item[13]])
