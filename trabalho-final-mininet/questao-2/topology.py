from __future__ import print_function
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class NetworkTopo(Topo):
    def build(self, **_opts):

        s1 = self.addSwitch('s1', failMode='standalone')
        s2 = self.addSwitch('s2', failMode='standalone')
        s3 = self.addSwitch('s3', failMode='standalone')

        h1 = self.addHost('h1', ip='192.168.0.1/28', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', ip='192.168.0.2/28', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', ip='192.168.0.3/28', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', ip='192.168.0.4/28', mac='00:00:00:00:00:04')
        h5 = self.addHost('h5', ip='192.168.0.5/28', mac='00:00:00:00:00:05')

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s3)
        self.addLink(h5, s3)

        self.addLink(s1, s2)
        self.addLink(s2, s3)


def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo, controller=None)
    net.start()

    print("\n#### PORTAS DOS HOSTS ####")
    dumpNodeConnections(net.hosts)

    print("\n### SWITCHES EM MODO NORMAL ###")
    for sw in ('s1', 's2', 's3'):
        net[sw].cmd("ovs-ofctl add-flow {} action=normal".format(sw))

    print("\n### TESTES DE PING (NORMAL) ###")
    print(net['h1'].cmd("ping -c 2 192.168.0.5"))
    print(net['h2'].cmd("ping -c 2 192.168.0.1"))
    print(net['h3'].cmd("ping -c 2 192.168.0.2"))
    print(net['h4'].cmd("ping -c 2 192.168.0.4"))
    print(net['h5'].cmd("ping -c 2 192.168.0.3"))

    print("\n### LIMPANDO REGRAS ###")
    for sw in ('s1', 's2', 's3'):
        net[sw].cmd("ovs-ofctl del-flows {}".format(sw))

    print("\n### TESTE SEM REGRAS ###")
    print(net['h1'].cmd("ping -c 2 192.168.0.5"))  # deve falhar

    print("\n### INSERINDO REGRAS MAC ###")
    s1, s2, s3 = net['s1'], net['s2'], net['s3']

    for sw in (s1, s2, s3):
        sw.cmd("ovs-ofctl add-flow {} dl_type=0x806,actions=flood".format(sw.name))

    # Regras ICMP
    s1.cmd("ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,actions=output:3")
    s2.cmd("ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,actions=output:2")
    s3.cmd("ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:05,actions=output:1")

    print("\n### TESTE COM REGRAS ###")
    print(net['h1'].cmd("ping -c 2 192.168.0.5"))

    CLI(net)
    net.stop()


topos = { 'mytopo': NetworkTopo }


if __name__ == '__main__':
    setLogLevel('info')
    run()
