##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime as dt
import math
import random
import yagmail

NAME = "[NAME]"
MY_EMAIL = "1stpassabit@gmail.com"
MY_PASSWORD = "vbpeqwlintvnzxmu"
TO_ADDRESS = "switnexxtra@gmail.com"
# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
year = now.year
month = 6 # now.month
day = 12 # now.day
# print(f"today is {day} of {month} year {year}")
birt_year = math.floor(data_dict[0]["year"])
birt_month = math.floor(data_dict[0]["month"])
birth_day = math.floor(data_dict[0]["day"])
birth_name = data_dict[0]["name"]

if month == birt_month and day == birth_day:
    # print(birth_name)
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter_content = letter_file.read()
        # print(letter_content)
        """ 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the 
        person's actual name from birthdays.csv"""
        for name in birth_name:
            new_letter = letter_content.replace(NAME, birth_name)
            # with yagmail.SMTP(MY_EMAIL, MY_PASSWORD) as yag:
            #     yag.send(TO_ADDRESS, subject="Email Automation in python", contents=new_letter)
            # 4. Send the letter generated in step 3 to that person's email address.
            # with smtplib.SMTP("smtp.gmail.com") as connection:
            #     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            #     connection.starttls()
            #     connection.sendmail(
            #         from_addr=MY_EMAIL,
            #         to_addrs=TO_ADDRESS,
            #         msg=f"Subject:Happy Birthday\n\n{new_letter}"
            #     )
        print(new_letter)
else:
    print("Not Yet Date!")








