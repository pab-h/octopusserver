# How did I do this? 

## Manage client requests
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
