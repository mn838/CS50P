def main( ):
    user_input = input( )
    string_list = user_input.split(" ")

    for i in range( len(string_list) - 1 ):
        print(string_list[i], end = "...")
    print( string_list[ len(string_list) - 1 ] )

if __name__ == "__main__":
    main( )