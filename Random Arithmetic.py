# Random Arithmetic
from random import randint


def main():
    while True:
        n1, n2 = [randint(1, 100) for i in range(2)]
        if input(f"{n1} + {n2} = {n1 + n2}\n{n1} - {n2} = {n1 - n2}\n{n1} x {n2} = {n1 * n2}\n{n1} / {n2} = {round(n1 / n2, 8)}\nEnter to go again or q to quit: ").lower() == "q":
            return "Have a good day!"


if __name__ == "__main__":
    print(main())
    
