#!/usr/bin/env python3

# Created by : Ntare Katarebe
# Created on : May 2021
# This program prints out your Address


def full_address(full_name, street_name, street_number,
        city, province, postal_code, apt_number = None):
    # return the full formal name

    full_address = full_name
    if apt_number != None:
        full_address = full_address + " " + apt_number[0]
    full_address = full_address + "\n" + street_name
    full_address = full_address + " " + street_number
    full_address = full_address + "\n" + city
    full_address = full_address + " " + province
    full_address = full_address + " " + postal_code

    return full_address


def main():
    # gets a users name and prints out their formal name
    apt_number = None

    full_name = input("Enter your full name: ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name and type (Main St.): ")
    city = input("Enter your city name: ")
    province = input("Enter your province name: ")
    postal_code = input("Enter your postal code: ")

    if apt_number != None:
          name = full_address(full_name, apt_number, street_number,
            street_name, city, province, postal_code)
    else:
          name = full_address(full_name, street_number, street_name,
            city, province, postal_code)

    print(name)


if __name__ == "__main__":
    main()
