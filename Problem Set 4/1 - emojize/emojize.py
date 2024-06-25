import emoji

def main( ) -> None:
    user_input: str = input( "Input: " )

    print( emoji.emojize( f'Output: {user_input}', language='alias' ) )

if __name__ == "__main__":
    main( )
