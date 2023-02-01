from enum import Enum

class HttpMethod(Enum):
    GET = 'GET'
    HEAD = 'HEAD'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    CONNECT = 'CONNECT'
    OPTIONS = 'OPTIONS'
    TRACE = 'TRACE'
    PATCH = 'PATCH'

class HttpStatus(Enum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

class HttpContentTypes(Enum):
    HTML = "text/html"
    HTM = "text/html"
    TXT = "text/plain"
    JPEG = "image/jpeg"
    JPG = "image/jpeg"
    