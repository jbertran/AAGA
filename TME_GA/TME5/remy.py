import math
from random import randint

node = {
    'prob': 1,
    'father': None,
    'children': [None, None]

}


def alea(sum_nodes, nodelist):
    r = randint(sum_nodes)
    tot = 0
    idx = 0
    while tot < r:
        tot += nodelist[idx]['prob']
        idx += 1
    return nodelist[idx-1]

def remi(tree_size):
    nodelist = [{'type': 'leaf', 'prob': 3, 'father': None}]
    sum_nodes = 3

    while len(nodelist) < tree_size:
        node = alea(sum_nodes, nodelist)
        father = node['father']

        # LEAF
        if len(node['children']) == 0:
            new_node = {'prob': 3,
                        'father': None,
                        'children': [None, None]}
            strat = randint(3)
            if strat == 2: # TODO
                side = randint(2)
                node['father'] = new_node
                new_node['children'][side] = node
                new_node['father'] = node['father']
            else:
                node['children'][strat] = new_node
                nodelist.append(new_node)
                node['prob'] = 2
                sum_node += 2
        # UNARY
        if len(node['children']) == 1:
            new_node = {'prob': 3,
                        'father': None,
                        'children': [None, None]}
            strat = randint(2)
            if strat == 0:                             # Add the second son
                side = 1 if node['children'][0] else 0
                node['children'][side] = new_node
            else:                                      # Add a node above
                
            nodelist.append(new_node)
            sum_nodes += 2
        # BINARY
