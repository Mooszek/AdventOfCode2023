import os
os.chdir(os.path.dirname(__file__))

total_count = 0


with open("input.txt", "r") as input_file:
    for line in input_file:
        line_total = "";
        for character in line:
            if character.isdigit():
                line_total += str(character)
            
        total_count += int((line_total[0] + line_total[-1]))
        

print(total_count)