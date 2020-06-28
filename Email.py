import yagmail

sender_email = 'rpalmer1502@gmail.com'
receiver_email = 'jchou0812@gmail.com'
subject = "Check THIS out"
sender_password = input(f'Please, enter the password for {sender_email}:\n')
yag = yagmail.SMTP(user=sender_email, password=sender_password)
contents = [
  "blhablhablahbalhbalbhalbhabhblahblhba",
  "As you can see, we can send a list of strings,",
  "being this our third one",
]
yag.send(receiver_email, subject, contents)
