def main( ):
    user_input = input( "camelCase: " )
    result_string = ""
    for letters in user_input:
        if ( letters.isupper() ):
            result_string += "_"
        result_string += f"{letters.lower()}"
    print( f"snake_case: {result_string}" )

if __name__ == "__main__":
    main( )
