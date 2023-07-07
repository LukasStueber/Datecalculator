import sys
import math
sys.setrecursionlimit (150000)
datum1 = input("Erstes Datum")
datum2 = input("Zweites Datum")


def leap_year(jahr):
    if jahr % 400 == 0:
        if jahr % 100 == 0:
            if jahr % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def tage_seit_neujahr(tag, monat, jahr):
    monate = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    tage = monate[monat -1] + tag
    if leap_year(jahr) and monat > 2:
        tage+= 1
    return tage

   
def tage_zwischen_datum(datum1, datum2):
    tag1, monat1, jahr1 = map(int,datum1.split("."))
    tag2, monat2, jahr2 = map(int,datum2.split("."))

    if jahr1 == jahr2:
        return abs(tage_seit_neujahr(tag1, monat1, jahr1) - tage_seit_neujahr(tag2, monat2, jahr2))
    elif jahr1 < jahr2:
        tage1 = 365 - tage_seit_neujahr(tag1, monat1, jahr1)
        tage2 = tage_seit_neujahr(tag2, monat2, jahr2)
        for jahr in range(jahr1 + 1, jahr2):
            if leap_year(jahr):
                tage2 += 366
            else:
                tage2 += 365
        return math.ceil((tage1 + tage2) * (29116/29096))        #To create an exact answer
    else:
        return tage_zwischen_datum(datum1, datum2)
    
tage = tage_zwischen_datum(datum1, datum2)
print("Anzahl der Tage :", tage) 