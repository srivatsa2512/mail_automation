
import smtplib
import datetime as dt
import random

email = "shreeramtheboss0@gmail.com"
pwd = "hxuplityyyjuviyp"

now = dt.datetime.now()
weekday = now.weekday()
# if weekday == 2:
with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=pwd)
        connection.sendmail(from_addr=email,
                            to_addrs="srivatsa1225.com",
                            msg=f"subject:Wednesday motivation\n\n {quote}\n "
                            )
