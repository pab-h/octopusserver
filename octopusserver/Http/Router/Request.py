from typing import Any

class Request:
    def __init__(self, request_raw: str) -> None:
        request_raw = request_raw.replace("\r", "")
        
        [header_raw, self.body] = request_raw.split("\n\n")

        header_lines = header_raw.split("\n")
        reqeust_line = header_lines.pop(0)
        [self.method, self.path, self.protocol] = reqeust_line.split(" ")

        self.header: dict[str, str] = {}

        for line in header_lines:
            [key, value] = line.split(": ") 

            self.header.update({ key: value })

        self.data: dict[str, Any] = {}


if __name__ == "__main__":
    request = Request(
"""GET / HTTP/1.1
Host: localhost:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1

{"oi":"123"}"""
)
 
    print(request.body)
    print(request.method)
    print(request.path)
    print(request.protocol)
    print(request.header)
