import requests
import sys
import json

def main( ) -> None:
    if ( len( sys.argv ) < 2 ):
        print( "Missing Command-Line Argument" )
        sys.exit( 1 )

    try:
        amount_btc: float = float( sys.argv[1] )
    except ValueError:
        print( "Command-line argument is not a number" )

    bitcoin_price: float = request_bitcoin_price( )

    print( f'${amount_btc * bitcoin_price:,.4f}' )

def request_bitcoin_price( ) -> int:
    try:
        r = requests.get( 'https://api.coindesk.com/v1/bpi/currentprice.json' )
    except requests.RequestException:
        sys.exit( 1 )

    json_doc: json = json.loads( r.text )
    return json_doc['bpi']['USD']['rate_float']

if __name__ == "__main__":
    main( )
