from abc import ABC, abstractmethod
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.http_types.http_request import HTTPRequest
class ControllerInterface(ABC):
    @abstractmethod
    def handle(self,http_request: HTTPRequest) -> HTTPResponse:
        """Controller handle method"""
        pass