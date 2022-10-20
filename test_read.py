import csv
csv_filename = 'CR_107_2.csv'
with open(csv_filename, 'rt') as f:
    reader = csv.DictReader(f)
    # reader_dict = dict(reader)
    # print(reader_dict)
    for row in reader:
        print(row)