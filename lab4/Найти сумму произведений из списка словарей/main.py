# TODO решите задачу
import json

INPUT_FILE = "input.json"

def task() -> float:
    with open(INPUT_FILE, encoding="utf-8") as f:
        json_data = json.load(f)

    total = sum(item["score"] * item["weight"] for item in json_data)  # Сумма произведений
    return round(total, 3)  # Округляем до 3 знаков

print(task())
