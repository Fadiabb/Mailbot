import getpass
import tomli

with open('./mail-config.toml') as file:
    content = file.read()
    content_dict = tomli.loads(content)
    
imapserver = content_dict['imapserver']
bot_address = content_dict['bot_address']
TRUSTED_SENDERS = content_dict['trusted_senders']
pwd = content_dict['password']
SMTP_SERVER = content_dict['smtpserver']

if not pwd:
    pwd = getpass.getpass("Account password:")


#check_freq = 5
commands = {"hello": "xx"}
