import socket

import logging

from os.path import exists as path_exists

from threading import Thread
from threading import active_count as active_thread_count 

from typing import Callable
 
from .Router import *

from ..Utils import *
from ..Utils import Queue 

Callback = Callable[[], None]

class Server:
    def __init__(self, port: int, buffer_size = 1024, max_response_thread = 2) -> None:
        self.port = port

        self.host = "0.0.0.0"

        self.queue = Queue[socket.socket]()

        self.runnnig = False

        self.MAX_RESPONSE_THREAD = max_response_thread

        self.resolve_queue_thread = Thread(target=self.resolve_queue)

        self.router = Router()

        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) 

        self.socket.setsockopt(
            socket.SOL_SOCKET, 
            socket.SO_REUSEADDR, 
            1
        )

        self.socket.bind((self.host, self.port))

        self.BUFFER_SIZE = buffer_size

        logging.info("Server initialized")

    def resolve_queue(self):
        while self.runnnig:
            max_thread_condition = active_thread_count() - 2 <= self.MAX_RESPONSE_THREAD

            while max_thread_condition and not self.queue.is_empty():
                client = self.queue.dequeue()

                response_thread = Thread(
                    target=self.handle, 
                    args=[client]
                )

                logging.debug("Response thread started")

                response_thread.start()

        logging.critical("Resolve queue thread stoped")
        
    def handle(self, client: socket.socket):
        try:
            request_raw = client.recv(self.BUFFER_SIZE).decode()

            logging.debug("Aceppt socket connection")

            request = Request(request_raw) 

            response = Response(client) 

            logging.info("Running use triggers")

            for trigger in self.router.uses: 
                trigger(request, response)

            triggers = self.router.find(HttpMethod(request.method), request.path)
            
            if not triggers is None:
                logging.debug("Trigger request was activated")

                for trigger in triggers:
                    trigger(request, response) 

                logging.debug("Trigger request stoped")

            else: 
                filename = f"{self.router.static_folder}{request.path}"

                if path_exists(filename):
                    response.send_file(filename)

                else:  
                    logging.warning("No resource was not found")

                    response.send_error(
                        HttpStatus.NOT_FOUND, 
                        str(HttpStatus.NOT_FOUND.value)
                    )

        except:
            logging.error("Error in response request")
        
        finally:
            logging.debug("Close socket connection")

            client.close()

    def listen(self, callback: Callback | None = None):
        self.socket.listen()

        self.runnnig = True

        logging.info("Resolve queue thread started")

        self.resolve_queue_thread.start()

        if not callback is None:
            callback() 

        try: 
            logging.info("Server started")

            while self.runnnig:
                (client, client_address) = self.socket.accept()

                self.queue.enqueue(client)

                logging.debug(f"Enqueue request by { client_address }")

        except:
            self.runnnig = False

            logging.critical("Server stoped")

if __name__ == "__main__":
    from time import time
    from time import sleep

    logging.basicConfig(
        filename = "tmp/log.log",
        format = "%(asctime)s %(module)s %(threadName)s [%(levelname)s] \"%(message)s\"",
        level = logging.DEBUG
    )

    server = Server(8000)

    router = server.router

    def hello_world(req: Request, res: Response):
        start_at = time()
        sleep(60)
        end_at = time()

        res.send({ 
            "start_at": f"{ start_at }",
            "end_at": f"{ end_at }",
            "delta": f"{ end_at - start_at }"
        })

    router.get("/", [hello_world])

    server.listen(lambda: print("\nServer listen on http://localhost:8000"))
