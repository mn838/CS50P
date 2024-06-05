def main( ):
    user_input = input( "Greeting: " ).lower().strip()
    if ( user_input[:5] == "hello" ):
        print( "$0" )
    elif ( user_input[:1] == "h" ):
        print( "$20" )
    else: print( "$100" )

if __name__ == "__main__":
    main( )
