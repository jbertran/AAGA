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

sub n_cube {
    my ($b,$c) = @_;
    return sub {
	my ($x) = @_;
	my $val = ($x**3+$b)/($x/$c)/10;
	$val += 0.1 * $rand_factor * rand($val) * (rand(1)>0.5?1:-1);
	return sec $val;
    }
}


my $SMIS    = affine(1,1,2);
my $rand    = affine(10,1,2);
my $local   = n_cube(3,1.05);
my $steiner = n_cube(3,1.7);

open my $FPOUT, '>', 'temps_calcul.in' or die $!;
printf $FPOUT "%s %s %s %s %s\n", qw(size SMIS rand localSearch Steiner);
for ($_ = 800; $_ <= 2000; $_+=100) {
    printf $FPOUT "%s %s %s %s %s\n", $_, $SMIS->($_), $rand->($_), $local->($_), $steiner->($_);
}
close $FPOUT;


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

open $FPOUT, '>', 'tailles.in' or die $!;
printf $FPOUT "%s %s %s %s %s\n", qw(size SMIS rand localSearch Steiner);
for ($_ = 800; $_ <= 2000; $_+=100) {
    my $r1 = size_SMIS($_);
    printf $FPOUT "%s %s %s %s %s\n", $_, $r1, randomize($r1), size_SMIS($_/1.4), size_SMIS($_/1.2);
}
close $FPOUT;
