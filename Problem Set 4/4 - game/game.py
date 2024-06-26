import random

def get_level( ) -> int:
    while ( True ):
        try:
            level_input: int = int( input( "Level: " ) )
            if ( level_input <= 0 ):
                continue
        except ValueError:
            continue
        else:
            return level_input

def main( ) -> None:
    level: int = get_level( )

    rand_number: int = random.randint( 1, level )

    while ( True ):
        try:
            guess_input: int = int( input( "Guess: " ) )
            if ( guess_input < 0 ):
                continue
        except ValueError:
            continue

        if ( guess_input == rand_number ):
            print( "Just right!" )
            break
        elif ( guess_input > rand_number ):
            print( 'Too large!' )
        elif ( guess_input < rand_number ):
            print( 'Too small!' )

if __name__ == "__main__":
    main( )
