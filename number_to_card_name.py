import csv

def number_to_card_name(number_list):
    Chinese_flag = 1
    if Chinese_flag == 1:
        csv_filename = 'CR_107_zh.csv'
    else:
        csv_filename = 'CR_107_en.csv'
    CR_card_dict = csv.DictReader(open(csv_filename))
    card_name_list = []
    for select_number in number_list:
        for row in CR_card_dict:
            a=1 # Useless code
        card_name_list.append(row[str(select_number)])
    return card_name_list
