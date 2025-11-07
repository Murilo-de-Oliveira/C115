from __future__ import print_function
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections

class NetworkTopo(Topo):
    def build(self, **_opts):

        switch1 = self.addSwitch('s1', failMode='standalone')
        switch2 = self.addSwitch('s2', failMode='standalone')
        switch3 = self.addSwitch('s3', failMode='standalone')

        host1 = self.addHost('h1', ip='192.168.0.1/28')
        host2 = self.addHost('h2', ip='192.168.0.2/28')
        host3 = self.addHost('h3', ip='192.168.0.3/28')
        host4 = self.addHost('h4', ip='192.168.0.4/28')
        host5 = self.addHost('h5', ip='192.168.0.5/28')

        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch2)
        self.addLink(host4, switch3)
        self.addLink(host5, switch3)

        self.addLink(switch1, switch2)
        self.addLink(switch2, switch3)


def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo, autoSetMacs=True, controller=None)
    net.start()

    print("\n#### Inspecao dos hosts ####")
    CLI(net, script="inspec.sh")

    print("\n### Teste de ping ###")
    CLI(net, script="ping.sh")

    print("\n### Limpar regras ###")
    for sw in ('s1', 's2', 's3'):
        net[sw].cmd("ovs-ofctl del-flows {}".format(sw))

    print("\n### Adicionar novas regras ###")
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,actions=output:2')
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,actions=output:1')
    
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:1')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:2')
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:1')
    
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:3')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:1')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2')
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:1')
    
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,actions=output:3')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,actions=output:2')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,actions=output:2')
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,actions=output:1')
    
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03,actions=output:1')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:2')
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:2')
    
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:3')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:1')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:2')
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:2')
    
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:05,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:05,actions=output:3')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:05,actions=output:2')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:02,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:02,actions=output:2')
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:02,actions=output:2')
    
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:04,actions=output:3')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:04,actions=output:1')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:03,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:03,actions=output:1')
    
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:05,actions=output:3')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:05,actions=output:2')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:03,actions=output:3')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:03,actions=output:1')
    
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:05,actions=output:2')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:04,actions=output:1')
    
    net['s1'].cmd('ovs-ofctl add-flow s1 dl_type=0x806,nw_proto=1,action=flood')
    net['s2'].cmd('ovs-ofctl add-flow s2 dl_type=0x806,nw_proto=1,action=flood')
    net['s3'].cmd('ovs-ofctl add-flow s3 dl_type=0x806,nw_proto=1,action=flood')

    host1 = net.get('h1')

    print(host1.cmd('ovs-ofctl dump-flows s1'))
    print(host1.cmd('ovs-ofctl dump-flows s2'))
    print(host1.cmd('ovs-ofctl dump-flows s3'))

    print("\n### Teste de ping com as regras ###")
    CLI(net, script="ping.sh") 

    net.stop()


topos = { 'mytopo': NetworkTopo }


if __name__ == '__main__':
    setLogLevel('info')
    run()
