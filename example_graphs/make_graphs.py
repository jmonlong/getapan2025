import bdsg

from bdsg.bdsg import HashGraph


def make_simple_nested_snarl():
    #                       5 
    #                     /   \ 
    #            1       4 ----6------- 
    #          /   \   /         \      \
    #        0       3  ----------7------8
    #          \   /
    #            2
    
    graph = HashGraph()
    seqs = ["AGGAT", "GGCAC", "CTTAG", "AAGTC", "CGGTA", "ACTAC", "CGTCA", "CCAGG", "TGATG"]
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
    graph.create_edge(nodes[6], nodes[8]);
    graph.create_edge(nodes[7], nodes[8]);
    
    path_seqs = [ ("ref#0#0", [0, 1, 3, 7, 8]), 
                   ("sample1#1#0#0", [0, 1, 3, 4, 5, 6, 7, 8]), 
                   ("sample1#2#0#0", [0, 2, 3, 4, 6, 8])]
    paths = [];
    
    for path_i in range(len(path_seqs)):
        paths.append(graph.create_path_handle(path_seqs[path_i][0]));
        for node_i in path_seqs[path_i][1]:
            graph.append_step(paths[-1], nodes[node_i]);
    
    
    graph.serialize("simple_nested_snarl.hg")


def make_loopy_chain():
    #                    2
    #                 /    \
    #             ----1      4---
    #           /      \   /     \
    #          /         3        \
    #         /                    \
    #        0----------------------5
    
    graph = HashGraph()
    seqs = ["AGGAT", "GGCAC", "CTTAG", "AAGTC", "CGGTAGCTTAGCATCAG", "GTACG"]
    nodes = []
    for s in seqs:
        nodes.append(graph.create_handle(s))
    
    graph.create_edge(nodes[0], nodes[1]);
    graph.create_edge(nodes[0], nodes[5]);
    graph.create_edge(nodes[1], nodes[2]);
    graph.create_edge(nodes[1], nodes[3]);
    graph.create_edge(nodes[2], nodes[4]);
    graph.create_edge(nodes[3], nodes[4]);
    graph.create_edge(nodes[4], nodes[5]);
    
    path_seqs = [ ("ref#0#0", [0, 1, 2, 4, 5]), 
                   ("sample1#1#0#0", [0, 1, 2, 4, 5]), 
                   ("sample1#2#0#0", [0, 1, 2, 4, 5]), 
                   ("sample2#1#0#0", [0, 1, 3, 4, 5]), 
                   ("sample2#2#0#0", [0, 5])]
    paths = [];
    
    for path_i in range(len(path_seqs)):
        paths.append(graph.create_path_handle(path_seqs[path_i][0]));
        for node_i in path_seqs[path_i][1]: graph.append_step(paths[-1], nodes[node_i]);
    
    
    graph.serialize("loopy_chain.hg")

def make_loopy_chain_flanked():
    #                    2
    #                 /    \
    #             ----1      4---
    #           /      \   /     \
    #          /         3        \
    #         /                    \
    #        0----------------------5
    
    graph = HashGraph()
    seqs = ["AGAGCGAGSACGA", "GGCAC", "CTTAG", "AAGTC", "CGGTAGCTTAGCATCAG", "ACGACTGAGCTGTACGATCGACT"]
    nodes = []
    for s in seqs:
        nodes.append(graph.create_handle(s))
    
    graph.create_edge(nodes[0], nodes[1]);
    graph.create_edge(nodes[0], nodes[5]);
    graph.create_edge(nodes[1], nodes[2]);
    graph.create_edge(nodes[1], nodes[3]);
    graph.create_edge(nodes[2], nodes[4]);
    graph.create_edge(nodes[3], nodes[4]);
    graph.create_edge(nodes[4], nodes[5]);
    
    path_seqs = [ ("ref#0#0", [0, 1, 2, 4, 5]), 
                   ("sample1#1#0#0", [0, 1, 2, 4, 5]), 
                   ("sample1#2#0#0", [0, 1, 2, 4, 5]), 
                   ("sample2#1#0#0", [0, 1, 3, 4, 5]), 
                   ("sample2#2#0#0", [0, 5])]
    paths = [];
    
    for path_i in range(len(path_seqs)):
        paths.append(graph.create_path_handle(path_seqs[path_i][0]));
        for node_i in path_seqs[path_i][1]: graph.append_step(paths[-1], nodes[node_i]);
    
    
    graph.serialize("loopy_chain_flanked.hg")

def make_loopy_snarl():
    #                  2
    #                /    \
    #           0----1      4---5
    #                 \   /     
    #                   3        

    graph = HashGraph()
    seqs = ["TACCG", "AGGAT", "GGCAC", "CTTAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "AAGTC", "GCAC"]
    nodes = []
    for s in seqs:
        nodes.append(graph.create_handle(s))
    
    graph.create_edge(nodes[0], nodes[1]);
    graph.create_edge(nodes[1], nodes[2]);
    graph.create_edge(nodes[1], nodes[3]);
    graph.create_edge(nodes[2], nodes[4]);
    graph.create_edge(nodes[3], nodes[4]);
    graph.create_edge(nodes[4], nodes[5]);
    
    path_seqs = [ ("ref#0#0", [0, 1, 3, 4, 5]), 
                   ("sample1#1#0#0", [0, 1, 2, 4, 5]), 
                   ("sample1#2#0#0", [0, 1, 3, 4, 5])]
    paths = [];
    
    for path_i in range(len(path_seqs)):
        paths.append(graph.create_path_handle(path_seqs[path_i][0]));
        for node_i in path_seqs[path_i][1]: graph.append_step(paths[-1], nodes[node_i]);
    
    
    graph.serialize("loopy_snarl.hg")



def make_aaa():
    #          -1---2---3---4---5
    #         /                  \
    #        0------------------  6
    
    graph = HashGraph()
    seqs = ["AAAAAAAAAA", "A", "A", "A", "A", "A", "AAAAAAAAAAAAAAA"]
    nodes = []
    for s in seqs:
        nodes.append(graph.create_handle(s))
    
    graph.create_edge(nodes[0], nodes[1]);
    graph.create_edge(nodes[0], nodes[2]);
    graph.create_edge(nodes[0], nodes[3]);
    graph.create_edge(nodes[0], nodes[4]);
    graph.create_edge(nodes[0], nodes[5]);
    graph.create_edge(nodes[0], nodes[6]);
    graph.create_edge(nodes[1], nodes[2]);
    graph.create_edge(nodes[2], nodes[3]);
    graph.create_edge(nodes[3], nodes[4]);
    graph.create_edge(nodes[4], nodes[5]);
    graph.create_edge(nodes[5], nodes[6]);
    
    path_seqs = [ ("ref#0#0", [0, 4, 5, 6]), 
                   ("sample1#1#0#0", [0, 1, 2, 3, 4, 5, 6]), 
                   ("sample1#2#0#0", [0, 3, 4, 5, 6])] 
    paths = [];
    
    for path_i in range(len(path_seqs)):
        paths.append(graph.create_path_handle(path_seqs[path_i][0]));
        for node_i in path_seqs[path_i][1]: graph.append_step(paths[-1], nodes[node_i]);
    
    
    graph.serialize("aaa.hg")




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
make_loopy_chain()
make_loopy_chain_flanked()
make_loopy_snarl()
make_aaa()
