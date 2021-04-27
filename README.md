# xivlauncher-otp
One-click OTP entry for XIV Launcher, for use with FFXIV's recent TOTP token support.

# Usage

PyOTP must be installed to use xivlauncher-otp. The easiest way to do so is with pip:

```
pip install pyotp
```

The environment variable ```XIV_OTP_SECRET``` must also be set to the secret portion of your one time code.
This can be extracted from the text of your registration QR code. Alternitively, your authenticator application
may support exporting OTP secrets.

Once this setup is done, set XIV Launcher's "Use One-Time-Passwords" option. When the prompt "Please enter your OTP key"
appears, run xivlauncher-otp (either through the provided .bat file, or by running ```python xivlauncher-otp.py``` to enter the code automatically.

# Security

While this script may slightly weaken the two-factor login scheme by using your pc as the factor "that you have," it should still provide similar levels of
protection against simple password guessing or password reuse attacks. Storing the secret in an environment variable should be secure enough for most use cases;
still, care should be taken to avoid your environment data from being scraped.

# How it works

XIV Launcher allows entry on the OTP prompt via requesting a webpage hosted locally; xivlauncher-otp uses your TOTP secret to generate the correct 
login code and send it via this option. 
