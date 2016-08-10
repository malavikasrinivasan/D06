# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def nested_sum(number_list):
    list_sum = 0
    for item in number_list:
        item_type = str(type(item))  # Finding the type of the list item and storing that as a string
        if "list" in item_type:
            list_sum += nested_sum(item)  # Recursive call if the item is another list
        elif "int" in item_type or "float" in item_type:
            list_sum += item  # Add to list_sum only if the number is an integer or a float
        else:
            print("'{}' is not a type that can be added, ignoring this!".format(item))  # Ignore strings and characters
    return list_sum


def main():
    pass

if __name__ == '__main__':
    main()
