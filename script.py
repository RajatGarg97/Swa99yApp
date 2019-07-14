# Importing Dependencies
import requests
from bs4 import BeautifulSoup
import smtplib
import time


def priceChecker(url, headers, quotedPrice, emailid):

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    priceToString = float(price[0:5])

    if priceToString <= quotedPrice:
        mailer(emailid)


def mailer(emailid):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Enter the password here recieved after two step verification
    server.login('swa99yapp@gmail.com', '')

    subject = 'Prices Slashed!!'
    body = 'Check the Amazon link ' + url

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('swa99yapp@gmail.com', emailid, msg)

    print('!!Email Sent Successfully!!')

    server.quit()
    exit()


def main():

    # Link of the webpage here
    url = input("Enter the URL here: ")

    # Enter your User Agent
    # To find your user agent just Google my user agent
    usrAgent = input("Enter your user agent: ")
    headers = {"User-Agent": usrAgent}

    # Your offer price
    quotedPrice = float(input("Enter Quoted Price: "))

    # Enter your email id here
    emailid = input("Enter your email id here: ")

    while(True):

        priceChecker(url, headers, quotedPrice, emailid)
        time.sleep(3600)


if __name__ == "__main__":
    main()
