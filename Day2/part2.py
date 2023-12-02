import os
os.chdir(os.path.dirname(__file__))

game_id = 1

current_color = ""
current_number = 0

total_count = 0

with open("input.txt", "r") as input_file:

    
    for line in input_file:
        
        max_red = 0
        max_green = 0
        max_blue = 0

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
                    max_green = current_number
                if current_color == "blue" and current_number > max_blue:
                    max_blue = current_number
                if current_color == "red" and current_number > max_red:
                    max_red = current_number
                current_color = ""
        
        total_count += (max_blue* max_green * max_red)

print(total_count)