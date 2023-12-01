import os
os.chdir(os.path.dirname(__file__))

total_count = 0

string_digits = {"zero" : 0, "one": 1, "two" : 2, "three":3, "four" : 4, "five" : 5, "six": 6, "seven" : 7, "eight": 8, "nine" : 9, "1" :1, "2" :2, "3" :3, "4" : 4, "5" :5 , "6" :6, "7" : 7, "8" :8, "9" : 9 }
string_digits_reverse =  {key[::-1]:string_digits[key] for key in string_digits}

with open("input.txt", "r") as input_file:
    for line in input_file:
        min_val = 100
        max_val = 100
        current_lowest = 0
        current_highest=0

        #getting first number from beggining of the line
        for key, value in string_digits.items():
                if line.find(key) <= min_val and line.find(key) >= 0:
                    current_lowest = value
                    min_val = line.find(key)

        #getting first number from the end of the line using reversed values
        for key, value in string_digits_reverse.items():
                if line[::-1].find(key) <= max_val and line[::-1].find(key) >= 0:
                    current_highest = value
                    max_val = line[::-1].find(key)
        total_count += int(str(current_lowest) + str(current_highest))


print(total_count)