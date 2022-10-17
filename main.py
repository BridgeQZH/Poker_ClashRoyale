# def main():
#     print("Hello World!")

from shuffle_and_deal import shuffle_and_deal


if __name__ == "__main__":
    player1_hold_card, player2_hold_card, common_card_list = shuffle_and_deal()
    print("player1_hold_card:", player1_hold_card)
    print("player2_hold_card:", player2_hold_card)
    print("common_card:", common_card_list)
    