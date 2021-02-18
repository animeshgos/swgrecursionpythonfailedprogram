import random
def comp():
    r=random.randint(1,3)
    if r==1:
        return 's'
    elif r==2:
        return 'w'
    else:
        return 'g'
def result(comp,add):
    print(comp)
    if comp=='g':
        if add=='w':
            return True
        elif add=='s':
            return False
        else:
            return (result(comp(),add))
    elif comp=='w':
        if add=='g':
            return False
        elif add=='s':
            return True
        else:
            return (result(comp(),add))
    elif comp=='s':
        if add=='g':
            return False
        elif add=='w':
            return True
        else:
            return (result(comp(),add))

you=input("enter snake('s') water('w') gun('g') : ")
print(result(comp(),you))