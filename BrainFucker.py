################################
#   Interpreter for the BrainFuck code language
#   author: Nicola Valcasara
#   written for the AIV01 course, 3rd year
#   09/11/2021
################################
import os

cellIdx = 0
cells = [0] * 27

def print_instructions():
    print("*********************************************************************")
    print("*                                                                   *")
    print("*  This interpreter will solve the brainfuck code you will write    *")
    print("*                                                                   *")
    print("*                       Characters allowed:                         *")
    print("*                       + - < > . [ ] only                          *")
    print("*                            x for exit                             *")
    print("*                                                                   *")
    print("*********************************************************************")


def change_cell(cellMove):
    global cellIdx
    cellIdx += cellMove

    if cellIdx < 0:
        raise Exception("out of bounds moving to cell " + str(cellIdx))


def change_number(number):
    global cellIdx
    cells[cellIdx] += number


def process_input(userin):

    possibleLoop = ""
    for ch in userin:

        if ch == '+':
            change_number(+1)
        elif ch == '-':
            change_number(-1)
        elif ch == '>':
            change_cell(+1)
        elif ch == '<':
            change_cell(-1)
        elif ch == '['
            possibleLoop += 

def print_result():
    print(*cells)


def clear():
    os.system('cls')


if __name__ == '__main__':

    waitNewInput = True
    while waitNewInput:
        clear()

        print_instructions()

        # user iteraction
        userInput = input()
        if userInput == 'x':
            waitNewInput = False

        try:
            process_input(userInput)
        except Exception as err:
            print(err)

        print_result()
