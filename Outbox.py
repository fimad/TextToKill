import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

class Outbox:
    """ Handles sending messages out from a game """
    
    def __init__(self, outputTypes=["gmail"],
                gmailAddress="texttokill@gmail.com",
                gmailPassword="murdermystery"):
        self.outputTypes = outputTypes
        self.gmailAddress = gmailAddress
        self.gmailPassword = gmailPassword

    def sendText(self, to, text, subject=""):
        """ sends a text with subject and text to a player """
        #msg = MIMEMultipart()
        msg = MIMEText(text)

        msg['From'] = self.gmailAddress
        msg['To'] = to
        msg['Subject'] = subject

        #msg.attach(MIMEText(text))

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(self.gmailAddress, self.gmailPassword)
        mailServer.sendmail(self.gmailAddress, to, msg.as_string())
        mailServer.close()
