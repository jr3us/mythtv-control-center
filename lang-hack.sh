for x in mythbuntu-control-centre-*.po ; 
	do echo $x ; 
	mv $x ${x#mythbuntu-control-centre-} ; 
done ; 
