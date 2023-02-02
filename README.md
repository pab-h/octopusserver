# Octopusserver

![Octopus](./assets/octopus.png)

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