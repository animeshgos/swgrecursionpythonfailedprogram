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
    if add=='s' or add=='w' or add=='g':
        print(f"computer chose --> {comp}")
        if comp=='g':
            if add=='w':
                return True
            elif add=='s':
                return False
            elif add=='g':
                return (result(comp(),add))
        elif comp=='w':
            if add=='g':
                return False
            elif add=='s':
                return True
            elif add=='w':
                return (result(comp(),add))
        elif comp=='s':
            if add=='g':
                return True
            elif add=='w':
                return False
            elif add=='s':
                return (result(comp(),add))
    else:
        print("invalid input ")
you=input("enter snake('s') water('w') gun('g') : ")
if (result(comp(),you))==True:
    print("you won")
else:
    print("you lose")
