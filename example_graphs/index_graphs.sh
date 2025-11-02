set -ex

#Make the graphs with the python script
python3 make_graphs.py

for GRAPH in simple_nested_snarl inversion; do

    vg view -dp ${GRAPH}.hg | dot -Tsvg -o ${GRAPH}.svg

    vg deconstruct -a -p ref#0#0 ${GRAPH}.hg >${GRAPH}.deconstruct.vcf

done
