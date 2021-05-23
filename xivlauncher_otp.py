from pyotp import TOTP
import os
import urllib.request
from datetime import datetime, timedelta
from time import sleep

FUTURE_LOOKAHEAD_SECONDS = 5

def main(args=[]):
	"""
	Read TOTP secret from the environment, generate the current login code,
	and send it to XIV Launcher via GETing its local login page.
	"""
	if 'XIV_OTP_SECRET' not in os.environ:
		print("XIV_OTP_SECRET not found as environment variable; exiting")
		return 1
	secret = os.environ['XIV_OTP_SECRET']
	if not secret:
		print("XIV_OTP_SECRET not defined; exiting")
		return 1
	auth = TOTP(secret)
	time_now = datetime.now()
	time_future = time_now + timedelta(seconds=FUTURE_LOOKAHEAD_SECONDS)
	otp_now = auth.now()
	otp_future = auth.at(time_future)
	otp = otp_now
	# Prevent auth error if the code is near to expiry, 
	# by delaying entry until the next code is valid
	if(otp_now != otp_future):
		otp = otp_future
		sleep(FUTURE_LOOKAHEAD_SECONDS)
	auth_url = "http://localhost:4646/ffxivlauncher/{}".format(otp)
	with urllib.request.urlopen(auth_url) as connect:
		pass
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

