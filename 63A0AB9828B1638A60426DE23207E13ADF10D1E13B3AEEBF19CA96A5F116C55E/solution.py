#Not much reversing was needed, all you need to do is input a key of 16, and when stepping in ida, you'll see it compared to another string.
#Usually the other string contains 1 digit, 1 upper char, and 1 lower char
#So I made a program to read a process dump of the program, which can be made when it's asking you for the key, and the program looks at the strings, and looks for strings that meet the criteria listed above
#You can read the program for more info
#Command: strings64.exe k.DMP | py sick.py
def meets_criteria(input_string):
    if len(input_string) != 16:
        return False

    if not any(char.islower() for char in input_string):
        return False

    if not any(char.isupper() for char in input_string):
        return False

    if not any(char.isdigit() for char in input_string):
        return False
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    if not all(char in valid_chars for char in input_string):
        return False

    return True

if __name__ == "__main__":
    i = 0
    while True:
        user_input = input()
        if meets_criteria(user_input):
            i += 1
            print(user_input)
            if (i > 5):
                print("The key should be listed above, make sure it isn't a expired key (the one printed by the program) and isn't an API or something (you should be able to tell), if it isn't listed above, do the process again")
                exit()
