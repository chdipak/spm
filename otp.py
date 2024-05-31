import random
def genotp():
    lc=[chr(i) for i in range(ord('a'),ord('z')+1)]
    uc=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    otp=''
    for i in range(0,2):
        otp=otp+str(random.randint(0,9))
        otp=otp+random.choice(uc)
        otp=otp+random.choice(lc)
    return otp