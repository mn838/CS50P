import sys
import csv

def main( ) -> None:
    file_handle_before = parse_command_line_args( )

    with open( sys.argv[2], 'w' ) as file_handle_after:
        before_file = csv.DictReader( file_handle_before )
        after_file = csv.DictWriter( file_handle_after, fieldnames = ['first', 'last', 'house'] )
        after_file.writeheader()
        for row in before_file:
            last_name, first_name = row['name'].split( ' ' )
            after_file.writerow( {'first' : f'{first_name.strip()}', 'last': f'{last_name[:-1]}', 'house': f'{row['house']}' } )

def parse_command_line_args( ) -> __file__:

    if ( len( sys.argv ) < 3 ):
        sys.exit( "Too few command-line arguments" )
    elif ( len( sys.argv )  > 3 ):
        sys.exit( "Too many command-line arguments" )

    try:
        file_handle_before = open( sys.argv[1] )
    except Exception as E:
        sys.exit( f"Could not read {sys.argv[1]}" )
    else:
        return file_handle_before

if __name__ == '__main__':
    main( )
