from smtplib import SMTP, SMTPAuthenticationError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Steps
# Args -> port, host, username, password
# 1. ehlo connection
# 2. enable tls
# 3. login
# 4. send mail
# 5. close conn

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

class EmailServer:
    # Context Manager to manage email connection
    class EmailConnection:

        def __init__(self, host, port, server):
            self.host = host
            self.port = port
            self.server = server

        def __enter__(self):
            if not self.server._connection:
                connection = SMTP(self.host, self.port)
                connection.ehlo()
                connection.starttls()
                self.server._connection = connection
            return self.server._connection

        def __exit__(self, *args):
            if not self.server._persists:
                self.server._connection.quit()
                self.server._connection = None

    def __init__(self):
        # Server information
        self._host = EMAIL_HOST
        self._port = EMAIL_PORT

        # Credentials are setted in login method
        self.username = None
        self.password = None

        # Connection details
        self._persists = False
        self._connection = None

    def __persists_connection(self):
        self._persists = True
    
    def __no_persists_connection(self):
        self._persists = False

    def login(self, username, password):
        with EmailServer.EmailConnection(self._host, self._port, self) as emconn:
            try:
                emconn.login(username, password)
            except SMTPAuthenticationError:
                raise Exception("Incorrect login")
            else:
                self.__persists_connection()
                self.username = username
                self.password = password
                return f'{username} successfully connected to the server.'
        
    def send_email(self, to, subject, body):
        if not isinstance(to, list):
            to = [to]
        msg = MIMEMultipart() 
        msg['From'] = self.username
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with EmailServer.EmailConnection(self._host, self._port, self) as emconn:
            for _to in to:
                msg['To'] = _to
                emconn.sendmail(
                    msg.get('From'), msg.get('To'), msg.as_string())

    def logout(self):
        if not self._connection:
            raise Exception("You're not logged in")
        else:
            with EmailServer.EmailConnection(self._host, self._port, self) as emconn:
                self.username = None
                self.password = None
                self.__no_persists_connection