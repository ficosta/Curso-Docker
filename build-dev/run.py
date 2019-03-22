import logging
import http.server
import socketserver
import getpass


class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s -- [%s] %s\n"% (
            self.client_address[0],
            self.log_date_time_string(),
            format%args
        ))

logging.basicConfig(
    filename='/log/http-server.log',
    fomart='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger().addHandler(logging.StreamHandler())
logging.info('Inicializando...')
PORT=8000

http = socketserver.TCPServer(("", PORT), MyHTTPHandler)
logging.info('Escutando a porta %s', PORT)
logging.info('Usuário %s', getpass.getuser())
http.serve_forever()