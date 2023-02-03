# How did I do this? 

## Manage client requests
**Note**: This functions are methods of Server class
```python
def listen(self, callback: Callback | None = None):
    self.socket.listen()
    
    self.runnnig = True
    
    self.resolve_queue_thread.start()

    ...

    if not callback is None:
        callback() 

    ...

    while self.runnnig:
        (client, client_address) = self.socket.accept()

        self.queue.enqueue(client)
```

```python
def resolve_queue(self):
    while self.runnnig:
        max_thread_condition = active_thread_count() - 2 <= self.MAX_RESPONSE_THREAD

        while max_thread_condition and not self.queue.is_empty():
            client = self.queue.dequeue()

            response_thread = Thread(
                target=self.handle, 
                args=[client]
            )

            response_thread.start()
```
**Note**: Method called in thread on `self.resolve_queue_thread.start()`

## Handle Request
```python
def handle(self, client: socket.socket):
    try:
        request_raw = client.recv(self.BUFFER_SIZE).decode()

        request = Request(request_raw) 

        response = Response(client) 

        for trigger in self.router.uses: 
            trigger(request, response)

        triggers = self.router.find(HttpMethod(request.method), request.path)
        
        if not triggers is None:
            for trigger in triggers:
                trigger(request, response) 

        else: 
            filename = f"{self.router.static_folder}{request.path}"

            if path_exists(filename):
                response.send_file(filename)

            else:  

                response.send_error(
                    HttpStatus.NOT_FOUND, 
                    str(HttpStatus.NOT_FOUND.value)
                )

    finally:
        client.close()
```

## Find Routes
**Note**: This functions are methods of Router class
```python
    def __init__(self) -> None:
        self.routes: dict[str, list[Trigger]] = {} 
        ...

    def find(self, method: HttpMethod, path: str):
        key = f"{method}:{path}"

        return self.routes.get(key)
```