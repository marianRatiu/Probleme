

def mygetter(*args):
    if len(args) == 1:

        def single_item_getter(item):
            return item[args[0]]
        return single_item_getter
    else:
        def multiple_item_getter(item):
            return tuple(item[arg]for arg in args)
        return multiple_item_getter



g1 = mygetter(0,-1)
print(g1([10,20,30]))

