from matplotlib import pyplot as plt
from math import factorial
import numpy as np
import re
FUNCTIONS = r"(sin|cos|tan|sec|csc|cot|log|ln|e)"



expr=input("Enter a function \n eg: sin(x), x**2, e**(x+1), (2x+1)**1/2 ...  \n f(x): ")

def convert_to_numpy(expr):
    expr = expr.replace("sin", "np.sin")
    expr = expr.replace("cos", "np.cos")
    expr = expr.replace("tan", "np.tan")
    expr = expr.replace("ln", "np.log")   
    expr = expr.replace("exp",   "np.exp")
    expr = expr.replace("^", "**") 
    return expr        

def fix_functions(expr):
    expr=expr.lower()
    expr=expr.replace(" ","")


    #change(3x=>3*x)

    expr=re.sub(r"(\d)(x)",r"\1*\2",expr)

    #change(x3=>x**3)

    expr=re.sub(r"(x)(\d)",r"\1**\2",expr)

    #change (ex=>e**x)

    expr=re.sub(r"(e)(\d)",r"\1**\2",expr)

    #change FUNCTIONS to proper form(sinx=>sin(x))

    expr=re.sub(rf"{FUNCTIONS}x",r"\1(x)",expr)
    expr=convert_to_numpy(expr)
    return expr

    
def make_func(expr):
    expr=fix_functions(expr)
    def f(x):
        return eval(expr,{"np":np,"x":x})
    return f



def derivitive(f,a,h=1e-5,order=1):
    if order==0:
        return f(a)
    elif order==1:
        return (f(a+h)-f(a-h))/(2*h)
    else:
        def nth_derivative(f,a,n):
            if n==1:
                return (f(a+h)-f(a-h))/(2*h)
            else:
                return (nth_derivative(f,a+h,n-1)-nth_derivative(f,a-h,n-1))/(2*h)
        return nth_derivative(f,a,order)
         
    

def taylor_polynominal(func,a,n):
   
   def P(x):
       result=0
       for k in range(n+1):
           term=derivitive(func,a,order=k)/factorial(k)*(x-a)**k
           result+=term
       return result
   return P



        
func=make_func(expr)# the inputed function

n=3 #order of the taylor function (degree it covers)

a=0 # a=0 because we are calculating the Maclaurin series

x=np.linspace(-2,2,1000) # the domain covered by both

y=func(x) # returns the y at the domain x

P5=taylor_polynominal(func,a,n) # the tyler polynomial

taylor_y=[P5(i) for i in x] #returns taylors y at the given domain


#ploting the Taylor and normal equation Together
plt.plot(x,taylor_y, label=f"order {n} Taylor-sereis",color="green")
plt.plot(x,y, label=fix_functions(expr),color="red",linewidth=0.5)
plt.axhline(0,color="Black")
plt.axvline(0,color="Black")
plt.grid(True)
plt.legend()
plt.show()
    














