import os
import time

os.system("clear")
os.system("figlet Word-Counter")


path = input("File Directory:  ")
file = open(path)
data = file.read()
words = data.split()
print("Checking...")
time.sleep(4)
print("The Number Of Words Contained In The File Are ", len(words))

