from __future__ import annotations

from ..port import Ports


class Device:
    """
    Base class for all Vex IQ devices.
    """
    @property
    def port(self) -> Ports:
        return self._port

    @port.setter
    def port(self, port: Ports):
        self._port = port

    def __str__(self) -> str:
        return f'{type(self).__name__}@{self.port}'


class DeviceWithoutPort:
    def __str__(self) -> str:
        return type(self).__name__
