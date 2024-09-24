**Email Automation with Python**
Overview
This project automates the process of sending emails with motivational quotes every Wednesday. It uses Python's built-in smtplib library to connect to Gmail's SMTP server, sends the emails, and randomly selects quotes from a text file to be included in the email. The project focuses on secure and efficient email automation, with user credentials managed securely using environment variables.

Features
Automated Weekly Emails: Sends an email every Wednesday with a motivational quote.
Random Quote Selection: Reads a list of quotes from a text file and picks one at random.
Secure Email Sending: Utilizes environment variables for email credentials, ensuring that sensitive information is not hardcoded.
Gmail SMTP Integration: Leverages Gmail’s SMTP server to send emails programmatically.
How it Works
The script checks the current day of the week.
If it’s Wednesday, the script reads a quotes.txt file containing motivational quotes, selects one randomly, and sends it via email.
The email is sent using Gmail’s SMTP server, with the smtplib library securing the connection via TLS.
The sender’s email credentials are retrieved from environment variables to ensure security.
Prerequisites
Python 3.x
Gmail account
Basic understanding of Python and SMTP
An environment to set up environment variables
