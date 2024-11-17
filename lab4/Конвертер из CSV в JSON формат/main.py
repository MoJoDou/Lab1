# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f_csv:
        r = csv.DictReader(f_csv)  # Считываем строки как словари, где ключи — заголовки столбцов
        csv_data = list(r)  # Преобразуем итератор в список словарей
       # TODO считать содержимое csv файла

      # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f_json:
        json.dump(csv_data, f_json, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
