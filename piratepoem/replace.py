import sys
for line in sys.stdin:
	line = line.strip()
	line = line.replace("swagger", " currency-counting machines ")
	line = line.replace(" flies ", " sails ")
	line = line.replace(" black flag", " Maritime Security Patrol Area ")
	line = line.replace("On a", "On his")
	line = line.replace(" whalebone ", " exploited marine stock's ")
	line = line.replace(" staff.", " behalf")
	line = line.replace(" eye", " Kalashnikov ")
	line = line.replace("ring ", "diamond ring ")
	line = line.replace("cannon ", "semi-automatic pistol ")
	line = line.replace("cutlass ", "hand grenade ")
	line = line.replace("cannon's ", "AK47's ")
	line = line.replace(" strong", " hostages")
	line = line.replace(" lost", " hijaked ")
	line = line.replace(" gold,", " millions of dollars, ")
	line = line.replace(" bold.", " a brawler, ")
	line = line.replace("buccaneer,", "burcad badeed,")
	line = line.replace("East Carolina", "Norther Somalia ")
	line = line.replace("and gold!", "toll ")
	line = line.replace("his purple", "the Gulf of Aden's")

	print line
