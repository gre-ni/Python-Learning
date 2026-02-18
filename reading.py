page_num = 186


pages = 17
minutes = 30
page_total = 284

rate = pages / minutes
# to_read = page_total - page_num
to_read = int(input("How many pages do you need: "))

minutes_needed = to_read / rate
print(f"You will need {round(minutes_needed // 60)} hours and {round(minutes_needed % 60)} minutes.")
