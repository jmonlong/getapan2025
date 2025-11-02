import bdsg

from bdsg.bdsg import HashGraph


def make_simple_nested_snarl():
    #                       5         9
    #                     /   \      /  \
    #            1       4 ----6    8---10
    #          /   \   /         \ /     \
    #        0       3  ----------7-------11
    #          \   /
    #            2
    
    graph = HashGraph()
    seqs = ["AGGAT", "GGCAC", "CTTAG", "AAGTC", "CGGTA", "G", "A", "GGTAC", "TGCGA", "TCATG", "GGGTG", "ATCAG"]
    nodes = []
    for s in seqs:
        nodes.append(graph.create_handle(s))
    
    graph.create_edge(nodes[0], nodes[1]);
    graph.create_edge(nodes[0], nodes[2]);
    graph.create_edge(nodes[1], nodes[3]);
    graph.create_edge(nodes[2], nodes[3]);
    graph.create_edge(nodes[3], nodes[4]);
    graph.create_edge(nodes[3], nodes[7]);
    graph.create_edge(nodes[4], nodes[5]);
    graph.create_edge(nodes[4], nodes[6]);
    graph.create_edge(nodes[5], nodes[6]);
    graph.create_edge(nodes[6], nodes[7]);
    graph.create_edge(nodes[7], nodes[8]);
    graph.create_edge(nodes[7], nodes[11]);
    graph.create_edge(nodes[8], nodes[9]);
    graph.create_edge(nodes[8], nodes[10]);
    graph.create_edge(nodes[9], nodes[10]);
    graph.create_edge(nodes[10], nodes[11]);
    
    path_seqs = [ ("ref#0#0", [0, 1, 3, 7, 8, 9, 10, 11]), 
                   ("sample1#1#0#0", [0, 1, 3, 4, 5, 6, 7, 8, 10, 11]), 
                   ("sample1#2#0#0", [0, 2, 3, 7, 11])]
    paths = [];
    
    for path_i in range(len(path_seqs)):
        paths.append(graph.create_path_handle(path_seqs[path_i][0]));
        for node_i in path_seqs[path_i][1]:
            graph.append_step(paths[-1], nodes[node_i]);
    
    
    graph.serialize("simple_nested_snarl.hg")


def make_inversion():
    #            1      -------     6
    #          /   \   /     /    /   \ 
    #        0       3  ---4----5------7
    #          \   /      /    /
    #            2        -----
    
    graph = HashGraph()
    seqs = ["AGGAT", "G", "C", "AGATC", "CGGTA", "CCATG", "ACAGCA", "TACAG"]
    nodes = []
    for s in seqs:
        nodes.append(graph.create_handle(s))
    
    graph.create_edge(nodes[0], nodes[1]);
    graph.create_edge(nodes[0], nodes[2]);
    graph.create_edge(nodes[1], nodes[3]);
    graph.create_edge(nodes[2], nodes[3]);
    graph.create_edge(nodes[3], nodes[4]);
    graph.create_edge(nodes[3], graph.flip(nodes[4]));
    graph.create_edge(nodes[4], nodes[5]);
    graph.create_edge(graph.flip(nodes[4]), nodes[5]);
    graph.create_edge(nodes[5], nodes[6]);
    graph.create_edge(nodes[5], nodes[7]);
    graph.create_edge(nodes[6], nodes[7]);
    
    path_seqs = [ ("ref#0#0", [0, 1, 3, 4, 5, 7]), 
                   ("sample1#1#0#0", [0, 2, 3, 4, 5, 6, 7]), 
                   ("sample1#2#0#0", [0, 2, 3, 4, 5, 7])] #Flip 4
    paths = [];
    
    for path_i in range(len(path_seqs)):
        paths.append(graph.create_path_handle(path_seqs[path_i][0]));
        for node_i in path_seqs[path_i][1]:
            if path_i == 2 and node_i == 4:
                graph.append_step(paths[-1], graph.flip(nodes[node_i]));
            else:
                graph.append_step(paths[-1], nodes[node_i]);
    
    
    graph.serialize("inversion.hg")

make_simple_nested_snarl()
make_inversion()
