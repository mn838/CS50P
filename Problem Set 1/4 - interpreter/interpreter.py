def main( ):
    user_input = input("Expression: ").split()
    num1 = float( user_input[0] )
    num2 = float( user_input[2] )
    operator = user_input[1]
    if ( operator == "+" ):
        print( num1 + num2 )
    elif ( operator == "-" ):
        print( num1 - num2 )
    elif ( operator == "*" ):
        print( num1 * num2 )
    elif ( operator == "/" ):
        print( num1 / num2 )

if __name__ == "__main__":
    main( )
