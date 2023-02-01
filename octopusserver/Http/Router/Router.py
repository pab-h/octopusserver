from ...Utils import HttpMethod

from .Request import Request

from .Response import Response

from typing import Callable

import os

Trigger = Callable[[Request, Response], None]

class Router:
    def __init__(self) -> None:
        self.routes: dict[str, list[Trigger]] = {}

        self.uses: list[Trigger] = []
        
        self.static_folder: str | None = None

    def static(self, path: str):
        if os.path.exists(path):
            self.static_folder = path

    def use(self, trigger: Trigger):
        self.uses.append(trigger)

    def join(self, router: 'Router'):        
        self.routes.update(router.routes)
        
    def method(self, method: HttpMethod, path: str, triggers: list[Trigger]): 
        key = f"{method}:{path}"

        self.routes.update({ key: triggers }) 

    def get(self, path: str, triggers: list[Trigger]):
        self.method(HttpMethod.GET, path, triggers)

    def post(self, path: str, triggers: list[Trigger]):
        self.method(HttpMethod.POST, path, triggers)

    def find(self, method: HttpMethod, path: str):
        key = f"{method}:{path}"

        return self.routes.get(key)

if __name__ == "__main__":
    router = Router()

    def hello(req: Request, res: Response):
        res.send("Hello, World!")

    router.method(HttpMethod.GET, "/", [hello])

    print(router.find(HttpMethod.GET, "/"))
    print(router.find(HttpMethod.GET, "+"))
