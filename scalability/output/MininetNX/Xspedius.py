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
		s25 = self.addSwitch('s25',**switchParameters)
		s26 = self.addSwitch('s26',**switchParameters)
		s27 = self.addSwitch('s27',**switchParameters)
		s28 = self.addSwitch('s28',**switchParameters)
		s29 = self.addSwitch('s29',**switchParameters)
		s30 = self.addSwitch('s30',**switchParameters)
		s31 = self.addSwitch('s31',**switchParameters)
		s32 = self.addSwitch('s32',**switchParameters)
		s33 = self.addSwitch('s33',**switchParameters)
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
		h50 = self.addHost('h50',**hostParameters)
		h51 = self.addHost('h51',**hostParameters)
		h52 = self.addHost('h52',**hostParameters)
		h53 = self.addHost('h53',**hostParameters)
		h54 = self.addHost('h54',**hostParameters)
		h55 = self.addHost('h55',**hostParameters)
		h56 = self.addHost('h56',**hostParameters)
		h57 = self.addHost('h57',**hostParameters)
		h58 = self.addHost('h58',**hostParameters)
		h59 = self.addHost('h59',**hostParameters)
		h60 = self.addHost('h60',**hostParameters)
		h61 = self.addHost('h61',**hostParameters)
		h62 = self.addHost('h62',**hostParameters)
		h63 = self.addHost('h63',**hostParameters)
		h64 = self.addHost('h64',**hostParameters)
		h65 = self.addHost('h65',**hostParameters)
		h66 = self.addHost('h66',**hostParameters)
		h67 = self.addHost('h67',**hostParameters)
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
		lhs50 = self.addLink('s25','h50',**linkHSParameters)
		lhs51 = self.addLink('s25','h51',**linkHSParameters)
		lhs52 = self.addLink('s26','h52',**linkHSParameters)
		lhs53 = self.addLink('s26','h53',**linkHSParameters)
		lhs54 = self.addLink('s27','h54',**linkHSParameters)
		lhs55 = self.addLink('s27','h55',**linkHSParameters)
		lhs56 = self.addLink('s28','h56',**linkHSParameters)
		lhs57 = self.addLink('s28','h57',**linkHSParameters)
		lhs58 = self.addLink('s29','h58',**linkHSParameters)
		lhs59 = self.addLink('s29','h59',**linkHSParameters)
		lhs60 = self.addLink('s30','h60',**linkHSParameters)
		lhs61 = self.addLink('s30','h61',**linkHSParameters)
		lhs62 = self.addLink('s31','h62',**linkHSParameters)
		lhs63 = self.addLink('s31','h63',**linkHSParameters)
		lhs64 = self.addLink('s32','h64',**linkHSParameters)
		lhs65 = self.addLink('s32','h65',**linkHSParameters)
		lhs66 = self.addLink('s33','h66',**linkHSParameters)
		lhs67 = self.addLink('s33','h67',**linkHSParameters)
		#Add a link of switches of original topology
		lss0 = self.addLink('s0','s1',**linkSSParameters)
		lss1 = self.addLink('s0','s3',**linkSSParameters)
		lss2 = self.addLink('s1','s2',**linkSSParameters)
		lss3 = self.addLink('s1','s11',**linkSSParameters)
		lss4 = self.addLink('s2','s4',**linkSSParameters)
		lss5 = self.addLink('s3','s4',**linkSSParameters)
		lss6 = self.addLink('s4','s5',**linkSSParameters)
		lss7 = self.addLink('s4','s6',**linkSSParameters)
		lss8 = self.addLink('s5','s24',**linkSSParameters)
		lss9 = self.addLink('s5','s8',**linkSSParameters)
		lss10 = self.addLink('s5','s10',**linkSSParameters)
		lss11 = self.addLink('s5','s9',**linkSSParameters)
		lss12 = self.addLink('s6','s33',**linkSSParameters)
		lss13 = self.addLink('s6','s7',**linkSSParameters)
		lss14 = self.addLink('s7','s8',**linkSSParameters)
		lss15 = self.addLink('s7','s18',**linkSSParameters)
		lss16 = self.addLink('s8','s17',**linkSSParameters)
		lss17 = self.addLink('s8','s33',**linkSSParameters)
		lss18 = self.addLink('s9','s17',**linkSSParameters)
		lss19 = self.addLink('s10','s11',**linkSSParameters)
		lss20 = self.addLink('s11','s12',**linkSSParameters)
		lss21 = self.addLink('s12','s13',**linkSSParameters)
		lss22 = self.addLink('s12','s24',**linkSSParameters)
		lss23 = self.addLink('s12','s25',**linkSSParameters)
		lss24 = self.addLink('s12','s27',**linkSSParameters)
		lss25 = self.addLink('s12','s30',**linkSSParameters)
		lss26 = self.addLink('s13','s14',**linkSSParameters)
		lss27 = self.addLink('s14','s26',**linkSSParameters)
		lss28 = self.addLink('s14','s28',**linkSSParameters)
		lss29 = self.addLink('s15','s16',**linkSSParameters)
		lss30 = self.addLink('s15','s24',**linkSSParameters)
		lss31 = self.addLink('s15','s28',**linkSSParameters)
		lss32 = self.addLink('s16','s18',**linkSSParameters)
		lss33 = self.addLink('s17','s21',**linkSSParameters)
		lss34 = self.addLink('s18','s21',**linkSSParameters)
		lss35 = self.addLink('s19','s21',**linkSSParameters)
		lss36 = self.addLink('s20','s29',**linkSSParameters)
		lss37 = self.addLink('s20','s22',**linkSSParameters)
		lss38 = self.addLink('s21','s23',**linkSSParameters)
		lss39 = self.addLink('s22','s24',**linkSSParameters)
		lss40 = self.addLink('s22','s23',**linkSSParameters)
		lss41 = self.addLink('s23','s24',**linkSSParameters)
		lss42 = self.addLink('s24','s32',**linkSSParameters)
		lss43 = self.addLink('s24','s29',**linkSSParameters)
		lss44 = self.addLink('s25','s26',**linkSSParameters)
		lss45 = self.addLink('s26','s27',**linkSSParameters)
		lss46 = self.addLink('s29','s30',**linkSSParameters)
		lss47 = self.addLink('s30','s31',**linkSSParameters)
		lss48 = self.addLink('s31','s32',**linkSSParameters)
		
topos = { 'Xspedius': ( lambda: MininetNX() ) }