import time
mars_points = 0
earth_points = 0
martian_points = 0

print("   o     o")
print("   |_____|")
print("   |0   0|    ____________________")
print("   |_\_/_|__ / Hello! I am Ian the |")
print("   __| |__   \ Alien!!!!! Welcome  |")
print("o==|     |==o \ to my quiz!!!!     /")
print("   |     |     \__________________/")
print("   -------")
print("    || ||")
print("    || ||")
print("     0 0")
print("                   ")
print("                   ")


print("   o     o")
print("   |_____|")
print("   |0   0|    ____________________")
print("   |__O__|__ / My first question is|")
print("   __| |__   \ Do you like social  |")
print("o==|     |==o \ spaces or quiet    /")
print("   |     |     \ spaces?          /")
print("   -------      \________________/")
print("    || ||         A) Social Spaces")
print("    || ||         B) Quiet Spaces ")
print("     0 0")
answer1 = input("My first question is Do you like social spaces or quiet spaces? ")
if answer1 == "A":
    earth_points += 1 
elif answer1 == "B":
    mars_points += 1

print("   o     o")
print("   |_____|")
print("   |0   0|    ____________________")
print("   |_ 3 _|__ / My next question is |")
print("   __| |__   \ Do you like dark    |")
print("o==|     |==o \ or light spaces?   /")
print("   |     |     \                  /")
print("   -------      \________________/")
print("    || ||         A) Dark Spaces")
print("    || ||         B) Light Spaces ")
print("     0 0")
answer1 = input("My next question is Do you like dark or light spaces?")
if answer1 == "B":
    earth_points += 1 
elif answer1 == "A":
    mars_points += 1 

print("   o     o")
print("   |_____|")
print("   |0   0|    ____________________")
print("   |_ w _|__ / My third question is\ ")
print("   __| |__   \ Do you like the     |")
print("o==|     |==o \ color red or       /")
print("   |     |     \ green more?      /")
print("   -------      \________________/")
print("    || ||         A) Green ")
print("    || ||         B) Red   ")
print("     0 0")
answer1 = input("My third question is Do you like the color red or green more?")
if answer1 == "A":
    earth_points += 1 
elif answer1 == "B":
    mars_points += 1 

print("   o     o")
print("   |_____|")
print("   |0   0|    ____________________")
print("   |_ w _|__ / My final Question is\ ")
print("   __| |__   \ Do you like the      |")
print("o==|     |==o \ moon or the         /")
print("   |     |     \ sun more?         /")
print("   -------      \_________________/")
print("    || ||         A) Sun ")
print("    || ||         B) Moon ")
print("     0 0")
answer1 = input("My final question is Do you like the color red or green more?")
if answer1 == "A" or answer1 == "a":
    earth_points += 1 
elif answer1 == "B" and mars_points == 3:
    mars_points +=1 
    martian_points += 1 
print("                                        ")
print("                                        ")
print(" Getting Results...")
time.sleep(3)
print(f"The results are in and you have {mars_points} mars points and {earth_points} earth points you also have {martian_points} secret martian points! Thanks for playing!")