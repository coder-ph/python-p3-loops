# def square_items(item_list):
#     squared_items = []
#     for item in item_list:
#         squared_items.append(item)
#         return squared_items

# square_items([-1,-2,-3])

def squared_items(int_list):
    squared_list = [item* item for item in int_list]
    print(squared_list)
    
squared_items([-1,-2,-3])