# You don't need to install any package... Just make sure you are using the latest version of python 3.
# You need to turn on less secure apps option towards your google account. Copy and paste the link next into your browser with the sender google account signed in.https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PP0cAqCpE4prwc-aJRg51eR9YNmwZIOlYKPINEvGMqeb5pR7MJ1_jcuf4EYm9feJZBuM2Ke3ZOhSvFEAKu9OXfcM78Zw
#And you are good to go.
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
