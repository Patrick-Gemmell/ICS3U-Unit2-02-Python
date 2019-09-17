#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: September 12 2019
# This calculated the area of a rectangle with variables


def main():
    # this function calculates area and perimeter

    Length = int(input("Enter Length of the rectangle (mm): "))
    width = int(input("Enter Width of hte rectangle (mm)"))

    area = Length*width
    perimeter = 2*(Length+width)

    print("")
    print("Area is {}mm**2".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
