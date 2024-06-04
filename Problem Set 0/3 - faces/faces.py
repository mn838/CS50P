def main( ):
    user_input = input( )
    split_input = user_input.split(" ")
    output_string = ""

    for words in split_input:
        if ( words == ":)" ):
            output_string += "🙂 "
        elif ( words == ":(" ):
            output_string += "🙁 "
        else:
            output_string += words + " "

    output_string = output_string[:-1]
    print( output_string )

if __name__ == "__main__":
    main( )