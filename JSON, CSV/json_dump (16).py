import json

films = [
    'Империя наносит ответный удар',
    'Возвращение джедая',
    'Скрытая угроза',
    'Атака клонов',
    'Месть ситхов'
]
yoda = {
    'name': 'Йода',
    'height': '66',
    'mass': '17',
    'hair_color': 'белый',
    'skin_color': 'зеленый',
    'films': films
}

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(yoda, file, ensure_ascii=False, indent=2)
