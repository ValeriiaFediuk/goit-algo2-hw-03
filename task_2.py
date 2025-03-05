import timeit
from BTrees.OOBTree import OOBTree



def add_item_to_tree(tree, item_id, item_data):
    tree[item_id] = item_data

def add_item_to_dict(d, item_id, item_data):
    d[item_id] = item_data

def range_query_tree(tree, min_price, max_price):
    return list(tree.items(min_price, max_price))

def range_query_dict(d, min_price, max_price):
    return [(k, v) for k, v in d.items() if min_price <= v['Price'] <= max_price]

def main_task2():
    sample_data = {
        1: {'Name': 'Product A', 'Category': 'Category 1', 'Price': 10},
        2: {'Name': 'Product B', 'Category': 'Category 1', 'Price': 20},
        3: {'Name': 'Product C', 'Category': 'Category 2', 'Price': 30},
        4: {'Name': 'Product D', 'Category': 'Category 2', 'Price': 40},
        5: {'Name': 'Product E', 'Category': 'Category 3', 'Price': 50},
    }
    
    tree = OOBTree()
    d = {}
    
    for item_id, item_data in sample_data.items():
        add_item_to_tree(tree, item_id, item_data)
        add_item_to_dict(d, item_id, item_data)
    
    min_price, max_price = 15, 45
    
    tree_time = timeit.timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)
    dict_time = timeit.timeit(lambda: range_query_dict(d, min_price, max_price), number=100)
    
    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    main_task2()
