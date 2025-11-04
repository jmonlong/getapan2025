```
source ~/Documents/repo/libbdsg/venv/bin/activate

python3 make_graphs.py

snakemake -p --cores 4 -n

GRAPH=aaa
GRAPH=loopy_chain
GRAPH=loopy_snarl
GRAPH=simple_nested_snarl

python3 ~/Documents/repo/daggi/daggi-tree.py --hash_graph ${GRAPH}.hg --distance_index ${GRAPH}.dist --output_prefix ${GRAPH}.snarltree


GRAPH=loopy_chain
vg index -j ${GRAPH}.w1.dist -w 6 ${GRAPH}.hg
python3 ~/Documents/repo/daggi/daggi-tree.py --hash_graph ${GRAPH}.hg --distance_index ${GRAPH}.w1.dist --output_prefix ${GRAPH}.w1.snarltree


```
