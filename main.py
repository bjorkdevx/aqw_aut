import pyautogui
import time
import os 
import subprocess
import sys
import random

FIRST_X, FIRST_Y = 552, 696# key 2 coldon typ 2,6 sec
SECOND_X, SECOND_Y = 612, 705 # key 3 coldon typ 6.2 sec 
THIRD_X, THIRD_Y = 655, 706 # key 4 15.4 sec
FOURTH_X, FOURTH_Y = 722, 705 # key 5 15,5 sec


SEVEN_MONEY_1_X, SEVEN_MONEY_1_Y = 763, 66
SEVEN_MONEY_2_X, SEVEN_MONEY_2_Y = 826, 68



GIT_REPO = "https://github.com/bjorkdevx/aqw_aut.git"

ATTACKS = {
    1: lambda: pyautogui.leftClick(FIRST_X, FIRST_Y),
    2: lambda: pyautogui.leftClick(SECOND_X, SECOND_Y),
    3: lambda: pyautogui.leftClick(THIRD_X, THIRD_Y),
    4: lambda: pyautogui.leftClick(FOURTH_X, FOURTH_Y)
}



#Failsafe move to left coner to stop
pyautogui.FAILSAFE = True
#need inprovment
ARCH_PALADIN_SOLO_DPS = [
    (3, 1),
    (1, 3.0),
    (1, 2.0),
    (4, 1),
    (1, 3),
    (1, 3),
    (1, 1),
    (2, 1),  
]  

#done
ARCH_PALADIN_FARMING = [
    #combo to add 4225223 look att the top to now what to write
    (3, 1),
    (1, 3),
    (1, 1),
    (4, 2),
    (1, 3),
    (1, 2.6),
    (2, 2),

    
]

ARCH_PALADIN_SUPPORT = [
    # 4225224
    (3, 1),
    (1, 3),
    (1, 1),
    (4, 2),
    (1, 3),
    (1, 2.6),
    (2, 2),
]

ARCH_PALADIN_TANK = [
    #422532232
    (1, 2.6),
]

ARCH_PALADIN_FARMING_MONEY = [
    #combo to add 4225223 look att the top to now what to write
    (3, 1),
    (1, 3),
    (1, 1),
    (4, 2),
    (1, 3),
    (1, 2.6),
    (2, 2),

    
]



IMPERIAL_CHUNIN_FARMING = [
    #3245 3254 
    (2, 2),
    (1, 1),
    (3, 1),
    (4, 1),
    (2, 2),
    (1, 1),
    (4, 2),
    (3, 2),


]


SWORD_MASTER_RANDOM = [
    #3245 3254 
    (2, 2),
    (1, 2),
    (3, 1),
    (4, 1),
    (2, 2),
    (1, 1),
    (4, 2),
    (3, 2),


]

BLOOD = [
    #3245 3254 
    (1, 2),
    (2, 2),
    (3, 2),
]



def run_rotation_arch_paladin(rotation):
    print("starting rotation (move mouse to top-left to stop)")
    print("starting in 5 sec")
    time.sleep(5)
    while True:
        for attack, delay in rotation:
            print(f"Attacking with key {attack}...")
            ATTACKS[attack]()
            if attack == 2:
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("T")
            time.sleep(delay)

def run_rotation_swrod_master(rotation):
    print("starting rotation (move mouse to top-left to stop)")
    print("starting in 5 sec")
    time.sleep(5)
    while True:
        for attack, delay in rotation:
            print(f"Attacking with key {attack}...")
            ATTACKS[attack]()
            if attack == 2:
                pyautogui.press("esc")
                time.sleep(1)
                pyautogui.press("T")
            time.sleep(delay)



def run_rotation_blood_farming(rotation):
    print("starting rotation (move mouse to top-left to stop)")
    print("starting in 5 sec")
    time.sleep(5)
    random_chance_interval = 4
    while True:
        for attack, delay in rotation:
            print(f"Attacking with key {attack}...")
            ATTACKS[attack]()
            time.sleep(delay)
         
            if random.randint(1, random_chance_interval) == 1:
                if random.randint(1,2) == 1:
                    print("turin in money")
                    pyautogui.leftClick(SEVEN_MONEY_1_X, SEVEN_MONEY_1_Y)
                    time.sleep(1.5)
                    pyautogui.leftClick(SEVEN_MONEY_2_X, SEVEN_MONEY_2_Y)


