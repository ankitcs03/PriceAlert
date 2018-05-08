# PriceAlert
------------------------------------------------------------------------------------------
## Task

This is a Python script that accepts a product name as arguments and then shows its current price fetched from Amazon & Flipkart and notify when its price drops to or below the defined price.

The product name can be both an exact product name (Intel i7 6700k) or a generic name (Bluetooth headphones). In case of a generic name display the first search result with its price.

After displaying the price, provide an option to set a price drop alert. On selecting to set a price drop alert, ask for a price and email id and set a notification.

If a notification is set, monitor the price of the product and alert the user by email when the price drops to or below the defined price.

## Items Implemented
- Currently it is working fine to extract the records from Flipkart and set a price alert on that.


## Items left to implemente
- Unable to extract data from Amazon

  **Reason:** It's because Amazon doesn't allow automated access to their data, so they're rejecting your request because it didn't come  from a proper browser. So to implemented these functionality we need an AWS API to get the price list of product from Amazon.
      Currently looking for a free AWS API that can suite this project requirement.

## Things can be improved
- Needs to implement error handling. 
- Needs to improve GUI (HTML & CSS)
 
## Things to take care while setting up this application
- Python Version    3.6.4
- django.VERSION   (1, 9, 4, 'final', 0)
- BeautifulSoup required for scraping 
- django-celery module required to run priceCompare.py in a regular interval to check if price has been dropped.
- [ If you need help to setup django-celery, please follow this link ](https://chase-seibert.github.io/blog/2010/07/09/djangocelery-quickstart-or-how-i-learned-to-stop-using-cron-and-love-celery.html)
- Needs to update priceCompare.py to set Email_ID and password of email sender's account. Currently it is set as "dummy". 
- Currently mail server name is set for hotmail/outlook. Update it if you are using Gmail or any ohter mail server
>	UserName = "**dummy**"

>	Password = "**dummy**"

> s = smtplib.SMTP('**smtp.live.com**', 587)
   
