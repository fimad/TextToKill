import imaplib
import email

class Inbox:
    """ Handles input collection for the game"""
    
    def __init__(self, inputTypes=["gmail"],
                gmailAddress="texttokill@gmail.com",
                gmailPassword="murdermystery"):
        self.inputTypes = inputTypes
        self.gmailAddress = gmailAddress
        self.gmailPassword = gmailPassword
        
    def poll(self):
        """ returns a list of sender, message tuples """
        rawMessages = []
        for inputType in self.inputTypes:
            rawMessages.append(self.update(inputType))
        return rawMessages
        
    def extract_body(self, payload):
        """ helper method for gmail updating """
        if isinstance(payload,str):
            return payload
        else:
            return '\n'.join([self.extract_body(part.get_payload()) for part in payload])

    def update(self, inputType):
        """ updates the message list from a given input """
        if inputType == "gmail":
            conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
            conn.login(self.gmailAddress, self.gmailPassword)
            conn.select()
            typ, data = conn.search(None, 'UNSEEN')
            #typ, data = conn.search(None, 'SEEN')
            try:
                for num in data[0].split():
                    typ, msg_data = conn.fetch(num, '(RFC822)')
                    for response_part in msg_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_string(response_part[1])
                            #subject=msg['subject']                   
                            #print(subject)
                            sender = msg['from']
                            #print(sender)
                            payload=msg.get_payload()
                            body=self.extract_body(payload)
                            #print(body)
                    typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
                    return (sender, body)
            finally:
                try:
                    conn.close()
                except:
                    pass
                conn.logout()
                
