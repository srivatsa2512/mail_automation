<h1><b>Email Automation with Python</b><br></h1>
<h2><b>Overview</b></h2><br>
 This project automates the process of sending emails with motivational quotes every Wednesday. It uses Python's built-in smtplib library to connect to Gmail's SMTP server, sends the emails, and randomly selects  quotes from a text file to be included in the email. The project focuses on secure and efficient email automation, with user credentials managed securely using environment variables.<br>

<h1><b>Features</b></h1><br>
<li>Automated Weekly Emails: Sends an email every Wednesday with a motivational quote.</li>
<li>Random Quote Selection: Reads a list of quotes from a text file and picks one at random.</li>
<li>Secure Email Sending: Utilizes environment variables for email credentials, ensuring that sensitive information is not hardcoded.</li>
<li>Gmail SMTP Integration: Leverages Gmail’s SMTP server to send emails programmatically.</li><br>

<h1>How it Works</h1>
<li> The script checks the current day of the week.</li>
<li>If it’s Wednesday, the script reads a quotes.txt file containing motivational quotes, selects one randomly, and sends it via email.</li>
<li>The email is sent using Gmail’s SMTP server, with the smtplib library securing the connection via TLS.</li>
<li>The sender’s email credentials are retrieved from environment variables to ensure security.</li><br>

<h1><b>Prerequisites</b></h1>
<li>Python 3.x</li>
<li>Gmail account</li>
<li>Basic understanding of Python and SMTP</li>
<li>An environment to set up environment variables</li>
