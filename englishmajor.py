import sys
# from nltk import tokenize # sigh, maybe go back and get the tokenizer to work later.
from imbox import Imbox

userName = "" # Put something here.
userPassword = "" # Also probably worth putting something here. 

class Reader(object):
    """ Reads the email and stuff. """
    
    def __init__(self):
        self.inbox = Imbox('imap.gmail.com',
                           username=userName,
                           password=userPassword,
                           ssl=True)
        self.getMessages()
        
    def getMessages(self):
        self.messages = self.inbox.messages(unread=True)
        return self.messages

    def listMessageIds(self):
        """ More or less debug. """
        for message in self.messages:
            print(message[0])
            

class Evaluator(object):
    """ Evaluates whether an email is valid. Start with only basic orthography. """
    
    def checkOrthography(self, emailText, sentenceOutput = True):
        #sentences = tokenize.sent_tokenize(emailText)
        sentences = emailText.split(".")
        for sentence in sentences:
            print("Evaluating: ", sentence) # --
            doesntStartsWithCapital = ( sentence.strip()[0].capitalize() != sentence.strip()[0] )
            if sentenceOutput:
                print("Sentence doesn't start with a capital:", sentence)
            if not doesntStartsWithCapital:
                return False
        return True
                    


if __name__ == "__main__":
    r = Reader()
    
    e = Evaluator()

    for message in r.getMessages():
        messageBody = message[1].body["plain"]
        try:
            e.checkOrthography(messageBody)
        except:
            error = True
