# -*- coding: utf-8 -*-f
from email_server.server import EmailServer

server = EmailServer()
server.login('satinfivee@gmail.com', 'AJOL_1809')
msg = (
    "Ya puse lo de los mensajes bien, ahora deberia ir sin problemas :) :) :)\n "
    "¿ya ves que guay?\nMuchos chus y ten un dia super, super bueno."
    )
server.send_email(['satinfivee@gmail.com', ], 'Good morning!', msg)