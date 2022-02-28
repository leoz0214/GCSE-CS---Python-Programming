#Pythagoras Theorem


def main():
    while True:
        selection = input("\nPythagoras Calculator\n1 - Find a hypotenuse\n2 - Find a missing side\n9 - Exit\n").strip()
        if selection == "1": print(f"Hypotenuse: {sum([float(input(f'Shorter side {i+1} (no units): '))**2 for i in range(2)]) ** 0.5}")
        elif selection == "2": print(f"Missing side: {(float(input('Hypotenuse (no units): '))**2 - float(input('Other shorter side (no units): '))**2) ** 0.5}")
        elif selection == "9": return "Have a good day!"
        else: input("Invalid input, enter to retry")


if __name__ == "__main__":
    print(main())
        
