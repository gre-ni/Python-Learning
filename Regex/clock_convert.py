import re
import sys


def main():
    print(convert(input("Hours: ")))

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM

def convert(s):
    if match := re.fullmatch(r"(?:(\d[0-2]?):?([0-5]\d)?) ?([AP]M) to (?:(\d[0-2]?):?([0-5]\d)?) ([AP]M)", s):

        time_from_hours = match.group(1)
        time_from_mins = match.group(2) or "00"
        time_from_day = match.group(3)
        
        time_to_hours = match.group(4)
        time_to_mins = match.group(5) or "00"
        time_to_day = match.group(6)
        
        if time_from_day == "PM":
            time_from_hours = int(time_from_hours) + 12
        
        if time_to_day == "PM":
            time_to_hours = int(time_to_hours) + 12
        
        if time_from_day == "AM" and time_from_hours == "12":
            time_from_hours = "00"
        
        if time_to_day == "AM" and time_to_hours == "12":
            time_to_hours = "00" 
        
        return f"{time_from_hours}:{time_from_mins} to {time_to_hours}:{time_to_mins}"
            
    else:
        raise ValueError


if __name__ == "__main__":
    main()