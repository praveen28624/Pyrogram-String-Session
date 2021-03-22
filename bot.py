import time
from pyrogram import Client
import tgcrypto

select = " "

tutor = """
~ go-to my.telegram.org
~ Login using your Telegram account
~ Click on API Development Tools
~ Create a new application, by entering the required details
"""

template = """
UserBot support: @userbotindo
            
<code>STRING_SESSION</code>: <code>{}</code>

⚠️ <b>Please be carefull to pass this value to third parties</b>"""

print("""\nRunning script...""")
time.sleep(1)
print(tutor)

app_id=int(input("app id -"))
api_hash=input("api hash -")

app = Client("my_account",app_id,api_hash)


with app:
  saved_messages_template = "Pyrogram session" + template.format(app.export_session_string())
  print("\nGenerating String session...\n")           
  app.send_message("me",saved_messages_template,parse_mode="html")
  time.sleep(1) 
  print("Your STRING_SESSION value have been sent to your Telegram Saved Messages")
