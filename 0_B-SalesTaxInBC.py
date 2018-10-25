# Program 0-B: Sales tax in BC
# Andrew Dunham

def main():

    #A very simple program that shows basic math functions and print statements in python. 
    
    purchaseAmount = 47.51
    PST = purchaseAmount * 0.07
    GST = purchaseAmount * 0.05

    print("Sales tax in BC")
    print("Purchase amount:", purchaseAmount )
    print("PST: ", PST)
    print("GST: ", GST)

if __name__ == '__main__':
    main()
