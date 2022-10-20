# from pandas import *
# xls = ExcelFile('CR_107.xlsx')
# df = xls.parse(xls.sheet_names[0])
# # dict_we_need = df.to_dict()
# # print(dict_we_need[1])
# print(df)

# import csv
# print(*(csv.DictReader(open('CR_107.csv')), sep='\n')


import csv

def number_to_card_name(number_list):
    
    # dictobj = csv.DictReader(open(csv_filename)).next()
    csv_filename = 'CR_107_2.csv'
    # with open(csv_filename, 'rt') as f:
    #     CR_card_dict = csv.DictReader(f)
    CR_card_dict = csv.DictReader(open(csv_filename))
    # print(CR_card_dict)
    card_name_list = []
    # print(input_file['45'])
    # print(CR_card_dict)
    for select_number in number_list:
        for row in CR_card_dict:
            a=1 # Useless code
        card_name_list.append(row[str(select_number)])

    # print(row)
    return card_name_list

    # with open(csv_filename) as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         print(row)