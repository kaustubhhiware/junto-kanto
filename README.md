# junto-kanto
Python files by Harsha and me(corrected some for script suitability)

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

* Update : A video has been added for the running demo

It takes a total of 20 minutes to run .
 
## Results

To generate a proper result text file (demo : results/ ), run
`
python result_gen.py

`

It asks 2 parameters , partnum and STEPnum . The generated output file can be viewed at
results/step_STEPnum_part_partnum_.txt

