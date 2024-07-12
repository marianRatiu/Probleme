

def mygetter(*args):
    if len(args) == 1:
        return lambda item: item[args[0]]
    else:
        return lambda item: tuple(item[arg] for arg in args)
        


g1 = mygetter(0,-1)
print(g1([10,20,30]))

