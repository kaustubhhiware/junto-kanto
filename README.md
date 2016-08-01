# junto-kanto
Python files by Harsha and me(corrected some for script suitability)

## Script
`
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

Current status :  for some reason , junto generated output file in Step 1 in my laptop and Harsha's laptop are different , due to which this fails in my laptop.

* Update : copy_output.py copies all label_prop_output in STEP1 to no_gold or 
with_gold as per arguments
 
 

