import sys
import random
import time

with open("words.txt", 'r') as file:
    words = [ word for word_category in [line.split(',') for line in file.readlines()] for word in word_category]

waiting_time = 1.2

def wait():
    time.sleep(waiting_time)

def print_intro():
    for i in range(3, 0, -1):
        print(str(i)+"...")
        wait()

def print_word():
    print(random.choice(words))
    wait()
    print("...?")
    wait()

def lets_go_baby():
    print_intro()
    while True:
        print_word()

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        try:
            value = float(sys.argv[1])
            if(value>0):
                global waiting_time
                waiting_time = value
        except ValueError:
            pass
    lets_go_baby()