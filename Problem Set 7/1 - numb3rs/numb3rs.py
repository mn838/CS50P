import sys
import re

def main( ) -> None:
    print(validate(input("IPv4 Address: ")))


def validate( ip: str ) -> bool:
    pattern = re.compile( r'\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b' )
    return bool( pattern.fullmatch( ip ) )


if __name__ == "__main__":
    main()
