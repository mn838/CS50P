def main( ):
    cents = 50
    while ( cents > 0 ):
        print( f"Amount Due: {cents}" )
        user_input = int( input( "Insert Coin: " ) )
        if ( user_input in [5, 10, 25] ):
            cents -= user_input
    print( f"Change Owed: {abs(cents)}" )

if __name__ == "__main__":
    main( )
