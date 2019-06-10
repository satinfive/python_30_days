# -*- coding: utf-8 -*-f
import os
from dotenv import load_dotenv
from email_server.server import EmailServer

# loads env variables
load_dotenv()

from_email = os.getenv('EMAIL')
password = os.getenv('EMAIL_PASSWORD')
to_email = os.getenv('TO_EMAIL')

server = EmailServer()
server.login('satinfivee@gmail.com', 'AJOL_1809')
msg = (
    "Ya puse lo de los mensajes bien, ahora deberia ir sin problemas :) :) :)\n "
    "¿ya ves que guay?\nMuchos chus y ten un dia super, super bueno."
    )
server.send_email([to_email, ], 'Good morning!', msg)