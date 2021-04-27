from pyotp import TOTP
import os
import urllib.request

def main(args):
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
	otp = auth.now()
	auth_url = "http://localhost:4646/ffxivlauncher/{}".format(otp)
	with urllib.request.urlopen(auth_url) as connect:
		pass
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
