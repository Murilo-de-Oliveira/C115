from __future__ import print_function
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.util import dumpNodeConnections

class NetworkTopo(Topo):
    def build(self, **_opts):

        switch1 = self.addSwitch('s1', failMode='standalone')
        switch2 = self.addSwitch('s2', failMode='standalone')
        switch3 = self.addSwitch('s3', failMode='standalone')

        # Adding hosts
        host1 = self.addHost('d1',ip='192.168.0.1/28',mac='00:00:00:00:00:01')
        host2 = self.addHost('d1',ip='192.168.0.2/28',mac='00:00:00:00:00:02')
        host3 = self.addHost('d1',ip='192.168.0.3/28',mac='00:00:00:00:00:03')
        host4 = self.addHost('d1',ip='192.168.0.4/28',mac='00:00:00:00:00:04')
        host5 = self.addHost('d1',ip='192.168.0.5/28',mac='00:00:00:00:00:05')
        
        connection_list = [
            (host1, switch1),
            (host2, switch1),
            (host3, switch2),
            (host4, switch3),
            (host5, switch3)
        ]

        # Connecting hosts to switches
        for host, switch in connection_list:
            self.addLink(host, switch)

        self.addLink(switch1, switch2)
        self.addLink(switch2, switch3)



def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo, controller=None)
    net.start()
    
    print('####Informacoes das portas####\n\n\n')
    dumpNodeConnections(net.hosts)

    print("\n### Switch em modo NORMAL ###")
    net['s1'].cmd("ovs-ofctl add-flow s1 action=normal")
    net['s2'].cmd("ovs-ofctl add-flow s2 action=normal")
    net['s3'].cmd("ovs-ofctl add-flow s3 action=normal")

    print("\n### Testes de ping ###")
    print(net['h1'].cmd("ping -c 2 10.0.0.5"))
    print(net['h2'].cmd("ping -c 2 10.0.0.1"))
    print(net['h3'].cmd("ping -c 2 10.0.0.2"))
    print(net['h4'].cmd("ping -c 2 10.0.0.4"))
    print(net['h5'].cmd("ping -c 2 10.0.0.3"))

    print("\n### Inserindo regras MAC ###")
    s1, s2, s3 = net['s1'], net['s2'], net['s3']

    for sw in (s1, s2, s3):
        sw.cmd("ovs-ofctl add-flow {} dl_type=0x806,actions=flood".format(sw.name))

    print("\n### Pings apos insercao de regras ###")
    s1.cmd("ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,actions=output:3")
    s2.cmd("ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,actions=output:2")
    s3.cmd("ovs-ofctl add-flow s3 dl_dst=00:00:00:00:00:05,actions=output:1")

    print(net['h1'].cmd("ping -c 2 10.0.0.5"))

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
