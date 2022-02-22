class Angle : 
    def __new__(self, value):
        return value

    def sumOfTwoAngles(val1, val2):
        if (val1+val2) > 360:
            return (val1+val2) - 360
        else : 
            return val1+val2

    def substractionOfTwoAngles(val1, val2):
        if (val1 - val2) < 0:
            return 360 - (val2 - val1)
        else :
            return val1 - val2
    
    def lessThan (val1, val2):
        if (val1 > 360):
            val1 = val1 - 360
        elif (val2 > 360):
            val2 = val2 - 360
        return min(val1, val2)

    def greaterThan (val1, val2):
        if (val1 > 360):
            val1 = val1 - 360
        elif (val2 > 360):
            val2 = val2 - 360
        return max(val1, val2)
    


a = Angle(60)
b = Angle(310)
s = Angle.sumOfTwoAngles(a, b)
d = Angle.substractionOfTwoAngles(a, b)
l = Angle.lessThan(a, b)
g = Angle.greaterThan(a, b)
print(str(s) + ", " + str(d)+ ", " + str(l) + ", " + str(g))