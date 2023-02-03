# Octopusserver

![Octopus](https://github.com/pab-h/octopusserver/blob/main/assets/octopus.png)

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