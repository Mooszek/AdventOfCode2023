import os
os.chdir(os.path.dirname(__file__))

total_count = 0


with open("input.txt", "r") as input_file:
    for line in input_file:
        line = line.strip()
        line = line.split(":")[1]

        winning_cards, my_cards = line.split("|")[0].split(" "), line.split("|")[1].split(" ")

        raffle_result = 0

        for card in my_cards:
            if card.isdigit()==True and card in winning_cards:
                if raffle_result == 0:
                    raffle_result =1
                else:
                    raffle_result *= 2
        total_count += raffle_result

print(total_count)