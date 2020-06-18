import requests
from bs4 import BeautifulSoup
import smtplib
import time


url = "https://www.amazon.com/Garmin-Fenix-Slate-Gray-Black/dp/B01N7J9APR"

headers = {
    "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}


def check_price():

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])

    if (converted_price < 338):
            send_mail()

    print(converted_price)
    print(title.strip())

    if (converted_price > 340):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('alexlyan1612@gmail.com', 'pvbwxcfxhsgumzwk')

    subject = 'price fell down!'
    body = print(
        "check amazon link: https://www.amazon.com/Garmin-Fenix-Slate-Gray-Black/dp/B01N7J9APR")

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        "alexlyan1612@gmail.com",
        msg
    )

    print("Mail has been send")
    server.quit()


while True:
    check_price()
    time.sleep(60)
