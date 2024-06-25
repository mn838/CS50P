import inflect
p: inflect = inflect.engine()

def main( ) -> None:
    names_list: list[str] = []
    while ( True ):
        try:
            user_input: str = input( "Name: " )
            names_list.append(user_input)
        except EOFError:
            print()
            print( f'Adieu, adieu, to {p.join(names_list)}' )
            break

if __name__ == "__main__":
    main( )
