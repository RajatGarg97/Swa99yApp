# Importing Dependencies
import requests
from bs4 import BeautifulSoup
import smtplib

def priceChecker(url, headers):

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    priceToString = float(price[0:5])

    quotedPrice = float(input("Enter Quoted Price: "))

    if priceToString <= quotedPrice:
        mailer()


def mailer():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Enter the password here recieved after two step verification
    server.login('swa99yapp@gmail.com', '') 

    subject = 'Prices Slashed!!'
    body = 'Check the Amazon link ' + url

    msg = f"Subject: {subject}\n\n{body}"

    # Enter your email id here
    emailid = input("Enter your email id here: ")     
    server.sendmail('swa99yapp@gmail.com', emailid, msg)

    print('!!Email Sent Successfully!!')

    server.quit() 

def main():

    # Copy the link of the webpage in these quotes
    url = ''

    # Copy your User Agent in the single quotes below
    # To find your user agent just Google my user agent
    headers = {
    "User-Agent": ''}
    priceChecker(url, headers)


if __name__ == "__main__":
    main()



