def main( ) -> None:
    fuel_left = get_frac( )
    if ( fuel_left <= 2 ):
        print( "E" )
    elif ( fuel_left >= 99 ):
        print( "F" )
    else:
        fuel_left = str(fuel_left)
        fuel_left = fuel_left.strip(".0")
        print(f"{fuel_left}%")

def get_frac( ) -> int:
    while ( True ):
        try:
            num, den = input( "Fraction: " ).split("/")
            int_num, int_den = int( num ), int( den )
            fuel_left = round( ( int_num / int_den ) * 100)
            if ( fuel_left > 101 or not num.isnumeric() or not den.isnumeric() ):
                continue
        except (ValueError, ZeroDivisionError):
            continue
        else:
            return fuel_left


if __name__ == "__main__":
    main( )
