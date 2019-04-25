sound_on = False
sound_location = "notification.mp3"

save_logs = True
folder_directory = "logs"

message_layout = """
{author}:{timestamp}->
{message}

Image URL: {attachment_url}
""" # You can change how the message is portrayed. The variables in brackets show where things will be placed.

whitelist_mode = False # Everyone is a threat, besides an individual described below.
blacklist_mode = False # No one is a threat, besides an individual described below.

blacklist = { 
    "[user]": False
}

whitelist = {
    "[user]": True
}


auto_signin = True # Be careful with this option. If others see it, you may be f**ked!
auto_signin_credentials = {
    "email": "naam@europe.com",
    "password": "33133313"
}

# Additionally, you may want to actually load from a text file instead. Try this->
# "email": open("credentials.txt", "r").read().splitlines()[0], (place email on first line)
# "password": open("credentials.txt", "r").read().splitlines()[1]}