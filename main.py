import random
import smtplib
import  datetime
import pandas
#_________________________monday quote_________________________
def mail(text):
    my_email = 'projectfestus@gmail.com'
    sender_pass = 'iyfikarcqyergruh'
    with smtplib.SMTP('smtp.gmail.com', 587) as mail:
        mail.starttls()
        mail.login(my_email, sender_pass)
        mail.sendmail(from_addr=my_email, to_addrs="festusj53@gmail.com", msg=f"Subject:Monday Motivation\n\n{text}")

with open("/data/quotes.txt", mode="r") as file:
    quote = file.readlines()


now = datetime.datetime.now()
if now.weekday() == 0:
    mail(random.choice(quote))



#________________________________birthday mail system_________________________________
def btmail(text, email, age):
    my_email = 'projectfestus@gmail.com'
    sender_pass = 'iyfikarcqyergruh'
    with smtplib.SMTP('smtp.gmail.com', 587) as mail:
        mail.starttls()
        mail.login(my_email, sender_pass)
        mail.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy {age} Birthday\n\n{text}")
def letter():
    nums = [1,2,3]
    num = random.choice(nums)
    with open(f"/data/letter_templates/letter_{num}.txt", mode="r") as file:
        lt = file.read()
    return lt

data = pandas.read_csv("data/birthdays.csv")

btday = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
data_now = (now.month,now.day)
if data_now in btday:
    person = btday[data_now]
    text = letter()
    text = text.replace("[NAME]", person["name"])
    text = text.replace("Angela", "Festus Jacob")
    btmail(text, person["email"], "+1")

