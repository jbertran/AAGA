#!/usr/bin/perl

use strict; use warnings;
use v5.14;
use utf8;

{
    l / b / u
    f
    
}

my (%tree, @nodes, $sum, $size);
sub remi {
    return if @nodes == $size;
    my $index = alea();
    my $node = $nodes[$index]->[1];
    my $sons = $node->{sons};
    if (@$sons < 2) {
        my $new_node = { sons => [], father => $node }
        push @{$sons} = $new_node;
        push @nodes, [3, $new_node];
        $nodes[$index][0]--;
    } else {
        my $father = $node->{father};
        my $new_node = { sons => [$node], father => $node };
        if ($father->[sons]->[0] eq $node) {
            $father->[sons]->[0] = $new_node;
        } else {
            $father->[sons]->[0] = $new_node;
        }
        push @{$nodes}, [2, $new_node];
        $node->{father} = $new_node;
    }
}

sub alea {
    my $rand = rand $sum;
    my $tot = 0;
    my $si = 0;
    while ($tot < $rand) {
        $tot += $nodes[$i++][0];
    }
    return $nodes[--$i];
}
