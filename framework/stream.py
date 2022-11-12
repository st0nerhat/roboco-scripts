from streams import Stream
from typing import TypeVar

contents = TypeVar("contents")

class Mux(Stream[contents]):
    """
    Multiplex multiple streams together into one event
    """
    inputs: tuple[Stream]

    def __init__(self, *inputs):
        self.inputs = inputs
        Stream.__init__(self, self._mux)

    def _mux(self) -> contents:
        event = tuple(map(lambda x: x.next_event(), self.inputs))
        if event[0] == None:
            return None
        else:
            return event

    