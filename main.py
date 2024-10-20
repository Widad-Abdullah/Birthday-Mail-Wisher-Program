import datetime as dt
import smtplib
import pandas
import random

# Your Email to send from
EMAIL=""
# Your Email's app password
PASSWORD=""

now=dt.datetime.now()
today=(now.month,now.day)

data=pandas.read_csv("birthdays.csv")
data_dic={(value.month,value.day):value for (index,value) in data.iterrows()}


with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as l:
    letter = l.read()

for bd in data_dic:
    if today==bd:
        final_letter = letter.replace("[NAME]", data_dic[bd]["name"].title())
        # Receivers Email
        TO_EMAIL = data_dic[bd]['email']
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,to_addrs=TO_EMAIL,msg=f"Subject:Happy Birthday!\n\n{final_letter}")


