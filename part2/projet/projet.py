import math
import random
import functools
from timeit import default_timer as timer

def id_generator():
    """Simple ID generator to differentiate node dictionaries,
    since they need to be unique in order for list.remove() to
    behave correctly
    """
    id = 0
    while True:
        yield id
        id += 1

fact = [math.factorial(i) for i in range(100)]

def g(n) :
    """The non-recursive calculation for the total number of general
    trees of size n
    """
    n -= 1
    if n <= 0 :
        return 1
    product = 1
    for k in range(1, n+1):
        product *= (0.5 - k)
    product *= (-2)**n
    return int(product)

def composition(n, length=None):
    """Return a list of potential compositions with lowest value 1
    totalling n
    """
    result = []
    a = [0 for i in range(n + 1)]
    k = 1
    a[0] = 0
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while 1 <= y:
            a[k] = x
            x = 1
            y -= x
            k += 1
        a[k] = x + y
        if not length or len(a[:k + 1]) == length:
            result.append(a[:k + 1])
    return result

def multinomial(n, coeffs):
    """Multinomial coefficient - n choose coeffs
    n! divided by the product of e! for e in coeffs
    Coeffs HAS to be a tuple
    """
    nfac = fact[n]
    product = 1
    for i in coeffs:
        product *= fact[i]
    return nfac/product

def compo_product(compo, n):
    """Return a composition product
    compo HAS to be a tuple
    """
    total = multinomial(n, compo)
    for i in compo:
        total *= g(i)
    return total


def inner_sum(n, k):
    return sum(map(lambda x: compo_product(x, n), composition(n, length=k)))

def tree_gen_rec(size, id_gen):
    """Recursively form a silhouette of a general tree of given size
    Use generator id_gen to differentiate nodes amongst themselves
    """
    if size == 0:
        raise Exception('You asked for a zero-size general tree.')
    if size == 1:
        return { 'terminal': True, 'tag': -1, 'id': next(id_gen) }
    if size == 2:
        return { 'children': [{'terminal': True, 'tag': -1, 'id': next(id_gen) }], 'tag': -1, 'id': next(id_gen)}

    rand = random.randrange(g(size) - 1)

    k = 1
    while k < size:
        tmp = inner_sum(size-1, k)
        if (rand - tmp > 0):
            rand -= tmp
        else:
            break
        k += 1

    # on a trouvé le k
    # on doit trouver la bonne composition
    compos = composition(size-1, length=k)

    i = 0
    while i < len(compos):
        tmp = compo_product(compos[i], size-1)
        if (rand - tmp > 0):
            rand -= tmp
        else:
            break
        i += 1

    # On a trouvé la composition: compo[i]
    children = [tree_gen_rec(x, id_gen) for x in compos[i]]
    return {'children': children, 'tag': -1, 'id': next(id_gen)}

def tree_gen(size):
    """Handle calls to the recursive silhouette generator, and tag the resulting
    tree silhouette for and increasingly tagged general tree
    """
    id_gen = id_generator()
    tree = tree_gen_rec(size, id_gen)
    tag_tree(tree)
    return tree

def traverse_side_effect(side_effect, tree):
    """Infix tree traversal for functions with side-effects.
    """
    side_effect(tree)
    if 'children' in tree:
        for node in tree['children']:
            traverse_side_effect(side_effect, node)

def dot_gen(tree, fname):
    """Generate the .dot file corresponding to the generated tree using the
    previously defined name generator.
    """
    with open(fname, 'w') as f:
        def output_dot_node(node, out=f):
            if 'children' in node:
                for child in node['children']:
                    out.write(str(node['tag']) + ' -> ' + str(child['tag']) + ';\n')

        f.write('digraph tree {\n')
        traverse_side_effect(output_dot_node, tree)
        f.write('}\n')

def tag_tree(tree):
    """Tag a general tree to make it an increasingly tagged general tree
    A.k.a. your basic prefix run, with a random twist
    """
    root_stack = [tree]
    end_stack = []
    i = 0
    while root_stack:
        e = root_stack[random.randrange(len(root_stack))]
        root_stack.remove(e)
        end_stack.append(e)
        i += 1
        if 'children' in e:
            root_stack += e['children']
    i = 1
    for e in end_stack:
        e['tag'] = i
        i+= 1

def tree_size(tree):
    """The size of given general tree, which may only contain terminal nodes
    and inner nodes with children
    """
    if not tree: return 0
    if 'terminal' in tree: return 1
    if 'children' in tree:
        return 1 + sum([tree_size(x) for x in tree['children']])

def tree_max_depth(tree):
    """The max depth of given general tree
    """
    if not tree: return 0
    if 'terminal' in tree: return 1
    if 'children' in tree:
        return 1 + max([tree_max_depth(x) for x in tree['children']])

def tree_avg_children(tree):
    def node_children(tree):
        if not tree: return 0
        if 'terminal' in tree: return 0
        if 'children' in tree:
            return sum([avg_node_children(i) for i in tree['children']]) + len(tree['children'])

    def inner_nodes_not_terminal(tree):
        if not tree: return 0
        if 'terminal' in tree: return 0
        if 'children' in tree: return 1 + sum([inner_nodes_not_terminal(i) for i in tree['children']])

    return node_children(tree) / float(inner_nodes_not_terminal(tree))

def nb_node_tree(tree):
    if not tree: return 0
    if 'terminal' in tree: return 1
    if 'children' in tree:
        return sum([nb_node_tree(i) for i in tree['children']]) + 1


def tree_avg_node_depth(tree):
    def tree_depth_sum(tree, depth = 0):
        if not tree: return 0
        if 'terminal' in tree: return depth
        if 'children' in tree: return depth + sum([tree_depth_sum(i, depth+1) for i in tree['children']])
    return tree_depth_sum(tree) / float(nb_node_tree(tree))

def printret(text):
    print(text, end="\r")

def generate_data(sample_size):
    max_tree_size = 30
    time = {}
    tree_tab = {}

    with open('data/time.csv', 'w') as f:
        for size in range(1, max_tree_size + 1):
            i = 1
            start = timer()
            tree_tab[size] = []
            times = []
            while i <= sample_size:
                printret("Generating size %d tree %d/%d" % (size, i, sample_size))
                tree = tree_gen(size)
                tree_tab[size].append(tree)
                if not time.get('size'):
                    time[size] = [(timer() - start) / float(i)]
                else:
                    time[size].append((timer() - start) / float(i))
                if (timer() - start >= 120):
                    print("Timeout, abandoning size %d" % size)
                    break
                i += 1
            f.write('%d, %.5f\n' % (size, sum(time[size])/float(len(time[size]))))

    with open('data/avg_depth.csv', 'w') as f:
        for size, trees in tree_tab.items():
            f.write('%d, %.5f\n' % (size, sum(map(lambda x: tree_max_depth(x), trees))/len(trees)))

    with open('data/tree_avg_children.csv', 'w') as f:
        for size, trees in tree_tab.items():
            f.write('%d, %.5f\n' % (size, sum(map(lambda x: tree_max_depth(x), trees))/len(trees)))

    with open('data/tree_avg_node_depth.csv', 'w') as f:
        for size, trees in tree_tab.items():
            f.write('%d, %.5f\n' % (size, sum(map(lambda x: tree_avg_node_depth(x), trees))/len(trees)))

if __name__ == '__main__':
    size = int(input())
    while size > 25 or size < 0:
        print("In the interest of time, we recommend generating a tree of size [10..20]")
        size = int(input())
    tree = tree_gen(size)
    dot_gen(tree, "tree.dot")
    print("Tree of size %d generated in 'tree.dot'" % size)
