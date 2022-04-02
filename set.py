set1 = set()


def add_cont():
    item = input('enter an item to add...')
    set1.add(item)
    item = input('enter another item to add...')
    set1.add(item)
    item = input('enter another item to add...')
    set1.add(item)
    item = input('enter another item to remove...')
    if item not in set1:
        print('not in set')
    else:
        set1.remove(item)

add_cont()
print(set1)
