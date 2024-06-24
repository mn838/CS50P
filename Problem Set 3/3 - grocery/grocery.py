def main( ) -> None:
    item_dictionary: dict[str : int] = {}

    while ( True ):
        try:
            user_input: str = input().upper()
        except EOFError:
            print()
            for items in sorted( item_dictionary ):
                print( f'{item_dictionary[items]} {items}' )
            break

        if ( user_input in item_dictionary ):
            item_dictionary[user_input] += 1
        else:
            item_dictionary[user_input] = 1

if __name__ == "__main__":
    main( )
