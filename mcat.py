import requests
import hashlib
import time
import secrets as s
from twilio.rest import Client
from datetime import datetime

# MCAT page stuff
link = "https://apps.aamc.org/mrs/"
# locked_page = "bf88d50572d097586ef556d498654c02bd3f215e6497beaea0a2754fb17f523b" # this was the original page
# this was the landing page's hash
locked_page = "0f76fd0d47629be5871985f69244ca6234e16f4a73b217d34bae35bd5e7f3017"
new_request = requests.get(link)
hash_value = hashlib.sha256(new_request.text.encode('utf-8')).hexdigest()

# Twilio client
client = Client(s.account_sid, s.auth_token)

# logic to call ellen if the page changed
while True:
	result = "[no_change]"
	if hash_value != locked_page:
		call = client.calls.create(
			to=s.ellen,
			from_=s.twilio,
			url='http://demo.twilio.com/docs/voice.xml',
		)
		message = client.messages.create(
			to=s.patrick,
			from_=s.twilio,
			body="page changed",
		)
		result = "[page_changed, called: {}]".format(s.ellen)

	# logging
	log_location = "./mcat.log"
	f = open(log_location, "a")
	f.write("pinged {} at {} and got: {}\n".format(link, datetime.now(), result))
	f.close()
	time.sleep(10)
