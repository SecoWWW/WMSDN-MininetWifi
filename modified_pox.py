from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.util import str_to_bool
import time

log = core.getLogger()

# some modification

class MyComponent(object):
    def __init__ (self):
        core.openflow.addListeners(self)
        log.debug("Hi starting the controller")
    def _handle_ConnectionUp (self, event):
        log.debug("Switch %s has come up", dpid_to_str(event.dpid))
    def _handle_ConnectionDown(self, event):
        log.debug("Swtich %s is down", dpid_to_str(event.dpid))

def launch():
    core.registerNew(MyComponent)
