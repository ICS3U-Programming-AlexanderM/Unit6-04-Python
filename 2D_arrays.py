#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Feb 1 2022
# This program generates random numbers,
# puts these number into a 2D array and calculates the average.
import random
import constant


# function to find average of a 2D list
def calc_average(num_list):
    total = 0
    counter = 0
    for current_row in num_list:
        for current_column in current_row:
            total += current_column
            counter += 1
    # calculate and return the average
    average = total / counter
    return average


def main():
    # declare list
    list_2d = []
    # get input rows and columns from user
    row_string = input("How many rows would you like: ")
    column_string = input("How many columns would you like: ")

    # error checking
    try:
        row = int(row_string)
        column = int(column_string)

        for row_counter in range(0, row):
            temp_column = []
            for column_counter in range(0, column):
                rand_num = random.randint(constant.MIN_NUM, constant.MAX_NUM)
                temp_column.append(rand_num)
                print("{} ".format(rand_num), end="")
            list_2d.append(temp_column)
            print("")

        average_main = calc_average(list_2d)
        print("The average is: {} ".format(average_main))
    except Exception:
        print("Invalid input(s).")


if __name__ == "__main__":
    main()
