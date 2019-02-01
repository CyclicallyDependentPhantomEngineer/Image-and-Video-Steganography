from pyfiglet import Figlet
from functions import *
from subprocess import call,STDOUT
import os


if __name__ == '__main__':

    print("Menu :")
    print("")
    print("(a) Encypt & Merge into Video")
    print("(b) Decrypt & Get the plain text")
    print("-----------------------")
    choice = raw_input("(!) Choose option : ")

    if choice == "a":
        call(["clear"])

        print("----------------------------------------")
        file_name = raw_input("(1) Video file name in the Desktop ? : ")

        try:
            caesarn = int(raw_input("(2) Caesar cypher n (Shift value) value ? : "))
        except ValueError:
            print("-----------------------")
            print("(!) n is not an integer ")
            exit()

        try:
            open("/root/Desktop/" + file_name)
        except IOError:
            print("-----------------------")
            print("(!) File not found ")
            exit()

        print("-----------------------")
        print("(-) Extracting Frame(s)")
        frame_extract(str(file_name))
        print("(-) Extracting audio")
        call(["ffmpeg", "-i", "/root/Desktop/" + str(file_name), "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
        print("(-) Reading text-to-hide.txt")
        print("(-) Encrypting & appending string into frame(s) ")
        encode_frame("temp", "/root/Desktop/text-to-hide.txt", caesarn)
        print("(-) Merging frame(s) ")
        call(["ffmpeg", "-i", "/root/Desktop/temp/%d.png" , "-vcodec", "png", "/root/Desktop/temp/video.mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)

        print("(-) Optimizing encode & Merging audio ")
        call(["ffmpeg", "-i", "temp/video.mov", "-i", "temp/audio.mp3", "-codec", "copy","/root/Desktop/enc-" + str(file_name)+".mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
        print("(!) Success , output : enc-" + str(file_name)+".mov")

    elif choice == "b" :
        call(["clear"])
        print("----------------------------------------")
        file_name = raw_input("(1) Video file name in Desktop  ? : ")

        try:
            caesarn = int(raw_input("(2) Caesar cypher n(Shift) value  ? : "))
        except ValueError:
            print("-----------------------")
            print("(!) n is not an integer ")
            exit()

        try:
            open("/root/Desktop/" + file_name)
        except IOError:
            print("-----------------------")
            print("(!) File not found ")
            exit()

        print("-----------------------")
        print("(-) Extracting Frame(s)")
        frame_extract(str(file_name))
        print("(-) Decrypting Frame(s)")
        decode_frame("temp",caesarn)
        print("(-) Writing to recovered-text.txt")
        print("(!) Success")


    else:
        exit()

