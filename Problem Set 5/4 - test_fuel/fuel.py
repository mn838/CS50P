def main( ) -> None:
    frac: str = input( "Fraction: " )
    pct: int = convert( frac )
    print( gauge( pct ) )


def convert( fraction ) -> int:
    x, y = fraction.split( "/" )
    if int( x ) / int( y ) > 1:
        raise ValueError
    elif int( y ) == 0:
        raise ZeroDivisionError
    return int( int( x ) / int( y ) * 100 )


def gauge( percentage ) -> str:
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{ int( percentage ) }%"
        else:
            raise TypeError
    except TypeError:
        pass


if __name__ == "__main__":
    main( )
