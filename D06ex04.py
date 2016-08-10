# Imports


# Body
def find_names_with_e(filename):
    name_list = []
    names_with_e_count = 0
    names_with_e = []  
    with open(filename, "r") as f:  # Reading from the file
        roster = f.readlines()
    for person in roster:  # Separating the names from the roster and creating a separate list
        name = person.split(" ")[0]
        name_list.append(name.strip())
    with open("e_roster.txt", "w") as f:
        for name in name_list:  # Going through each name and checking if it has e
            if "e" in name:
                names_with_e_count += 1  # Incrementing count
                names_with_e.append(name)  # Adding to the list of names with e
                f.write(name + "\n")

    print("{} names had the letter e in them and they were - ".format(names_with_e_count))
    for name in names_with_e:
        print(name)

def main():
    find_names_with_e("roster.txt")

if __name__ == "__main__":
    main()
