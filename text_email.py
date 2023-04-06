import random
import smtplib
import ssl
import pandas
import datetime as dt
import math


NAME = "[NAME]"
MY_EMAIL = "1stpassabite@gmail.com"
MY_PASSWORD = "ntilkwogugibwqko"
EMAIL_TO = "sweetnessgoodness10@gmail.com"
SMTP_SEVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_CONTEXT = ssl.create_default_context()


now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv("birthdays.csv")
new_data = data.to_dict(orient="records")

birth_day = math.floor(new_data[0]["day"])
birth_month = math.floor(new_data[0]["month"])
birth_name = new_data[0]["name"]

if birth_month == month and birth_day == day:

    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as message_files:
        message = message_files.read()
        new_message = message.replace(NAME, birth_name)
        try:
            print("connecting to server.....")
            with smtplib.SMTP(SMTP_SEVER, SMTP_PORT) as connection:
                connection.starttls(context=EMAIL_CONTEXT)
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                print("Connected to Server :-)")

                print()
                print(f"Sending Email to - {EMAIL_TO}")
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=EMAIL_TO,
                    msg=f"Subject:Email Automation with python\n\n{new_message}"
                )
                print(f"Email Successfully Sent to - {EMAIL_TO}")

        except Exception as e:
            print(e)
else:
    print(f"Not yet {month} and {day}. but still checking!")