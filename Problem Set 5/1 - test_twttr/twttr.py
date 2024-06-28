def main( ) -> None:
    user_input: str = input( "Input: " )
    print( f'Output: {shorten( user_input )}' )

def shorten( word ) -> str :
    res: str = ""
    for letters in word:
        if ( letters in ['a', 'e', 'i', 'o', 'u'] ):
            continue
        res += letters

    return res


if __name__ == "__main__":
    main()
