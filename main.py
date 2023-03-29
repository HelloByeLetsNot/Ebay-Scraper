import requests
from bs4 import BeautifulSoup
import smtplib

# Define the URL to scrape
url = "https://www.ebay.com/sch/i.html?_nkw=laptop&_sacat=0&_sop=10&_udlo=0&_udhi=10"

# Define the email settings
email_from = "your_email@example.com"
email_to = "recipient_email@example.com"
email_subject = "Laptop Alert"
email_body = "A laptop has been listed on eBay for under $10.00 with a Buy Now option! Check it out at: " + url
email_server = "smtp.gmail.com"
email_port = 587
email_username = "your_email_username"
email_password = "your_email_password"

# Define a function to scrape eBay and send an email alert
def check_ebay():
    # Make a GET request to the eBay URL
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    # Find all listings with a Buy Now option and a price under $10.00
    listings = soup.find_all("li", {"class": "s-item", "data-format": "buyItNow", "data-price|": lambda x: float(x) < 10.00})
    # If there are any matching listings, send an email alert
    if listings:
        server = smtplib.SMTP(email_server, email_port)
        server.starttls()
        server.login(email_username, email_password)
        message = "Subject: {}\n\n{}".format(email_subject, email_body)
        server.sendmail(email_from, email_to, message)
        server.quit()

# Call the function to check eBay for matching listings
check_ebay()
