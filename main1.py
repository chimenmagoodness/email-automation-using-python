# import smtplib
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
date_of_week = now.weekday()
# print(date_of_week)


MY_EMAIL = "1stpassabite@gmail.com"
MY_PASSWORD = "Switnex6058'"
TO_ADDRESS = "switnexxtra@gmail.com"
if date_of_week == 3:
    with open("quotes.txt", encoding='utf-8') as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDRESS,
            msg=f"Subject:Hello {TO_ADDRESS} \n\n{quote}"
    )

#
# my_email = "1stpassabite@gmail.com"
# password = "60587102"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="switnexxtra@gmail.com",
#         msg="Subject:Hello Bro \n\nThis is to check up on you mother sucker"
#     )

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# today = now.today()
# date_of_week = now.weekday()
# print(today)
#
# date_of_birth = dt.datetime(year=2000, month=6, day=12)
# print(date_of_birth)
