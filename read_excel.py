# from pandas import *
# xls = ExcelFile('CR_107.xlsx')
# df = xls.parse(xls.sheet_names[0])
# # dict_we_need = df.to_dict()
# # print(dict_we_need[1])
# print(df)

# import csv
# print(*(csv.DictReader(open('CR_107.csv')), sep='\n')


import csv
csv_filename = 'CR_107_2.csv'

input_file = csv.DictReader(open(csv_filename))
# dictobj = csv.DictReader(open(csv_filename)).next() 

# print(input_file['45'])
select_number = 29

for row in input_file:
    # print(row)
    print(row[str(select_number)])


# with open(csv_filename) as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)