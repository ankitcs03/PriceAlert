from celery.task.schedules import crontab
from celery.decorators import periodic_task

from pricecheck.models import Alert
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def pCompare(alert):
	if alert.url :
		uClient = uReq(alert.url)
		page_html = uClient.read()
		uClient.close()

		page_soup =  soup(page_html, "html.parser")
		product_name = page_soup.find("a", {"class","_2cLu-l"})
		if product_name:
			product_name = product_name.get('title')
		else:
			product_name = page_soup.find("div",{"class","_3wU53n"}).text

		if product_name == alert.product_name :
			price = page_soup.find("div", {"class","_1vC4OE"})
			price = price.text[1:] 
			if int(price.replace(',','')) <= int(alert.alert_price) :
				return "True"
	else:
		return "False"

def sendEmail(alert):
	UserName = "dummy"
	Password = "dummy"
	s = smtplib.SMTP('smtp.live.com', 587)
	s.ehlo()
	s.starttls()
	s.login(UserName, Password)
	
	msg = MIMEMultipart()
	msg['From'] = 'ankitcs03@hotmail.com'
	msg['To'] = 'ankit.cs.03@gmail.com'
	msg['Subject'] = "Alert Messgae !!! "
	emailText = "Price has been drop to (or below) %s for product %s" %( str(alert.alert_price) , alert.item )
	emailBody = MIMEText(emailText, 'plain')
	msg.attach(emailBody)
	s.sendmail("ankitcs03@hotmail.com", "ankit.cs.03@gmail.com", msg.as_string())
	
	print("Alert Email send successfully!!")
	print()
	s.quit()


#class priceCompare():
def main():
	alerts = Alert.objects.all()
	for alert in alerts:
		ret = pCompare(alert)
		if ret == "True" :
			sendEmail(alert)


# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
main()
