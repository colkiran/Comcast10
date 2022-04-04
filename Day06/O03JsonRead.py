
import json

JFR = open("books.json", "r")               # by default it is read mode if not mentioned
jsonfile = json.load(JFR)

# print(jsonfile)
for book in jsonfile['books']:
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 40)


