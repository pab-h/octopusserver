# Octopusserver

![Octopus](./assets/octopus.png)

## How to install
### Pypi
```bash 
pip install octopusserver
```
### Poetry
```bash 
poetry add octopusserver
```

## Getting Started
```python
from octopusserver import Octopus
from octopusserver import Request
from octopusserver import Response

PORT = 3000

app = Octopus(PORT)

def hello_world(req: Request, res: Response):
    res.send("Hello, World!")

app.router.get("/", [hello_world])

app.listen(lambda: print(f"Server listen on http://localhost:{ PORT }/"))
```

## How to register your application's routes
```python
from octopusserver import Octopus

PORT = 3000

app = Octopus(PORT)

router = app.router

router.get("path/to/get/route/", [trigger_get_route])

router.post("path/to/post/route/", [trigger_post_route])

```

## For the future
- [ ] Recive files
- [ ] Handling post and get data

## How did I do this? 
[Here](./HOW_DID_I_DO_THIS.md) 

## References
* [ExpressJs](https://expressjs.com/)
* [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
* [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)
* [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
* [HTTP Server: Everything you need to know to Build a simple HTTP server from scratch](https://medium.com/from-the-scratch/http-server-what-do-you-need-to-know-to-build-a-simple-http-server-from-scratch-d1ef8945e4fa)
* [Writing an HTTP server from scratch](https://bhch.github.io/posts/2017/11/writing-an-http-server-from-scratch/)
* [Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
* [Hash table](https://en.wikipedia.org/wiki/Hash_table)