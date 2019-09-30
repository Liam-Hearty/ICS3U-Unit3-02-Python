#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program makes the user guess the chosen number.


import constants


def main():
    # This program makes the user guess the chosen number.

    # input
    chosen_number = int(input("Enter your guess between 0-9: "))

    # process
    if chosen_number != 5:
        # output
        print("Wrong!")

    # process
    if chosen_number == 5:
        # output
        print("Correct!!")


if __name__ == "__main__":
    main()
