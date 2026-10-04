"""
Create a shopping list containing at least four items.
[ ] Print the original shopping list.
[ ] Use append() to add one item.
[ ] Use extend() to add two items.
[ ] Use remove() to remove a specific item.
[ ] Use pop() to remove the final item and capture what was removed.
[ ] Create a reversed COPY without modifying the current original.
[ ] Reverse the ORIGINAL list in place using reverse().
[ ] Print the results before and after each operation.
"""




def print_original_shopping_list(list_input):
    print(list_input)

def function_collection_shopping_list(list_input):
    list_input.append("Water")
    print(list_input)
    list_input.extend(["Soda", "Lemon"])
    print(list_input)
    list_input.remove("Soda")
    print(list_input)
    removed = list_input.pop()
    print(removed)

def reverse_copying_collection_shopping_list(list_input):
    reversed_copy = list_input[::-1]
    print(reversed_copy)
    list_input.reverse()
    print(list_input)


shopping_list = ["Bread", "Milk", "Nuts", "AlphabettiSoup"]

if __name__ == "__main__":
    print_original_shopping_list(shopping_list)
    function_collection_shopping_list(shopping_list)
    reverse_copying_collection_shopping_list(shopping_list)