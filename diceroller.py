import random

def roll_dice(num_dice):
    print(f"\nRolling {num_dice} dice...")
    
    for _ in range(num_dice):
        dice_value = random.randint(1, 6)
        print(f"Dice: {dice_value}")
    
def main():
    while True:
        print("\nWelcome to the Dice Rolling App!")
        print("1. Roll the dice")
        print("2. Quit")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == "1":
            num_dice = int(input("Enter the number of dice to roll: "))
            roll_dice(num_dice)
        elif choice == "2":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
