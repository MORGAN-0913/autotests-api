import json
from textwrap import indent

from sqlalchemy import false

json_data1 = '{"name": "Вася", "age": 30, "is_student": true}'
parsed_data1 = json.loads(json_data1)

print(parsed_data1, type(parsed_data1))

json_data2 = """
{
  "name": "Иван",
  "age": 30,
  "is_student": true,
  "courses": [
      "Python",
      "Linux",
      "Automation"]
}"""

parsed_data2 = json.loads(json_data2)
print(parsed_data2["courses"], type(parsed_data2))


data1 = {
  "name": "Мария",
  "age": 25,
  "is_student": False,
}

json_string = json.dumps(data1, indent = 4)

print(json_string, type(json_string))

with open ("json_example.json", "r", encoding="utf-8") as file:
    data2 = json.load(file)
    print(data2, type(data2))

with open ("json_read_file.json", "w", encoding="utf-8") as file:
    json.dump(data1, file, indent = 4, ensure_ascii=False)