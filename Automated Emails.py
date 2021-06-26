import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("*Your gmail id you want to use*","*Your password*")
subject="*Write the subject to your email*"
body="*Write down the message*"
message="Subject:{}\n\n{}".format(subject,body)
listOfAddress=["*Recipient 1 *","*Recipient 2*"....]  #Add as many as you want
ob.sendmail("*Re-enter the sender email*",listOfAddress,message)
print("send successfully")
ob.quit()
