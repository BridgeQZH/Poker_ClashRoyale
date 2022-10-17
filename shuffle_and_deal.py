import random

def shuffle_and_deal(total_card_number=107, player_hold_card_number = 4, common_card_number = 8):
    total_card_number = 107
    player_hold_card_number = 4
    common_card_number = 8

    total_card_list = list(range(total_card_number))
    # print(total_card_list)
    player1_hold_card = random.sample(total_card_list, player_hold_card_number)
    player2_hold_card = random.sample([x for x in total_card_list if x not in player1_hold_card], player_hold_card_number)
    
    remain_card = [x for x in total_card_list if x not in player1_hold_card and x not in player2_hold_card]
    common_card_list = random.sample(remain_card, common_card_number)

    return player1_hold_card, player2_hold_card, common_card_list


