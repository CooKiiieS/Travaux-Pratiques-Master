from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Node
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

class Test_Topo(Topo):
  def __init__(self):
    "Create P2P topology"
    # Initialiser la topologie
    Topo.__init__(self)
    # Ajouter les hôtes et les switchs
    h1 = self.addNode('h1')
    h2 = self.addNode('h2')
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    # Ajouter les liaisons
    self.addLink(h1, s1)
    self.addLink(s1, s2)
    self.addLink(s2, s3)
    self.addLink(s3, h2)
topos = {
          'toptest' : (lambda: Test_Topo())
}

def topTest():
  topo = Test_Topo()
  net = Mininet(topo=topo, link=TCLink)
  net.start()
  h1 = net.get('h1')
  h2 = net.get('h2')
  h1int0 = h1.intf('h1-eth0')
  h2int0 = h2.intf('h2-eth0')
  h1.setIP('192.168.1.1', 24, h1int0)
  h2.setIP('192.168.1.2', 24, h2int0)
  net.pingAll() # Ping entre tous les clients apres creation du reseau
  CLI(net) # Sans cette ligne, on ne verrait jamais le CLI
  net.stop() # Ne pas oublier de detruire le reseau
if __name__ == '__main__':
    setLogLevel('info')
    topTest()