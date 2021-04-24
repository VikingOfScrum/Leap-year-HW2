'''
Simple program to check if inputted year is a leap year or not.

Greet user
Ask user for input
if input is not valid ask again for input
check if input is valid int or exit
if input is not valid and input is exit, exit program
if input is valid check if given year is leap
print output

Joseph Hanson
'''


def print_if_leap(input_year):
    '''
    Checks if input is a leap year.
    leap years are years divisable by 4 and or 400
    non leap years all years not divisable by 4 and or 400
    '''
    input_year = int(input_year)
    if input_year % 100 == 0 and input_year % 400 != 0:
        print(input_year, "is not a leap year.")
    elif input_year % 4 == 0 or input_year % 400 == 0:
        print(input_year,"is a leap year.")
    else:
        print(input_year, "is not a leap year.")

def main():
    '''
    Main driver function for the assignment.
    greets users with what the program does.
    uses a for loop to repeat while play is True.
    asks user for input then sends input to check function.
    if check function returns true sends it to print leap year function.
    if user types 'exit' play will become false and exit the program.
    '''

    print("Hello, This program is designed to check if the input year is a leap year.")
    play = True
    exit_program = "exit"

    while play == True:
        input_year = input("Please enter a year or type 'exit' to quit: ")

        print_if_leap(input_year)


if __name__=='__main__':
    main()