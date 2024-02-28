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

    # Ajouter les liaisons
    self.addLink(h2, s1)
    self.addLink(h1, s1)

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
  h1.setIP('11.0.0.1', 8, h1int0)
  h2.setIP('11.0.0.3', 8, h2int0)
  CLI(net) # Sans cette ligne, on ne verrait jamais le CLI
  net.stop() # Ne pas oublier de detruire le reseau
if __name__ == '__main__':
    setLogLevel('info')
    topTest()