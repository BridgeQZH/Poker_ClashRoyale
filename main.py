# def main():
#     print("Hello World!")

from shuffle_and_deal import shuffle_and_deal
from number_to_card_name import number_to_card_name

if __name__ == "__main__":
    player1_hold_card, player2_hold_card, common_card_list = shuffle_and_deal()
    print("玩家一的手牌：", number_to_card_name(player1_hold_card))
    print("玩家二的手牌：", number_to_card_name(player2_hold_card))
    print("公共牌：", number_to_card_name(common_card_list))
    