from pyotp import TOTP
import os
import urllib.request
from datetime import datetime, timedelta
from time import sleep
import sys
import argparse

FUTURE_LOOKAHEAD_SECONDS = 5
XIV_OTP_SECRET_VAR = "XIV_OTP_SECRET"

def copy_to_clip(code:str):
	import pyperclip
	pyperclip.copy(code)

def get_otp_secret_from_env():
	if XIV_OTP_SECRET_VAR not in os.environ:
		return ""
	else:
		return os.getenv(XIV_OTP_SECRET_VAR)

def main():
	"""
	Read TOTP secret from the environment, generate the current login code,
	and send it to XIV Launcher via GETing its local login page.
	"""
	parser = argparse.ArgumentParser(
		prog='xivlauncher-otp',
		description='Automatically sends an OTP to XIVLauncher'
	)
	parser.add_argument('-s', '--secret', type=str, default=get_otp_secret_from_env(), help=f'Your TOTP Secret. If not given, uses {XIV_OTP_SECRET_VAR} instead.')
	parser.add_argument('-C', '--copy-to-clip', action='store_true', help='If set, also attempts to copy the OTP to the clipboard')
	parsed = parser.parse_args()

	secret = parsed.secret
	if not secret:
		print(f"TOTP Secret not supplied; either pass using `--secret YOURSECRETHERE` or setting the env var {XIV_OTP_SECRET_VAR}")
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

	if parsed.copy_to_clip:
		copy_to_clip(otp)

	auth_url = "http://localhost:4646/ffxivlauncher/{}".format(otp)
	with urllib.request.urlopen(auth_url) as connect:
		pass
	
	return 0

if __name__ == '__main__':
	sys.exit(main())

