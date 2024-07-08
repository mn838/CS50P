import re
import sys

def main( ) -> None:
    print(parse(input("HTML: ")))


def parse( s: str ) -> str:
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
    match = re.search( pattern, s )
    if match:
        return f'https://youtu.be/{match.group( 1 )}'
    else: return None


if __name__ == "__main__":
    main()
