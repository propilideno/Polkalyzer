from mininet.topo import Topo

class MininetNX( Topo ):
	def build( self ):
		#Add Switches
		s0 = self.addSwitch('s0')
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		s5 = self.addSwitch('s5')
		s6 = self.addSwitch('s6')
		s7 = self.addSwitch('s7')
		s8 = self.addSwitch('s8')
		s9 = self.addSwitch('s9')
		s10 = self.addSwitch('s10')
		s11 = self.addSwitch('s11')
		s12 = self.addSwitch('s12')
		s13 = self.addSwitch('s13')
		#Add 2 hosts to each switch
		h0 = self.addHost('h0')
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
		h7 = self.addHost('h7')
		h8 = self.addHost('h8')
		h9 = self.addHost('h9')
		h10 = self.addHost('h10')
		h11 = self.addHost('h11')
		h12 = self.addHost('h12')
		h13 = self.addHost('h13')
		h14 = self.addHost('h14')
		h15 = self.addHost('h15')
		h16 = self.addHost('h16')
		h17 = self.addHost('h17')
		h18 = self.addHost('h18')
		h19 = self.addHost('h19')
		h20 = self.addHost('h20')
		h21 = self.addHost('h21')
		h22 = self.addHost('h22')
		h23 = self.addHost('h23')
		h24 = self.addHost('h24')
		h25 = self.addHost('h25')
		h26 = self.addHost('h26')
		h27 = self.addHost('h27')
		#Add a link of hosts and switch
		lhs0 = self.addLink('s0','h0')
		lhs1 = self.addLink('s0','h1')
		lhs2 = self.addLink('s1','h2')
		lhs3 = self.addLink('s1','h3')
		lhs4 = self.addLink('s2','h4')
		lhs5 = self.addLink('s2','h5')
		lhs6 = self.addLink('s3','h6')
		lhs7 = self.addLink('s3','h7')
		lhs8 = self.addLink('s4','h8')
		lhs9 = self.addLink('s4','h9')
		lhs10 = self.addLink('s5','h10')
		lhs11 = self.addLink('s5','h11')
		lhs12 = self.addLink('s6','h12')
		lhs13 = self.addLink('s6','h13')
		lhs14 = self.addLink('s7','h14')
		lhs15 = self.addLink('s7','h15')
		lhs16 = self.addLink('s8','h16')
		lhs17 = self.addLink('s8','h17')
		lhs18 = self.addLink('s9','h18')
		lhs19 = self.addLink('s9','h19')
		lhs20 = self.addLink('s10','h20')
		lhs21 = self.addLink('s10','h21')
		lhs22 = self.addLink('s11','h22')
		lhs23 = self.addLink('s11','h23')
		lhs24 = self.addLink('s12','h24')
		lhs25 = self.addLink('s12','h25')
		lhs26 = self.addLink('s13','h26')
		lhs27 = self.addLink('s13','h27')
		#Add a link of switches of original topology
		lss0 = self.addLink('s0','s1')
		lss1 = self.addLink('s0','s7')
		lss2 = self.addLink('s1','s2')
		lss3 = self.addLink('s1','s6')
		lss4 = self.addLink('s2','s3')
		lss5 = self.addLink('s3','s4')
		lss6 = self.addLink('s3','s6')
		lss7 = self.addLink('s4','s5')
		lss8 = self.addLink('s5','s10')
		lss9 = self.addLink('s6','s7')
		lss10 = self.addLink('s6','s10')
		lss11 = self.addLink('s6','s11')
		lss12 = self.addLink('s6','s12')
		lss13 = self.addLink('s6','s13')
		lss14 = self.addLink('s7','s8')
		lss15 = self.addLink('s8','s9')
		lss16 = self.addLink('s9','s10')
		
topos = { 'Compuserve': ( lambda: MininetNX() ) }