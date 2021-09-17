#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This function asks the user to guess a number between 1 and 9

import constants


def main():
    # This function asks the user to guess a number between 1 and 9

    # input
    guessed_number = int(input("Enter a number between 1 and 9: "))
    print("")

    # process & output
    if guessed_number == constants.NUMBER:
        print("YAAAAY you guessed it right!!!")

    if guessed_number != constants.NUMBER:
        print(" :( you guessed wrong, try again.")

    print("Done.")


if __name__ == "__main__":
    main()
