from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class GalleryConfiguration:

    configuration = {}

    def __init__(self) -> None:
        try: 
            config_file = open("configuration.json")
            self.configuration = json.loads(config_file.read())
        except:
            print("Error: Unable to load server configuration.")
            exit()

class GalleryServer(BaseHTTPRequestHandler):

    def do_OPTIONS(self) -> None:
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:

        # read path for image number

        # find image in database or the 404 image

        # send back image in response

        pass

if __name__ == "__main__":
    config = GalleryConfiguration().configuration
    web_server = HTTPServer((config['host_name'], config['server_port']), GalleryServer)
    print(f"Server started http://{config['host_name']}:{config['server_port']}")