def main( ) -> None:
    plate: str = input( "Plate: " )
    if is_valid( plate ):
        print( "Valid" )
    else:
        print( "Invalid" )

def is_valid( s ) -> bool:
    if ( not s.isalnum( ) ):
        return False
    elif ( len( s ) < 2 or len( s ) > 6 ):
        return False
    elif ( s[0].isdigit( ) or s[1].isdigit( ) ):
        return False
    elif ( len( s ) > 2 and s[2] == "0" ):
        return False

    state: int = 0
    for i, c in enumerate( s ):
        if ( state == 0 ):
            if ( c.isdecimal( ) ):
                return False
            if ( i == 1 ):
                state = 1

        elif ( state == 1 ):
            if ( c.isdigit( ) ):
                if ( c == "0" and i < 3 ):
                    return False
                state = 2

        elif ( state == 2 ):
            if ( c.isalpha( ) ):
                return False

    return True

if __name__ == "__main__":
    main()
