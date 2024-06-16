def main( ):
    user_input = input( "Input: " )
    result_string = ""

    for letter in user_input:
        if ( letter.lower() in ['a', 'e', 'i', 'o', 'u'] ):
            continue
        result_string += letter
    print( f"Output: {result_string}" )

if __name__ == "__main__":
    main( )
