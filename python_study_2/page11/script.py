# Create a dictionary with keys and values, and assign it to the items variable
items = {"apple":2, "banana":4, "orange":6}
# Create a for loop that gets the keys of items
for item_name in items:
    # Print '--------------------------------------------------'
    print("---------------------------------------------")
    # Print 'Each ___ costs ___ dollars'
    print("Each " + item_name + " costs " + str(items[item_name]) + " dollars" )