import random

# Function to generate different nickname styles
def generate_nicknames(name1, name2):
    nicknames = []

    # Core Style
    nicknames.append(name1[:2] + name2[-2:])  # Example: Am + ya = Amya

    # Enhancements
    nicknames.append(name1[:len(name1)//2] + name2[len(name2)//2:])  # First half + second half
    nicknames.append("".join(random.choice(name1 + name2) for _ in range(4)))  # Random chars
    nicknames.append(name1[:3] + name2[:3])  # First 3 letters of both
    nicknames.append(name2[::-1] + name1[::-1])  # Reversed combo

    return nicknames

def nickname_generator():
    history = []  # To store generated nicknames
    while True:
        print("\n===== Auto Nickname Combiner =====")
        name1 = input("Enter first name: ").strip().capitalize()
        name2 = input("Enter second name: ").strip().capitalize()

        if not name1 or not name2:
            print("❌ Both names are required. Try again.")
            continue

        nicknames = generate_nicknames(name1, name2)

        print("\n✨ Generated Nicknames:")
        for i, n in enumerate(nicknames, 1):
            print(f"{i}. {n}")
            history.append(n)

        # Ask if user wants another nickname set
        choice = input("\nDo you want to try again with new names? (y/n): ").strip().lower()
        if choice != 'y':
            break

    # Show history before exit
    print("\n📜 Nickname History (this session):")
    for i, n in enumerate(history, 1):
        print(f"{i}. {n}")

    print("\n👋 Thanks for using Auto Nickname Combiner!")

# Run the program
if __name__ == "__main__":
    nickname_generator()