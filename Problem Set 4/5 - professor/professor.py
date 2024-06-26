import random

def main( ) -> None:
    level: int = get_level( )

    count: int = 0
    num_wrong: int = 0
    num_correct: int = 0

    while ( count < 10 ):
        num_1 = generate_integer( level )
        num_2 = generate_integer( level )

        while ( num_wrong < 3 ):
            try:
                user_input = int ( input( f'{num_1} + {num_2} = ' ) )
            except ValueError:
                print( "EEE" )
                continue

            if ( user_input != num_1 + num_2 ):
                print( "EEE" )
                num_wrong += 1
            else:
                num_correct += 1
                break

            if ( num_wrong == 3 ):
                print( f'{num_1} + {num_2} = {num_1 + num_2}' )

        num_wrong = 0
        count += 1

    print( f'Score: {num_correct}' )

def get_level( ) -> int:
    while ( True ):
        try:
            level_input: int = int( input( "Level: " ) )
            if ( level_input <= 0 or level_input > 3 ):
                continue
        except ValueError:
            continue
        else:
            return level_input


def generate_integer( level ) -> int:
    if ( level == 1 ):
        return random.randint( 0, 9 )
    elif ( level == 2 ):
        return random.randint( 10, 99 )
    elif ( level == 3 ):
        return random.randint( 100, 999 )


if __name__ == "__main__":
    main()
