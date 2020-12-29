from datetime import datetime
import pandas
import random

# Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Get the birthdays of persons that we have in our birthday list
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# If today's date matches a person's birthday, take one of our birthday letter templates and send it to that person(s)
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])