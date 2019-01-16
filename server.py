from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


# Instantiate a dummy authorizer for managing 'virtual' users
authorizer = DummyAuthorizer()
# Define a new user having full r/w permissions and a read-only
authorizer.add_user("Nahid", "7777", "/home/nahid", perm="elradfmw")
# anonymous user
authorizer.add_anonymous("/home/nahid", perm="elradfmw")
# Instantiate FTP handler class
handler = FTPHandler
handler.authorizer = authorizer
# Instantiate FTP server class and listen on 127.0.0.1:7777
server = FTPServer(("127.0.0.1", 7777), handler)
# start ftp server
server.serve_forever() 