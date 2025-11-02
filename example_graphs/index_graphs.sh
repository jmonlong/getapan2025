set -ex

#Make the graphs with the python script
python3 make_graphs.py

for GRAPH in simple_nested_snarl loopy_snarl loopy_chain aaa; do

    vg view -dp ${GRAPH}.hg | dot -Tsvg -o ${GRAPH}.svg

    vg index -j ${GRAPH}.dist ${GRAPH}.hg

    vg deconstruct -a -p ref#0#0 ${GRAPH}.hg >${GRAPH}.deconstruct.vcf

done
