from email.message import EmailMessage 
import smtplib 


def credentials():
    id="" #KEEP YOUR MAIL ID
    pwd="" #KEEP YOUR PASSWORD
    
    return(id,pwd)

try:
    smtpObj=smtplib.SMTP('smtp.gmail.com',587) 
    smtpObj.ehlo() 
    smtpObj.starttls()

    #credentials is a function to return a id and password
    #Calling the function
    id=credentials()[0]
    pwd=credentials()[1]
    smtpObj.login(id,pwd)
    
    msg=EmailMessage() #Create mail message object
    msg['From']="" #sender id or name
    msg['TO']="" #receiver mail id
    msg['Subject']="Testing" #subject 
    msg.set_content("Hi How are you?") #content of msg
    smtpObj.send_message(msg)
    smtpObj.quit()

except Exception as err:
    print(err)
