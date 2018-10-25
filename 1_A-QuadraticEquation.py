# Program 1-A:  Quadratic Equation
# Andrew Dunham

def main():
    
    print('Q U A D R A T I C   E Q U A T I O N')
    print('  Calculates the roots of ax^2 + bx + c = 0 \n')
    
    a = int(input("Enter coefficient a: "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))
    print(" ")
    
    firstPart = -b/(2*a)
    secondPart = (b**2 - (4 * a * c))
                          
    if secondPart < 0:
        secondPart = abs(secondPart)
                  
        rootOne = (secondPart ** 0.5) / (2 * a)
        rootTwo = (secondPart ** 0.5) / (2 * a)
        print("  Roots are", firstPart, "+ i", "%0.2f" % rootOne, "and", firstPart, "- i", "%0.2f" % rootTwo)
                  
    else:
        rootOne = (-b + (secondPart ** 0.5)) / (2 * a)
        rootTwo = (-b - (secondPart ** 0.5)) / (2 * a)
        print("  Roots are", "%0.2f" % rootOne, "and", "%0.2f" % rootTwo)
    
if __name__ == '__main__':
    main()   
