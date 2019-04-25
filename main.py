#!/usr/bin/python3

import discord

#Standard library/os operations
import os

import datetime
import sys

from functions import *

#Audio
import pygame

exec(open("conf.py").read()) # Lazy way of implementing configuration files.
# Also didn't close my reading. Bad practice, but who cares?


if (not os.path.exists("logs/")):
    os.mkdir("logs/")

if (whitelist_mode == True and blacklist_mode == True):
    print("You cannot have whitelist mode and blacklist mode enabled at the same time. Change your configuration file. Exiting...")
    exit(1)

if (sound_on):
    pygame.init() # initalize pygame
    pygame.mixer.init()
    pygame.mixer.music.load(sound_location) # load the configuration file



if (len(sys.argv) < 2 and not auto_signin):
    print("Incorrect number of arguments.")
    helpmenu()
    exit(1)

if (len(sys.argv) > 1 and sys.argv[1] == "--sound-test"): # Test your sound?
    #print("From {location}".format(location = sound_location))
    pygame.mixer.music.play()
    pygame.event.wait()
    exit(1)



client = discord.Client()

@client.event
async def on_ready(): # Intro message
    print("Logged into {user}".format(user = client.user.name))
    print("Detecting all messages that are deleted!")


@client.event
async def on_message_delete(message): # Event invoked whenever ANY message is deleted from anyone of your contacts. 
    if (whitelist_mode): # Assume everyone but this person is a threat.
        if (whitelist[str(message.author)] == True):
            return
    
    if (blacklist_mode): # Assume everyone is docile besides this person
        if (not blacklist[str(message.author)] == True):
            return
    
    if (sound_on): # Did you enable sound? You should.
        pygame.mixer.music.play()

    if (not os.path.exists(folder_directory + "/" + str(message.author) + "/")): # Create a neat portfolio of the person you are monitoring
        os.mkdir("{folder_directory}/{user}/".format(user = str(message.author), folder_directory = folder_directory))

    proxy_url = "" # Make it sub-global

    
    for attachment in message.attachments: # Loop through the assortment of attachments (only really one, anyway)
        proxy_url = attachment["proxy_url"] # Obtain the proxy_url, which doesn't get deleted when the actual message gets deleted, opposed to the regular url (denoted by cdn)
        print("Attachment Url: {image}".format(image = proxy_url)) 

    log_format = message_layout.format(
        message = message.content, 
        author = str(message.author), 
        timestamp = str(message.timestamp),
        attachment_url = proxy_url
    )

    print(log_format)
    
    if (save_logs):
        fp = open(folder_directory + "/" + str(message.author) + "/" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log", "a") # Open file pointer to file with the author and the date in their portfolio.
        fp.write(log_format)
        fp.close()


# Wrap up
if (auto_signin):
    client.run(auto_signin_credentials["email"], auto_signin_credentials["password"])
else:
    client.run(sys.argv[1], sys.argv[2]) # Utilize the arguments as they shall be used.


# x lines!
