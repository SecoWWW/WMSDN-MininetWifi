from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.util import str_to_bool
import time

log = core.getLogger()


def _handle_connectioUp(self, event):
    """
    SOme modified strategy
    """
    print "Switch %s has come up." % event.dpid
