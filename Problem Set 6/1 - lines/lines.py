import sys

def main( ) -> None:
    file_handle = parse_command_line_args( )

    count = 0

    for lines in file_handle.readlines( ):
        lines = lines.strip( )
        if lines.startswith( "#" ) or lines == "" :
            continue

        count += 1
    print( count )

def parse_command_line_args( ):

    if ( len( sys.argv ) < 2 ):
        sys.exit( "Too few command-line arguments" )
    elif ( len( sys.argv )  > 2 ):
        sys.exit( "Too many command-line arguments" )

    file_name = sys.argv[1].split( "." )
    try:
        if ( file_name[1] != "py" ):
            sys.exit( "Not a Python file" )
    except Exception as E:
        sys.exit( "Not a Python file" )

    try:
        file_handle = open( sys.argv[1] )
    except Exception as E:
        sys.exit( "File does not exist" )
    else:
        return file_handle

if __name__ == "__main__":
    main( )
