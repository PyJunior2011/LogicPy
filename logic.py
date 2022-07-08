def trigger(value):
    v1 = value
    if v1 <= 0:
        v1 = 0
    return v1

def vrs(value):
    v2 = value
    if v2 > 0:
        v2 * -1
    elif v2 < 0:
        abs(v2)
    return v2

def sqrt(value):
    v3 = value
    if v3 < 0:
        v3=abs(v3)
    for i1 in range(1, v3, 1):
        j = v3 / i1
        if j == i1:
            v3 = i1
            return v3
            break

def nor(conditionA, conditionB):
    CA1 = conditionA
    CB1 = conditionB
    if  CA1 == False or CB1 == False:
        return True
    elif  CA1 == True or CB1 == True:
        return False

def nand(conditionA, conditionB):
    CA2 = conditionA
    CB2 = conditionB
    if CA2 == True and CB2 == True:
        return False
    elif CA2 == False and CB2 == False:
        return True

def xor(conditionA, conditionB):
    CA3 = conditionA
    CB3 = conditionB
    if CA3 != CB3:
        return True
    else:
        return False

def xorn(conditionA, conditionB):
    CA4 = conditionA
    CB4 = conditionB
    if CA4 != CB4:
        return False
    else:
        return True
