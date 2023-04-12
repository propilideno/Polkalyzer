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
		s14 = self.addSwitch('s14')
		s15 = self.addSwitch('s15')
		s16 = self.addSwitch('s16')
		s17 = self.addSwitch('s17')
		s18 = self.addSwitch('s18')
		s19 = self.addSwitch('s19')
		s20 = self.addSwitch('s20')
		s21 = self.addSwitch('s21')
		s22 = self.addSwitch('s22')
		s23 = self.addSwitch('s23')
		s24 = self.addSwitch('s24')
		s25 = self.addSwitch('s25')
		s26 = self.addSwitch('s26')
		s27 = self.addSwitch('s27')
		s28 = self.addSwitch('s28')
		s29 = self.addSwitch('s29')
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
		h28 = self.addHost('h28')
		h29 = self.addHost('h29')
		h30 = self.addHost('h30')
		h31 = self.addHost('h31')
		h32 = self.addHost('h32')
		h33 = self.addHost('h33')
		h34 = self.addHost('h34')
		h35 = self.addHost('h35')
		h36 = self.addHost('h36')
		h37 = self.addHost('h37')
		h38 = self.addHost('h38')
		h39 = self.addHost('h39')
		h40 = self.addHost('h40')
		h41 = self.addHost('h41')
		h42 = self.addHost('h42')
		h43 = self.addHost('h43')
		h44 = self.addHost('h44')
		h45 = self.addHost('h45')
		h46 = self.addHost('h46')
		h47 = self.addHost('h47')
		h48 = self.addHost('h48')
		h49 = self.addHost('h49')
		h50 = self.addHost('h50')
		h51 = self.addHost('h51')
		h52 = self.addHost('h52')
		h53 = self.addHost('h53')
		h54 = self.addHost('h54')
		h55 = self.addHost('h55')
		h56 = self.addHost('h56')
		h57 = self.addHost('h57')
		h58 = self.addHost('h58')
		h59 = self.addHost('h59')
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
		lhs28 = self.addLink('s14','h28')
		lhs29 = self.addLink('s14','h29')
		lhs30 = self.addLink('s15','h30')
		lhs31 = self.addLink('s15','h31')
		lhs32 = self.addLink('s16','h32')
		lhs33 = self.addLink('s16','h33')
		lhs34 = self.addLink('s17','h34')
		lhs35 = self.addLink('s17','h35')
		lhs36 = self.addLink('s18','h36')
		lhs37 = self.addLink('s18','h37')
		lhs38 = self.addLink('s19','h38')
		lhs39 = self.addLink('s19','h39')
		lhs40 = self.addLink('s20','h40')
		lhs41 = self.addLink('s20','h41')
		lhs42 = self.addLink('s21','h42')
		lhs43 = self.addLink('s21','h43')
		lhs44 = self.addLink('s22','h44')
		lhs45 = self.addLink('s22','h45')
		lhs46 = self.addLink('s23','h46')
		lhs47 = self.addLink('s23','h47')
		lhs48 = self.addLink('s24','h48')
		lhs49 = self.addLink('s24','h49')
		lhs50 = self.addLink('s25','h50')
		lhs51 = self.addLink('s25','h51')
		lhs52 = self.addLink('s26','h52')
		lhs53 = self.addLink('s26','h53')
		lhs54 = self.addLink('s27','h54')
		lhs55 = self.addLink('s27','h55')
		lhs56 = self.addLink('s28','h56')
		lhs57 = self.addLink('s28','h57')
		lhs58 = self.addLink('s29','h58')
		lhs59 = self.addLink('s29','h59')
		#Add a link of switches of original topology
		lss0 = self.addLink('s0','s9')
		lss1 = self.addLink('s0','s4')
		lss2 = self.addLink('s0','s29')
		lss3 = self.addLink('s1','s2')
		lss4 = self.addLink('s1','s3')
		lss5 = self.addLink('s1','s29')
		lss6 = self.addLink('s2','s29')
		lss7 = self.addLink('s3','s29')
		lss8 = self.addLink('s4','s29')
		lss9 = self.addLink('s5','s14')
		lss10 = self.addLink('s6','s13')
		lss11 = self.addLink('s7','s8')
		lss12 = self.addLink('s7','s28')
		lss13 = self.addLink('s8','s27')
		lss14 = self.addLink('s8','s12')
		lss15 = self.addLink('s9','s10')
		lss16 = self.addLink('s9','s20')
		lss17 = self.addLink('s10','s11')
		lss18 = self.addLink('s10','s13')
		lss19 = self.addLink('s12','s13')
		lss20 = self.addLink('s12','s14')
		lss21 = self.addLink('s12','s16')
		lss22 = self.addLink('s12','s23')
		lss23 = self.addLink('s12','s24')
		lss24 = self.addLink('s12','s25')
		lss25 = self.addLink('s12','s26')
		lss26 = self.addLink('s14','s15')
		lss27 = self.addLink('s14','s17')
		lss28 = self.addLink('s14','s21')
		lss29 = self.addLink('s14','s22')
		lss30 = self.addLink('s14','s29')
		lss31 = self.addLink('s18','s29')
		lss32 = self.addLink('s19','s29')
		
topos = { 'WideJpn': ( lambda: MininetNX() ) }