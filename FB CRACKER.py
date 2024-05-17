def banner():
  class colors:
    BIBlue="\[\033[1;94m\]"  
    BIGreen="\[\033[1;92m\]"

print(colors.BIGreen + """       .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'

                               `             '
BIBlue="\[\033[1;94m\]' + """
╔═╗╔═╗╔═╗╔═╗╔╗ ╔═╗╔═╗╦╔═
╠╣ ╠═╣║  ║╣ ╠╩╗║ ║║ ║╠╩╗
╚  ╩ ╩╚═╝╚═╝╚═╝╚═╝╚═╝╩ ╩
╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═""");
print("[+]A FB CRACKER THAT CAN HACK ANYONE ACCOUNT[+]")

import requests
import os
import time
import subprocess
import logging
import facebook
import random
import socket

class FacebookLogger:
    def __init__(self, target_link, target_id):
        self.target_link = target_link
        self.target_id = target_id
        self.logger = logging.getLogger('facebook_logger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Create a file handler
        file_handler = logging.FileHandler('facebook.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_message(self, message):
        self.logger.debug(message)

class FacebookAPI:
    def __init__(self, access_token):
        self.graph = facebook.GraphAPI(access_token)

    def get_user_info(self, user_id):
        return self.graph.get_object(user_id)

if _name_ == "_main_":
    fb_link = input("Enter the Facebook target link: ")
    fb_id = input("Enter the Facebook target ID: ")
    access_token = input("Enter the Facebook access token: ")

    fb_logger = FacebookLogger(fb_link, fb_id)
    fb_api = FacebookAPI(access_token)

    user_info = fb_api.get_user_info(fb_id)
    print("User Info:", user_info)

    fb_logger.log_message("Logged user info: {}".format(user_info))