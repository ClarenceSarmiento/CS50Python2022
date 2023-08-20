grocery = {}

while True:
    try:
        item = input().upper().strip()
        if item in grocery:
            # if item is in the grocery, then update its quantity
            grocery[item] += 1
        else:
            # else add the item in the grocery
            grocery[item] = 1
    except KeyError:
        pass
    except EOFError:
        sorted_grocery = dict(sorted(grocery.items()))
        for item in sorted_grocery:
            print(sorted_grocery[item], item, sep=" ")
        break
