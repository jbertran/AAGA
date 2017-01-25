#!/usr/bin/perl

use strict; 
use warnings;
use v5.14;
use autodie qw( open close );
$| = 1;

use Time::HiRes qw( time );


open my $FPOUT, '>', 'results_cached.csv';

for my $size ( 1 .. 22 ) {
    my $time = time;
    my $i;
    for ($i = 1; $i <= 20; $i++){
	printf "\rIn progress: size = %2d --- try = %2d/20", $size, $i;  
	system("echo $size | python3 projet.py");
	last if (time - $time > 120); # Abort after 120 seconds.
    }
    print "\r", " "x80;
    if ($i < 20) {
	print "\rSize $size, timeout exceeded after $i iterations.\n";
    }
    $time = (time - $time) / $i;
    $time = sprintf"%.3f", $time;
    printf "\rSize = %2d --- mean time = %f\n", $size, $time;
    print $FPOUT "$size;$time;\n";
}

close $FPOUT;
