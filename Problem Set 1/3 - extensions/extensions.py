def main( ):
    user_input = input( "File name: " ).replace(" ", "").lower().split( "." )

    if ( user_input[len(user_input) - 1] == "gif" ):
        print( "image/gif" )
    elif ( user_input[len(user_input) - 1] == "jpg" or user_input[len(user_input) - 1] == "jpeg" ):
        print( "image/jpeg")
    elif ( user_input[len(user_input) - 1] == "png" ):
        print( "image/png")
    elif ( user_input[len(user_input) - 1] == "pdf" ):
        print( "application/pdf")
    elif ( user_input[len(user_input) - 1] == "txt" ):
        print( "text/plain" )
    elif ( user_input[len(user_input) - 1] == "zip" ):
        print( "application/zip" )
    else: print( "application/octet-stream")

if __name__ == "__main__":
    main( )
