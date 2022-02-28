# Primary division


def main():
    while True:
        n1, n2 = [int(input(f"Enter number {i+1}: ")) for i in range(2)]
        print(f"{n1}/{n2} = {n1 // n2} remainder {n1 % n2}")
        if input("Enter to continue, q to quit: ").lower() == "q": return "Have a wonderful day!"


if __name__ == "__main__":
    print(main())
        
