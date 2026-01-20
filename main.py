import pyautogui
import time
import os 
import subprocess
import sys
import random


ATTACKS = {}

PRESETS = {
    "1": {
        "FIRST": (552, 696),
        "SECOND": (612, 705 ),
        "THIRD": (655, 706 ),
        "FOURTH": (722, 705 ),
        "MONEY_1": (763, 66),
        "MONEY_2": (826, 68),
    },
    "2": {
        "FIRST": (833, 955),
        "SECOND": (914, 957),
        "THIRD": (997, 956),
        "FOURTH": (1080, 951),
        "MONEY_1": (1133, 78),
        "MONEY_2": (1216, 83),
    }

}




def choose_preset():
    global FIRST_X, FIRST_Y 
    global SECOND_X, SECOND_Y
    global THIRD_X, THIRD_Y
    global FOURTH_X, FOURTH_Y 
    global SEVEN_MONEY_1_X, SEVEN_MONEY_1_Y
    global SEVEN_MONEY_2_X, SEVEN_MONEY_2_Y
    global ATTACKS
    pick =input("""
    Choose preset:
    1: Ph
    2: Jo

    """)
    if pick not in PRESETS:
        print("Invalid preset, using preset 1")
        pick = "1"

    p = PRESETS[pick]

    
    FIRST_X, FIRST_Y = p["FIRST"]
    SECOND_X, SECOND_Y = p["SECOND"] 
    THIRD_X, THIRD_Y = p["THIRD"]
    FOURTH_X, FOURTH_Y = p["FOURTH"]
    SEVEN_MONEY_1_X, SEVEN_MONEY_1_Y = p["MONEY_1"]
    SEVEN_MONEY_2_X, SEVEN_MONEY_2_Y = p["MONEY_2"]

    ATTACKS = {
        1: lambda: pyautogui.leftClick(FIRST_X, FIRST_Y),
        2: lambda: pyautogui.leftClick(SECOND_X, SECOND_Y),
        3: lambda: pyautogui.leftClick(THIRD_X, THIRD_Y),
        4: lambda: pyautogui.leftClick(FOURTH_X, FOURTH_Y)
    }

    print(f"Preset {pick} loaded")



D_YAMI_FAST = 1.5   


GIT_REPO = "https://github.com/bjorkdevx/aqw_aut.git"





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


YAMI_NO_RONINI_DMG = [
    #434424 24245 
    (3, 1),
    (2, 1),
    (3, 2.2),
    (3, D_YAMI_FAST),
    (1, D_YAMI_FAST),
    (3, D_YAMI_FAST),
    (1, D_YAMI_FAST),
    (3, D_YAMI_FAST),
    (1, D_YAMI_FAST),
    (3, D_YAMI_FAST),
    (4, 1.8),
]

YAMI_NO_RONINI_SURVIVAL = [
    #2114114 
    (2, 1.9),
    (1, 1.8),
    (1, 1),
    (4, 1.8),
    (1, D_YAMI_FAST),
    (1, 1.7),
    (4, D_YAMI_FAST),
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
                pyautogui.press("T")
            time.sleep(delay)

def run_rotation_yami_no_ronin(rotation):
    print("starting rotation (move mouse to top-left to stop)")
    print("starting in 5 sec")
    time.sleep(5)
    while True:
        for attack, delay in rotation:
            print(f"Attacking with key {attack}...")
            ATTACKS[attack]()
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


def yami_no_ronin():
    pick = input("""
     Yami no Ronin
     ------------
     1: "DMG"
     2: "Survival"

     Pick an otion: """)
    options = {
        "1": lambda: run_rotation_yami_no_ronin(YAMI_NO_RONINI_DMG),
        "2": lambda: run_rotation_yami_no_ronin(YAMI_NO_RONINI_SURVIVAL)
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


    1: Arch paladin work not good
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
        sys.exit(0)
    except subprocess.CalledProcessError:
        print("Failed to pull the latest changes!")
        sys.exit(1)

       


def main():
    print("Welcome to AutoClicker Tool!")
    print("_______________________________")
    pick = input("""Pick 1 of the options\n
                1: Arch paladin
                2: Yami no Ronin
                3: Farming
                9: Get position
                0: Update
                 """)

    options = {
        "1": arch_paladin,
        "2": yami_no_ronin,
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
    choose_preset()
    main()

