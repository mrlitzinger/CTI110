    # A program to take to entered values and add them as well as mu
    # 02/03/2020
    # CTI-110 P2HW1 - Basic Math
    # Stephen Litzinger
    #
def main():
    #Ask user for firt and second number and store input as num1 and num2

    num1 = int(input('First number please?'))
    num2 = int(input('Second number please?'))

    #Add num1 and num2 and store as addsum

    addSum = num1 + num2

    #Multiply num1 and num2 and store as multiplysum
    
    multiplySum = num1 * num2
    
    #Display numbers as added and multiplied values using stored values addsum and multiplysum

    print('Your added total is', addSum)
    print('Your multiplied total is', multiplySum)
    print('The first number you entered was', num1)
    print('The second number you entered was', num2)
main()
