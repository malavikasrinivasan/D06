# Imports
from random import randint

# Body


def random_numbers_to_file():
    with open("random_numbers.txt", "w") as f:  # Create/Open file in write
        for i in range(0, 10):
            f.write(str(randint(1, 1000)) + "\n")


def main():
    random_numbers_to_file()


if __name__ == "__main__":
    main()
