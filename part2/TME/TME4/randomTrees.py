#!/usr/bin/python3

import math
import time
import random as rnd
import argparse as ap

# example node
node = {
    'tag': 1,
    'prob': 1,
    'father': None,
    'children': [None, None]
}


def alea(sum_nodes, nodelist):
    """Return a random node within nodelist according to sum_nodes
    """
    r = rnd.randrange(sum_nodes)
    tot = 0
    idx = 0
    while tot < r:
        tot += nodelist[idx]['prob']
        idx += 1
    return nodelist[idx-1]

def node_arity(node):
    """Return how many non-null children the node has
    """
    l, r = node['children']
    return 2 if l and r else 1 if l or r else 0

def node_father_idx(node):
    """Return a node's position in its father's list
    """
    children = node['father']['children']
    if children[0] is None or children[0].get('tag') != node['tag']:
        return 1
    else:
        return 0

def tree_size(tree):
    if tree is not None:
        l = 0
        if tree['children'][0] is not None:
            l = tree_size(tree['children'][0])
        r = 0
        if tree['children'][1] is not None:
            r = tree_size(tree['children'][1])
        return 1 + l + r
    else:
        return 0

def remy(n):
    ng = name_gen()
    tree_root = {'tag': next(ng),
                 'prob': 3,
                 'father': None,
                 'children': [None, None]}
    nodelist = [tree_root]
    sum_nodes = 3
    sum_bits = 0

    while len(nodelist) < n:

        node = alea(sum_nodes, nodelist)
        sum_bits += math.ceil(math.log(len(nodelist), 2))
        new_node = None

        # LEAF
        if node_arity(node) == 0:
            new_node = {'tag': next(ng),
                        'prob': 3,
                        'father': None,
                        'children': [None, None]}
            strat = rnd.randrange(3)
            sum_bits += 2
            if strat == 2:                             # New node one level above
                if node['father'] is None:
                    tree_root = new_node
                else:
                    idx = node_father_idx(node)
                    node['father']['children'][idx] = new_node
                side = rnd.randrange(2)
                sum_bits += 1
                new_node['prob'] = 2
                new_node['children'][side] = node
                new_node['father'] = node['father']
                node['father'] = new_node
            else:                                      # Node goes in a child
                new_node['father'] = node
                node['children'][strat] = new_node
                node['prob'] = 2

        # UNARY
        elif node_arity(node) == 1:
            new_node = {'tag': next(ng),
                        'prob': 3,
                        'father': None,
                        'children': [None, None]}
            strat = rnd.randrange(2)
            sum_bits += 1
            if strat == 0:                             # Add the second child
                side = 1 if node['children'][0] is not None else 0
                new_node['father'] = node
                node['children'][side] = new_node
                node['prob'] = 1
            else:                                      # New node one level above
                if node['father'] is None:
                    tree_root = new_node
                else:
                    idx = node_father_idx(node)
                    node['father']['children'][idx] = new_node
                side = rnd.randrange(2)
                sum_bits += 1
                new_node['children'][side] = node
                new_node['father'] = node['father']
                node['father'] = new_node
                new_node['prob'] = 2

        # BINARY
        else:                                          # New node one level above
            new_node = {'tag': next(ng),
                        'prob': 2,
                        'father': None,
                        'children': [None, None]}
            if node['father'] is None:
                tree_root = new_node
            else:
                idx = node_father_idx(node)
                node['father']['children'][idx] = new_node
            side = rnd.randrange(2)
            sum_bits += 1
            new_node['children'][side] = node
            new_node['father'] = node['father']
            node['father'] = new_node

        nodelist.append(new_node)
        sum_nodes += 2

    return tree_root, sum_bits

def name_gen():
    """Name generator, mostly to tag nodes with a unique identifier
    """
    count = 1
    while True:
        yield str(count)
        count += 1

def traverse_side_effect(side_effect, tree):
    """Infix tree traversal for functions with side-effects.
    """
    if tree is not None:
        traverse_side_effect(side_effect, tree['children'][0])
        side_effect(tree)
        traverse_side_effect(side_effect, tree['children'][1])

def gen_dot(tree, fname):
    """Generate the .dot file corresponding to the generated tree using the
    previously defined name generator.
    """

    with open(fname, 'w') as f:
        def output_dot_node(node, out=f):
            if node['children'][0] is not None:
                f.write(node['tag'] + ' -> ' + node['children'][0]['tag'] + ';\n')
            if node['children'][1] is not None:
                f.write(node['tag'] + ' -> ' + node['children'][1]['tag'] + ';\n')
        f.write('digraph tree {\n')
        traverse_side_effect(output_dot_node, tree)
        f.write('}\n')

def tests():
    pass

if __name__ == '__main__':
    rnd.seed()

    parser = ap.ArgumentParser()
    parser.add_argument('-g', type=int, help='Generate a tree with specified size')
    parser.add_argument('-o', type=str, help='Output the generated .dot to specified file')
    parser.add_argument('--benchbits', action='store_true', help="Benchmark the algorithm's random bit usage")
    parser.add_argument('--benchtime', action='store_true', help="Benchmark the algorithm's time complexity")

    args = parser.parse_args()

    fname = 'tree.dot'
    size = 500
    samplesize = [i for i in range(100, 2000, 100)]

    if args.g is not None:
        size = args.g
    if args.o is not None:
        fname = args.o

    if args.benchbits:
        with open('bits_samples.dat', 'w') as f:
            for size in samplesize:
                print('Generating ' + str(size))
                for it in range(10):
                    _, bits = remy(size)
                    f.write(str(size) + ' ' + str(bits) + '\n')

    elif args.benchtime:
        with open('time_samples.dat', 'w') as f:
            for size in samplesize:
                print('Generating ' + str(size))
                for it in range(10):
                    tprev = time.time()
                    remy(size)
                    t = time.time() - tprev
                    f.write(str(size) + ' ' + str(t) + '\n')

    else:
        tree, _ = remy(size)
        gen_dot(tree, fname)
