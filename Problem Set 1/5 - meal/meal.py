def main():
    user_input = input("What time is it? ")
    num_minutes = convert( user_input )

    if ( num_minutes >= 7 and num_minutes <= 8 ):
        print( "breakfast time" )
    elif ( num_minutes >= 12 and num_minutes <= 13 ):
        print( "lunch time" )
    elif ( num_minutes >= 18 and num_minutes <= 19 ):
        print( "Dinner time" )

def convert(time):
    time_split = time.split( ":" )
    return float( time_split[0] ) + float( time_split[1] ) / 60

if __name__ == "__main__":
    main()
