import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='xivlauncher-otp',
     version='0.1',
     author="ForOhForError",
     description="XIV Launcher OTP Entry",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     install_requires=['pyotp'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
     py_modules=['xivlauncher_otp'],
     entry_points={'console_scripts': ['xivlauncher_otp=xivlauncher_otp:main']},
 )
