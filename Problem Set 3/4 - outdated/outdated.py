months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main( ) -> None:
    while ( True ):
        try:
            date: str = input("Date: ").strip()
            if ( '/' in date ):
                month, day, year = date.split("/")
                month, day, year  = int(month), int(day), int(year)
                if ( month <= 12 and day <= 31 ):
                    print(f"{year}-{month:02d}-{day:02d}")
                    break
            else:
                month, day, year = date.split(" ")
                if ( month in months_list and ',' in day ):
                    month: int = months_list.index(month) + 1
                    day: int = int( day.replace(",", "") )
                    if ( month <= 12 and day <= 31 ):
                        print(f"{year}-{month:02d}-{day:02d}")
                        break
        except:
            pass


if __name__ == "__main__":
    main( )
