import math
import random
from colorPrint import CLColors

def testValue(pseudo,real):
    marginOfError = .001
    error = abs(real - pseudo)
    if(error<marginOfError):
        CLColors.printSucces("The margin of error is acceptable")
    else:
        print(pseudo,real)
        print(f"{error}>{marginOfError}")
        CLColors.printError("The margin of error is not acceptable")

#Checked and tested
def simpsonIntegration(a,b,fn):
    """
    Function that numerically integrates a given function from 
    a to b.


    a,b are either int or float


    fn is a function that will be the basis for the integration.
        it must recieve only one param.
    """
    SIMPSON_N = 10000000
    h = (b-a)/SIMPSON_N
    sumEven = 0
    sumOdd = 0
    for x in range(1,SIMPSON_N):
        if(x%2==0):
            sumEven += fn(a+x*h)
        else:
            sumOdd += fn(a+x*h)
    return (fn(a) + 2*sumEven + 4*sumEven + fn(b))*h/3

#Checked and tested
def fermatTheorem(num):
    """
    Using Fermat's little Theorem, the function will determine if the number provided as param is prime or not.

    num must be an int.
    """
    for x in range(15):
        a = random.randint(1,num-1)
        v = (a**num) - a
        if(v%num != 0):
            return False
    return True

#Checked and tested
def gcd(a,b): 
    """
    Returns the greatest common between a and b.

    a,b must be integers
    """
    if(b == 0): 
        return a 
    else: 
        return gcd(b, a % b) 

class fraction : 

    def __init__(self, value):
        temp    = str(value)
        parts   = temp.split(".")
        self.denominator  = 1
        self.nominator    = int(parts[0])
        if(len(parts)>1):
            self.denominator = 10**len(parts[1])
            self.nominator  = int(parts[0]+parts[1])
        self.simplify()

    def print(self):
        print(self.nominator,"/",self.denominator)
        print(self.value)
    
    def multiply(self,otherNumber):
        if(type(otherNumber) is not fraction):
            otherNumber = fraction(otherNumber)
        self.nominator      *= otherNumber.nominator
        self.denominator    *= otherNumber.denominator
        self.simplify()

    def add(self,otherNumber):
        if(type(otherNumber) is not fraction):
            otherNumber = fraction(otherNumber)
        if(self.denominator == otherNumber.denominator):
            self.nominator += otherNumber.nominator
        else:
            self.nominator = self.nominator*otherNumber.denominator + otherNumber.nominator*self.denominator
            self.denominator *= otherNumber.denominator
        self.simplify()

    def substract(self,otherNumber):
        if(type(otherNumber) is not fraction):
            otherNumber = fraction(-otherNumber)
            self.add(otherNumber)
        else:
            self.add(-otherNumber)

    def divide(self,otherNumber):
        if(type(otherNumber) is not fraction):
            otherNumber = fraction(otherNumber)
        self.nominator      *= otherNumber.denominator
        self.denominator    *= otherNumber.nominator
        self.simplify()

    def simplify(self):
        d = gcd(self.denominator,self.nominator)
        self.nominator      = self.nominator//d
        self.denominator    = self.denominator//d
        self.value = self.value = self.nominator/self.denominator

    def testValue(self,value):
        if(self.value == value):
            CLColors.printSucces("Success")
        else:
            CLColors.printError("Failure")

def test(x):
    return math.cos(x)

integralS = simpsonIntegration(0,3*math.pi/8,test)

testValue(integralS,math.sin(3*math.pi/8))