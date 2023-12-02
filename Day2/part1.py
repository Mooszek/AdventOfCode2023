import os
os.chdir(os.path.dirname(__file__))

game_id = 1

max_red = 12
max_green = 13
max_blue = 14

current_color = ""
current_number = 0

total_count = 0

with open("input.txt", "r") as input_file:

    
    for line in input_file:
        
        game_correct = True

        #remove game id
        line = line.strip()
        line = line.split(":")[1]


        line = line.replace(";", "")
        line = line.replace(",", "")
        
        line = line.split(" ")

        for pick_color in line[::-1]:
            if pick_color.isalpha():
                current_color = pick_color
            elif pick_color.isnumeric():
                current_number = int(pick_color)
                if current_color == "green" and current_number > max_green:
                    game_correct = False
                if current_color == "blue" and current_number > max_blue:
                    game_correct = False
                if current_color == "red" and current_number > max_red:
                    game_correct = False
                current_color = ""

        if game_correct is True:
            total_count += game_id

        game_id +=1

print(total_count)