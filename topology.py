#!/usr/bin/python

"""This example shows how to work in adhoc mode

sta1 <---> sta2 <---> sta3"""

import sys

from mininet.node import RemoteController
from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology():
    "Create a network."
    #net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference, controller=RemoteController)
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")    
    sta1 = net.addStation('sta1', position='10,10,0', range='100')
    sta2 = net.addStation('sta2', position='50,10,0', range='100')
    sta3 = net.addStation('sta3', position='90,10,0', range='100')
    c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6653)

    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()
    net.plotGraph(max_x=300, max_y=300)

    info("*** Creating links\n")
    net.addLink(sta1, cls=adhoc, ssid='adhocNet',
                mode='g', channel=5)
    net.addLink(sta2, cls=adhoc, ssid='adhocNet',
                mode='g', channel=5)
    net.addLink(sta3, cls=adhoc, ssid='adhocNet',
                mode='g', channel=5)

    info("*** Starting network\n")
    net.build()
    #c1.start()

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')    
    topology()
