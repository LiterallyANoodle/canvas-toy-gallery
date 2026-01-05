from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import psycopg2

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
        try:
            print(f"Connecting to database {config['db_name']} on {config['db_host_name']}")
            conn = psycopg2.connect(
                dbname=config['db_name'],
                user=config['db_user'],
                password=config['db_pwd'],
                host=config['db_host_name']
            )
            cur = conn.cursor()

            print('PostgreSQL database version:')
            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            print(db_version)

            cur.close()
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database conneciton closed.')

        # send back image in response

if __name__ == "__main__":
    config = GalleryConfiguration().configuration
    web_server = HTTPServer((config['host_name'], config['server_port']), GalleryServer)
    print(f"Server started http://{config['host_name']}:{config['server_port']}")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        print("Received interrupt command.")

    web_server.server_close()
    print("Server stopped.")