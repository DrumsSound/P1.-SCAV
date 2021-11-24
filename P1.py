"""
Víctor Ferrer
SCAV - P1

"""

import os
from typing import List

import scipy.fftpack as fftpack


# First function translates 3 values in RGB into the 3 YUV values

def rgb_yuv(a, b, c, rgb_to_yuv):
    # Exercise 1
    """Parameters:
        - a,b,c: int RGB or YUV values
        - rgb_to_yuv: boolean that if it's true translates rgb to yuv, if false the reverse
    """
    if rgb_to_yuv:
        Y = (0.257 * a) + (0.504 * b) + (0.098 * c) + 16
        U = (-0.148 * a) - (0.291 * b) + (0.439 * c) + 128
        V = (0.439 * a) - (0.368 * b) - (0.071 * c) + 128
        print("\n Your values in YUV are: ", round(Y), round(U), round(V), "\n")

    elif not rgb_to_yuv:
        B = 1.164 * (a - 16) + 2.018 * (c - 128)
        G = 1.164 * (a - 16) - 0.813 * (b - 128) - 0.391 * (c - 128)
        R = 1.164 * (a - 16) + 1.596 * (b - 128)
        print("\n Your values in RGB are: ", round(R), round(G), round(B), "\n")


def resize(width, height):
    # Exercise 2
    cmd = str(
        "ffmpeg -i lenna.png -vf scale=" + width + ":" + height + " lenna_resized_" + width + "x" + height + ".png")
    os.system(cmd)


def black_and_white(comp_level):
    # Exercise 3
    cmd_1 = 'ffmpeg -i lenna.png -vf format=gray lenna_bw.png'
    os.system(cmd_1)
    cmd_2 = str("ffmpeg -i lenna_bw.png -compression_level " + str(comp_level) + " lenna_compressed.png")
    os.system(cmd_2)


def run_length_enc():
    # Exercise 4
    array = [17, 8, 54, 0, 0, 0, 97, 5, 16, 0, 45, 23, 0, 0, 0, 0, 0, 3, 67, 0, 0, 8]
    print_array(array)
    cont = 0

    for i in range(len(array)):
        if cont != 0:
            cont -= 1
        elif array[i] == 0:
            cont = int(count_0(array, i, 0))
            print(array[i], "", cont, " ", end="")
            cont -= 1
        else:
            print(array[i], " ", end="")
    print("\n")


def count_0(array, position, contador_):
    # Auxiliary function (counts recursively the amount of 0)
    if array[position] == 0:
        cont = count_0(array, position + 1, contador_ + 1)
        return cont
    else:
        return int(contador_)


def print_array(array):
    # Auxiliary function (for printing the arrays
    for i in range(len(array)):
        print(round(array[i]), " ", end="")
    print("\n")


def dct():
    # Exercise 5
    x = [17, 8, 54, 0, 0, 0, 97, 5, 16, 0, 45, 23, 0, 0, 0, 0, 0, 3, 67, 0, 0, 8]
    print(" Original array: \n")
    print_array(x)
    y = fftpack.dct(x, type=2, n=None, axis=-1, norm='ortho', overwrite_x=False, )
    print(" Array converted DCT: \n")
    print_array(y)
    z = fftpack.idct(y, type=2, n=None, axis=-1, norm='ortho', overwrite_x=False)
    print(" Array decoded again: \n")
    print_array(z)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    option = int(input("Choose your action:\n\n  "
                       "1. RGB and YUV translator\n  "
                       "2. Image resize\n  "
                       "3. Convert to b/w\n  "
                       "4. Run-length encoding\n  "
                       "5. DCT convertor\n  "
                       "exit. To end the program\n\n Your action: "))
    while option != 'exit':

        if option == 1:
            rgb_to_yuv_ = bool(
                input(' Enter 1 if you want to Translate RGB to YUV \n Enter 0 if you want to translate YUV to '
                      'RGB \n Your option: '))
            a_ = int(input("\n Enter your first value: "))
            b_ = int(input(" Enter your second value: "))
            c_ = int(input(" Enter your third value: "))

            rgb_yuv(a_, b_, c_, rgb_to_yuv_)

        elif option == 2:
            width_ = str(input(" Enter width: "))
            height_ = str(input(" Enter height: "))
            resize(width_, height_)

        elif option == 3:
            validation = False
            while not validation:
                comp_level_ = int(input(" Enter your compression level (between 1 and 100): "))

                if 1 <= comp_level_ <= 100:
                    black_and_white(comp_level_)
                    validation = True
                else:
                    print(" The option introduced is not correct. Try again. ")

        elif option == 4:
            run_length_enc()

        elif option == 5:
            dct()

        else:
            print("\n The option introduced is not valid. Try again.\n\n")

        option = int(input("\n Choose your action:\n\n  "
                           "1. RGB and YUV translator\n  "
                           "2. Image resize\n  "
                           "3. Convert to b/w\n  "
                           "4. Run-length encoding\n  "
                           "5. DCT convertor\n  "
                           "exit. To end the program\n\n Your action: "))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
