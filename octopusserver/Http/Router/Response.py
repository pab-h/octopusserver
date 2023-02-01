import json

from os.path import basename
from os.path import splitext

import logging

from socket import socket

from ...Utils import HttpStatus
from ...Utils import HttpContentTypes

class Response:
    def __init__(self, client: socket) -> None:
        self.status = HttpStatus.OK

        self.protocol = "HTTP/1.1"

        self.client = client

        self.header: dict[str, str] = {}

    @staticmethod
    def content_type_by_file(filename: str):
        extension = splitext(filename)[1]
        extension = extension.replace(".", "")
        extension = extension.upper()
        
        try: 
            return HttpContentTypes[extension]

        except:
            return HttpContentTypes.TXT

    def __build_http_header(self):
        header = f"{self.protocol} {self.status.value} {self.status.name}\n"

        for (key, value) in self.header.items():
            header += f"{key}: {value}\n"

        header += "\n"
                
        return header

    def send(self, body: str | dict | bytes):
        if isinstance(body, dict):
            body = json.dumps(body)

            self.header.update({ "Content-Type": "application/json" })

        self.header.update({ "Content-Length": str(len(body)) }) 

        http_response = self.__build_http_header()

        if isinstance(body, str):
            body = body.encode()

        self.client.sendall(http_response.encode() + body)

    def send_file(self, filename: str):
        try: 
            with open(filename, "rb") as file:
                file_content: bytes = file.read()
                
                content_type = Response.content_type_by_file(filename)

                self.header.update({ "Content-Type": content_type.value })
                 
                self.send(file_content)

        except FileNotFoundError as error:
            logging.error(error)

            filename = basename(filename)

            self.send_error(
                HttpStatus.INTERNAL_SERVER_ERROR,
                f"The file {filename} not exits"
            ) 

    def send_error(self, status: HttpStatus, message: str):
        self.status = status
        
        self.header.update({ "Content-Type": HttpContentTypes.TXT.value })

        self.send(message)

if __name__ == "__main__":
    import os

    filename = f"{os.getcwd()}/index.html"

    print(Response.content_type_by_file(filename))
