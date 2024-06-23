felipes_menu: dict[str, float] = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def main( ) -> None:
    total: int = 0

    while ( True ):
        try:
            menu_item: str = input( "Item: " ).lower()
        except EOFError:
            print()
            break

        if( menu_item in felipes_menu ):
            total += felipes_menu[menu_item]
            print( f"Total: ${total:.2f}" )
        else:
            continue

if __name__ == "__main__":
    main()
