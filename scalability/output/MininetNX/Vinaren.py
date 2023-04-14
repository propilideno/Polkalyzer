from mininet.topo import Topo

class MininetNX( Topo ):
	def build( self ):
		#DefaultParameters
		switchParameters= {}
		hostParameters= {}
		linkHSParameters= {}
		linkSSParameters= {}
		#Add Switches
		s0 = self.addSwitch('s0',**switchParameters)
		s1 = self.addSwitch('s1',**switchParameters)
		s2 = self.addSwitch('s2',**switchParameters)
		s3 = self.addSwitch('s3',**switchParameters)
		s4 = self.addSwitch('s4',**switchParameters)
		s5 = self.addSwitch('s5',**switchParameters)
		s6 = self.addSwitch('s6',**switchParameters)
		s7 = self.addSwitch('s7',**switchParameters)
		s8 = self.addSwitch('s8',**switchParameters)
		s9 = self.addSwitch('s9',**switchParameters)
		s10 = self.addSwitch('s10',**switchParameters)
		s11 = self.addSwitch('s11',**switchParameters)
		s12 = self.addSwitch('s12',**switchParameters)
		s13 = self.addSwitch('s13',**switchParameters)
		s14 = self.addSwitch('s14',**switchParameters)
		s15 = self.addSwitch('s15',**switchParameters)
		s16 = self.addSwitch('s16',**switchParameters)
		s17 = self.addSwitch('s17',**switchParameters)
		s18 = self.addSwitch('s18',**switchParameters)
		s19 = self.addSwitch('s19',**switchParameters)
		s20 = self.addSwitch('s20',**switchParameters)
		s21 = self.addSwitch('s21',**switchParameters)
		s22 = self.addSwitch('s22',**switchParameters)
		s23 = self.addSwitch('s23',**switchParameters)
		s24 = self.addSwitch('s24',**switchParameters)
		#Add 2 hosts to each switch
		h0 = self.addHost('h0',**hostParameters)
		h1 = self.addHost('h1',**hostParameters)
		h2 = self.addHost('h2',**hostParameters)
		h3 = self.addHost('h3',**hostParameters)
		h4 = self.addHost('h4',**hostParameters)
		h5 = self.addHost('h5',**hostParameters)
		h6 = self.addHost('h6',**hostParameters)
		h7 = self.addHost('h7',**hostParameters)
		h8 = self.addHost('h8',**hostParameters)
		h9 = self.addHost('h9',**hostParameters)
		h10 = self.addHost('h10',**hostParameters)
		h11 = self.addHost('h11',**hostParameters)
		h12 = self.addHost('h12',**hostParameters)
		h13 = self.addHost('h13',**hostParameters)
		h14 = self.addHost('h14',**hostParameters)
		h15 = self.addHost('h15',**hostParameters)
		h16 = self.addHost('h16',**hostParameters)
		h17 = self.addHost('h17',**hostParameters)
		h18 = self.addHost('h18',**hostParameters)
		h19 = self.addHost('h19',**hostParameters)
		h20 = self.addHost('h20',**hostParameters)
		h21 = self.addHost('h21',**hostParameters)
		h22 = self.addHost('h22',**hostParameters)
		h23 = self.addHost('h23',**hostParameters)
		h24 = self.addHost('h24',**hostParameters)
		h25 = self.addHost('h25',**hostParameters)
		h26 = self.addHost('h26',**hostParameters)
		h27 = self.addHost('h27',**hostParameters)
		h28 = self.addHost('h28',**hostParameters)
		h29 = self.addHost('h29',**hostParameters)
		h30 = self.addHost('h30',**hostParameters)
		h31 = self.addHost('h31',**hostParameters)
		h32 = self.addHost('h32',**hostParameters)
		h33 = self.addHost('h33',**hostParameters)
		h34 = self.addHost('h34',**hostParameters)
		h35 = self.addHost('h35',**hostParameters)
		h36 = self.addHost('h36',**hostParameters)
		h37 = self.addHost('h37',**hostParameters)
		h38 = self.addHost('h38',**hostParameters)
		h39 = self.addHost('h39',**hostParameters)
		h40 = self.addHost('h40',**hostParameters)
		h41 = self.addHost('h41',**hostParameters)
		h42 = self.addHost('h42',**hostParameters)
		h43 = self.addHost('h43',**hostParameters)
		h44 = self.addHost('h44',**hostParameters)
		h45 = self.addHost('h45',**hostParameters)
		h46 = self.addHost('h46',**hostParameters)
		h47 = self.addHost('h47',**hostParameters)
		h48 = self.addHost('h48',**hostParameters)
		h49 = self.addHost('h49',**hostParameters)
		#Add a link of hosts and switch
		lhs0 = self.addLink('s0','h0',**linkHSParameters)
		lhs1 = self.addLink('s0','h1',**linkHSParameters)
		lhs2 = self.addLink('s1','h2',**linkHSParameters)
		lhs3 = self.addLink('s1','h3',**linkHSParameters)
		lhs4 = self.addLink('s2','h4',**linkHSParameters)
		lhs5 = self.addLink('s2','h5',**linkHSParameters)
		lhs6 = self.addLink('s3','h6',**linkHSParameters)
		lhs7 = self.addLink('s3','h7',**linkHSParameters)
		lhs8 = self.addLink('s4','h8',**linkHSParameters)
		lhs9 = self.addLink('s4','h9',**linkHSParameters)
		lhs10 = self.addLink('s5','h10',**linkHSParameters)
		lhs11 = self.addLink('s5','h11',**linkHSParameters)
		lhs12 = self.addLink('s6','h12',**linkHSParameters)
		lhs13 = self.addLink('s6','h13',**linkHSParameters)
		lhs14 = self.addLink('s7','h14',**linkHSParameters)
		lhs15 = self.addLink('s7','h15',**linkHSParameters)
		lhs16 = self.addLink('s8','h16',**linkHSParameters)
		lhs17 = self.addLink('s8','h17',**linkHSParameters)
		lhs18 = self.addLink('s9','h18',**linkHSParameters)
		lhs19 = self.addLink('s9','h19',**linkHSParameters)
		lhs20 = self.addLink('s10','h20',**linkHSParameters)
		lhs21 = self.addLink('s10','h21',**linkHSParameters)
		lhs22 = self.addLink('s11','h22',**linkHSParameters)
		lhs23 = self.addLink('s11','h23',**linkHSParameters)
		lhs24 = self.addLink('s12','h24',**linkHSParameters)
		lhs25 = self.addLink('s12','h25',**linkHSParameters)
		lhs26 = self.addLink('s13','h26',**linkHSParameters)
		lhs27 = self.addLink('s13','h27',**linkHSParameters)
		lhs28 = self.addLink('s14','h28',**linkHSParameters)
		lhs29 = self.addLink('s14','h29',**linkHSParameters)
		lhs30 = self.addLink('s15','h30',**linkHSParameters)
		lhs31 = self.addLink('s15','h31',**linkHSParameters)
		lhs32 = self.addLink('s16','h32',**linkHSParameters)
		lhs33 = self.addLink('s16','h33',**linkHSParameters)
		lhs34 = self.addLink('s17','h34',**linkHSParameters)
		lhs35 = self.addLink('s17','h35',**linkHSParameters)
		lhs36 = self.addLink('s18','h36',**linkHSParameters)
		lhs37 = self.addLink('s18','h37',**linkHSParameters)
		lhs38 = self.addLink('s19','h38',**linkHSParameters)
		lhs39 = self.addLink('s19','h39',**linkHSParameters)
		lhs40 = self.addLink('s20','h40',**linkHSParameters)
		lhs41 = self.addLink('s20','h41',**linkHSParameters)
		lhs42 = self.addLink('s21','h42',**linkHSParameters)
		lhs43 = self.addLink('s21','h43',**linkHSParameters)
		lhs44 = self.addLink('s22','h44',**linkHSParameters)
		lhs45 = self.addLink('s22','h45',**linkHSParameters)
		lhs46 = self.addLink('s23','h46',**linkHSParameters)
		lhs47 = self.addLink('s23','h47',**linkHSParameters)
		lhs48 = self.addLink('s24','h48',**linkHSParameters)
		lhs49 = self.addLink('s24','h49',**linkHSParameters)
		#Add a link of switches of original topology
		lss0 = self.addLink('s0','s7',**linkSSParameters)
		lss1 = self.addLink('s1','s7',**linkSSParameters)
		lss2 = self.addLink('s2','s7',**linkSSParameters)
		lss3 = self.addLink('s3','s17',**linkSSParameters)
		lss4 = self.addLink('s4','s13',**linkSSParameters)
		lss5 = self.addLink('s5','s15',**linkSSParameters)
		lss6 = self.addLink('s6','s7',**linkSSParameters)
		lss7 = self.addLink('s7','s8',**linkSSParameters)
		lss8 = self.addLink('s7','s14',**linkSSParameters)
		lss9 = self.addLink('s7','s16',**linkSSParameters)
		lss10 = self.addLink('s7','s17',**linkSSParameters)
		lss11 = self.addLink('s9','s10',**linkSSParameters)
		lss12 = self.addLink('s9','s21',**linkSSParameters)
		lss13 = self.addLink('s10','s11',**linkSSParameters)
		lss14 = self.addLink('s10','s20',**linkSSParameters)
		lss15 = self.addLink('s10','s13',**linkSSParameters)
		lss16 = self.addLink('s11','s19',**linkSSParameters)
		lss17 = self.addLink('s11','s12',**linkSSParameters)
		lss18 = self.addLink('s11','s13',**linkSSParameters)
		lss19 = self.addLink('s13','s14',**linkSSParameters)
		lss20 = self.addLink('s13','s22',**linkSSParameters)
		lss21 = self.addLink('s13','s23',**linkSSParameters)
		lss22 = self.addLink('s13','s24',**linkSSParameters)
		lss23 = self.addLink('s14','s17',**linkSSParameters)
		lss24 = self.addLink('s14','s15',**linkSSParameters)
		lss25 = self.addLink('s17','s18',**linkSSParameters)
		
topos = { 'Vinaren': ( lambda: MininetNX() ) }