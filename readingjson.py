import json
path = '/Users/tekendra/downloads/pydata-book-2nd-edition/datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]
for rec in records:
    print(rec)
