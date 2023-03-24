import random


def main():
    level = inputLevel()
    number = chooseNumber(level)
    game(number, inputNumber())


def inputLevel():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                inputLevel()
        except (TypeError, ValueError):
            continue

        return level


def chooseNumber(level):
    number = random.randint(1, level)
    return number


def inputNumber():
    while True:
        try:
            givenNumber = int(input("Guess: "))
            if givenNumber <= 0:
             inputNumber()
        except (ValueError, TypeError):
            continue
        
        return givenNumber


def game(number, givenNumber):
    while True:
        if number < givenNumber:
            print("Too Large")
            givenNumber = inputNumber()
        elif number > givenNumber:
            print("Too small")
            givenNumber = inputNumber()
        else:
            print("Just Right")
            break


main()
