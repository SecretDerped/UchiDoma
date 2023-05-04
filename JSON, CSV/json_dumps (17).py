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

result = json.dumps(yoda, ensure_ascii=False, indent=2)
print(type(result))
print(result)
