from csv import DictReader
import json
from files import BOOKS_CSV, USERS_JSON, RESULT_JSON

books = []
reference = {}
references = []

with open(BOOKS_CSV) as f:
    reader = DictReader(f)

    for row in reader:
        books.append(row)

with open(USERS_JSON, "r") as f:
    users = json.loads(f.read())

    for user in users:
        reference.update(
            {
                "name": user["name"],
                "gender": user["gender"],
                "address": user["address"],
                "age": user["age"],
                "books": []
            }
        )
        references.append(reference)

    i = len(books) - 1
    while i != 0:
        for user in references:
            user["books"].append(books[i])
            i -= 1
            if i == 0:
                break

with open('result.json', 'w') as outfile:
    json.dump(references, outfile, indent=1)
