def hello():
    print("Hello, user!")

def pack(item1, item2, item3):
    result = [item1, item2, item3]

    return result

def eat_lunch(lunchbox):
    if len(lunchbox) == 0:
        print('My lunchbox is empty')
    else:
        print('First I eat ' + lunchbox[0])
        for i in range(1, len(lunchbox)):
            food = lunchbox[i]
            print('Next I eat ' + food)


hello()
print(pack(1, 'a', 'b'))
eat_lunch(['breakfast', 'lunch', 'dinner'])