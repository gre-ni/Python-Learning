from datetime import date, timedelta
import inflect
import sys
import re


def main():
    date_input = input("Date of Birth: ")
    p = inflect.engine()

    # Collecting Input
    try:
        date_past = get_date(parse_date_format(date_input))

    except (ValueError, TypeError):
        print("Invalid date")
        sys.exit(1)

    date_today = date.today()

    duration_seconds = (date_today - date_past).total_seconds()
    duration_minutes = round(duration_seconds / 60)

    duration_in_words = p.number_to_words(duration_minutes)
    print(f"{duration_in_words.capitalize().replace("and ", "")} minutes")

# Output format: Fifteen million, seven hundred seventy-eight thousand eighty minutes

def parse_date_format(date: str) -> tuple[int, int, int]:
    if match := re.search(r"^(?:([1-2]\d\d\d)-(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[0-1]))$", date):
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        return year,month,day

    else:
        raise ValueError


def get_date(date_parts: tuple[int, int, int]) -> date:
    try:
        date_given = date(*date_parts)
        if date_given > date.today():
            raise ValueError
        else:
            return date_given

    except (ValueError, TypeError):
        raise


if __name__ == "__main__":
    main()
