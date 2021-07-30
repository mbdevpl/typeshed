from typing import Any

from .command import Command as Command
from .errorhandler import ErrorCode as ErrorCode

LOGGER: Any

class RemoteConnection:
    @classmethod
    def get_timeout(cls): ...
    @classmethod
    def set_timeout(cls, timeout) -> None: ...
    @classmethod
    def reset_timeout(cls) -> None: ...
    @classmethod
    def get_remote_connection_headers(cls, parsed_url, keep_alive: bool = ...): ...
    keep_alive: Any
    def __init__(self, remote_server_addr, keep_alive: bool = ..., resolve_ip: bool = ...) -> None: ...
    def execute(self, command, params): ...