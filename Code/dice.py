import random
import time

def normal_dice():
    num = random.randint(1,6)
    return num

def biased_dice(bias):
    array = []
    for i in range(1,7):
        if i != bias:
            array.append(i)
        else:
            for j in range(3):
                array.append(i)
    #print(array)
    num = random.choice(array)
    return num

def getchoice():
    choice = int(input("Enter your choice : \t"))
    return choice

def main():
    print("Choices :\n 1. Normal Dice\n 2. Biased Dice\n 3. Exit")
    choice = getchoice()
    if choice == 1:
        val = normal_dice()
    elif choice == 2:
        bias_at = int(input("Enter the preferred number"))
        val = biased_dice(bias_at)
    elif choice == 3:
        quit()
    else:
        print("Invalid choice")
    print(f"\n{val}\n")
    time.sleep(1)

while True:
    if __name__ == "__main__":
        main()
