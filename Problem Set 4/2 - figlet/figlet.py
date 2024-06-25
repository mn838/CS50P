from pyfiglet import Figlet
import sys
import random

def main( ) -> None:
    figlet: Figlet = Figlet()
    list_of_fonts: list[str] = figlet.getFonts( )
    try:
        if ( len( sys.argv ) == 3 and ( sys.argv[1] == '-f' or sys.argv[1] == '--font' ) and sys.argv[2] in list_of_fonts ):
            user_input: str = input( "Input: " )
            figlet.setFont( font = sys.argv[2] )
        elif ( len( sys.argv ) == 1 ):
            user_input: str = input( "Input: " )
            figlet.setFont( font = random.choice( list_of_fonts ) )
        else:
            sys.exit( "Invalid Usage" )
        print( figlet.renderText( user_input ) )
    except IndexError:
        sys.exit( "Invalid Usage" )


if __name__ == "__main__":
    main( )
