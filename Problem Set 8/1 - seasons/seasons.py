from datetime import date
import inflect
import sys

def main() -> None:
    try:
        user_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit('Invalid date')

    num_minutes = get_total_minutes(user_date, date.today())
    p = inflect.engine()

    print(f"{p.number_to_words(num_minutes, andword='').capitalize()} {p.plural('minute', num_minutes)}")



def get_total_minutes(start_date: date, end_date: date) -> int:
    return (end_date - start_date).days * 24 * 60

if __name__ == '__main__':
    main()
