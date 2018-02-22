# junto-kanto

Code for our paper [A Graph Based Semi-Supervised Approach for Analysis of Derivational Nouns in  Sanskrit](http://aclweb.org/anthology/W17-2409) at [ACL TextGraphs'17](https://sites.google.com/site/textgraphs2017/program). 

## Scripts details

Files written in a tree structure, depending on independent runs are possible
or not.

**hunt_duplicates** - remove duplicate nodes in gold and seeds from the file that has more nodes,
also ensure seeds have same number of L1 and L2

**simplify** - Master script to run junto on each part in each STEP

|---- **simply_copy** - copies label_prop_output and nodes_dict to next part.

|---- **simplify_loop_for2** - run junto on each part of STEP2

|----|---- **graph.py**

|---- **simplify_loop_for3** - run junto on each part of STEP3

|----|---- **graph.py**

|----|---- **merge.py**

**step3_imp_parts** - run static code on STEP3, no junto involved

**code** - Intent not clear. Refer to Harsha about this.

**copy_output** - Redundant script to copy label_prop_output

**count_nodes** - count number of nodes in seeds, gold_labels, total_in_graph which
includes unlabelled nodes. L1 and L2 marked separately. Results saved in `step_x_nodes.csv`

**crosscheck_nodes** - Redundant

**join_csv** - merges 2 result csvs `preiphery/part_i_gold.csv` and `step3/part_i_results.csv` to
generate `periphery/part_i_gold_predict.csv` and `results/periphery_scores.csv`

**result_gen** - # compute precision, recall, and accuracy and generates `results/step_STEPnum_part_partnum.txt`
 and `results/step_STEPnum_part_partnum_results.csv`

|---- **result_important** - run result_gen only on important 5 parts

The other files are relatively easier to understand.

## Script
`
python hunt_duplicates.py &&
python simplify.py
`
* Asks if junto is to compiled before running

* copies a simple_config file to STEP1

* calls *simplify_looper.py* in STEP1 directory , which runs part appropriate codes to generate graphs

*A function juntofy is called which copies the _simple config_  file to each part , and runs
`
junto config simple_config
`

* Return to simplify.py , calls *simply_copy.py* , which copies label_prop_output from STEP1/part i to label_prop_output_step1 in STEP2/part i

* Calls *simplify_looper_for2.py* which runs *graph.py* in STEP2 for each part,followed by juntofy

* simplycopy copies prop_output from STEP2 to STEP3 , and inputgraph from STEP1 and 2 to STEP3

* calls *simplify_looper_for3.py* running *graph.py* and *merge.py* in STEP3 for each of these parts

It takes a total of 20 minutes to run .

## Results

To generate a proper result text file (demo : results/ ), run
```
python result_gen.py
```

It asks 2 parameters , partnum and STEPnum . The generated output file can be viewed at
results/step_STEPnum_part_partnum_.txt

## People involved

* [Gulab Arora](https://in.linkedin.com/in/gulab-arora-b508a9a3)
* [Harshavardhan Ponnada](http://cse.iitkgp.ac.in/~ponnadah/)
* [Kaustubh Hiware](http://kaustubhhiware.github.io)
* [Amrith Krishna](http://www.cnergres.iitkgp.ac.in/amrithk/)
* [Prof. Pawan goyal](http://cse.iitkgp.ac.in/~pawang/)

## LICENSE

Apache License. Have a look at [LICENSE.md](LICENSE.md) for more details.