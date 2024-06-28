def main( ) -> None:
    user_input: str = input( "Greeting: " ).lower().strip()
    print( value( user_input ) )

def value( greeting: str ) -> int:
    greeting = greeting.lower().strip()
    if ( greeting[:5] == "hello" ):
        return 0
    elif ( greeting[:1] == "h" ):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main( )
