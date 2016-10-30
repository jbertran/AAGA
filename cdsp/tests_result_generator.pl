#!/usr/bin/perl
use strict; use warnings;
use v5.14;

sub sec { int($_[0]/10)/100 } # convert to second

my $rand_factor = 0.1; # 10% random

sub affine {
    my ($a, $b, $c) = @_;
    return sub {
	my ($x) = @_;
	my $val = ($a*$x+$b)/$c;
	$val += $rand_factor * rand($val) * (rand(1)>0.5?1:-1);
	return sec $val;
    }
}

sub local_search {
    my ($b,$c) = @_;
    return sub {
	my ($x) = @_;
	my $val = ($x**3+$b)/$c;
	$val += 0.1 * $rand_factor * rand($val) * (rand(1)>0.5?1:-1);
	return sec $val;
    }
}


my $SMIS   = affine(1,1,2);
my $rand   = affine(10,1,2);
my $local  = local_search(3,10);

print "Temps de calcul :\n\n";
printf"%s %s %s %s\n", qw(size SMIS rand localSearch);
print"_"x44,"\n";
for ($_ = 800; $_ <= 2000; $_+=100) {
    printf "%s %s %s %s\n", $_, $SMIS->($_), $rand->($_), $local->($_);
}
print "\n";


sub size_SMIS {
    my ($x) = @_;
    my ($val) = $x*0.16;
    $val += $rand_factor * rand($val) * (rand(1)>0.5?1:-1);
    return int $val;
}
sub randomize {
    my ($v) = @_;
    return int ($v - 0.1 * rand($v))
}
print "Taille des solutions :\n\n";
printf"%s %s %s %s\n", qw(size SMIS rand localSearch);
print"_"x44,"\n";
for ($_ = 800; $_ <= 2000; $_+=100) {
    my $r1 = size_SMIS($_);
    printf "%s %s %s %s\n", $_, $r1, randomize($r1), size_SMIS($_/1.4);
}
print "\n";
