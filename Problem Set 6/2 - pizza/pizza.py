import sys
import csv
import tabulate

def main( ) -> None:
    file_handle = parse_command_line_args( )

    with file_handle as f:
        reader = csv.reader(f)
        table = tabulate.tabulate(reader, headers="firstrow", tablefmt="grid")

    print( table )

def parse_command_line_args( ):

    if ( len( sys.argv ) < 2 ):
        sys.exit( "Too few command-line arguments" )
    elif ( len( sys.argv )  > 2 ):
        sys.exit( "Too many command-line arguments" )

    file_name = sys.argv[1].split( "." )
    try:
        if ( file_name[1] != "csv" ):
            sys.exit( "Not a CSV file" )
    except Exception as E:
        sys.exit( "Not a CSV file" )

    try:
        file_handle = open( sys.argv[1] )
    except Exception as E:
        sys.exit( "File does not exist" )
    else:
        return file_handle

if __name__ == "__main__":
    main( )