def run_rotation_imperial_chunin_farming(rotation):
    print("starting rotation (move mouse to top-left to stop)")
    print("starting in 5 sec")
    time.sleep(5)
    random_chance_interval = 2
    while True:
        for attack, delay in rotation:
            print(f"Attacking with key {attack}...")
            ATTACKS[attack]()
            time.sleep(delay)
         
            if random.randint(1, random_chance_interval) == 1:
                if random.randint(1,2) == 1:
                    print("turin in money")
                    pyautogui.leftClick(SEVEN_MONEY_1_X, SEVEN_MONEY_1_Y)
                    time.sleep(1.5)
                    pyautogui.leftClick(SEVEN_MONEY_2_X, SEVEN_MONEY_2_Y)

                   
def run_rotation_arch_paladin_moeny(rotation):
    print("starting rotation (move mouse to top-left to stop)")
    print("starting in 5 sec")
    time.sleep(5)
    random_chance_interval = 2
    while True:
        for attack, delay in rotation:
            print(f"Attacking with key {attack}...")
            ATTACKS[attack]()
            time.sleep(delay)
         
            if random.randint(1, random_chance_interval) == 1:
                if random.randint(1,2) == 1:
                    print("turin in money")
                    pyautogui.leftClick(SEVEN_MONEY_1_X, SEVEN_MONEY_1_Y)
                    time.sleep(1.5)
                    pyautogui.leftClick(SEVEN_MONEY_2_X, SEVEN_MONEY_2_Y)


def swrod_master():
    pick = input("""
     Sword Master
     ------------
     1: "random"

     Pick an otion: """)
    options = {
        "1": lambda: run_rotation_swrod_master(SWORD_MASTER_RANDOM),
    }
    if pick in options:
        options[pick]()
    else:
        main()


def arch_paladin():
    
    pick = input("""
     ARCH PALADIN
     ------------
     1: "Solo dps"
     2: "Farming"
     3: "Support"
     4: "Tank"

     Pick an otion: """)
    options = {
        "1": lambda: run_rotation_arch_paladin(ARCH_PALADIN_SOLO_DPS),
        "2": lambda: run_rotation_arch_paladin(ARCH_PALADIN_FARMING),
        "3": lambda: run_rotation_arch_paladin(ARCH_PALADIN_SUPPORT),
        "4": lambda: run_rotation_arch_paladin(ARCH_PALADIN_TANK)
    }
    if pick in options:
        options[pick]()
    else:
        main()




def position():
    print("postion")
    time.sleep(4)
    print(pyautogui.position())
    main()


def farming_stuff():
    
    pick = input("""Pick 1 of the options\n


    1: Arch paladin
    2: imperial chunin 
    3: blood
                
    """)

    options = {
        
        "1": lambda: run_rotation_arch_paladin(ARCH_PALADIN_FARMING_MONEY),
        "2": lambda: run_rotation_imperial_chunin_farming(IMPERIAL_CHUNIN_FARMING),
        "3": lambda: run_rotation_blood_farming(BLOOD),
        }

    if pick in options:
        options[pick]()
    else:
        print("No valed optin going to main meanu")
        main()








def update():
    print("pulling the latest update")
    try:
        subprocess.run(["git", "pull", "origin", "main"])
        print("Repo clone successfully!")
        main()
    except subprocess.CalledProcessError:
        print("Failed to pull the latest changes!")

       


def main():
    print("Welcome to AutoClicker Tool!")
    print("_______________________________")
    pick = input("""Pick 1 of the options\n
                1: Arch paladin
                2: Sword Master
                3: Farming
                9: Get position
                0: Update
                 """)

    options = {
        "1": arch_paladin,
        "2": swrod_master,
        "3": farming_stuff,
        "9": position,
        "0": update,
    }

    if pick in options:
        options[pick]()
    else:
        print("pick")
        main()

if __name__ == "__main__":
    main()

