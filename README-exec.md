
ALL FILES ARE IN PYTHON2.

Each part contains 3 folders-> Step1,Step2,Step3
1_graph.py has the code for generating input_graph and seeds for Step1

In 1_graph.py, we reduced unlabelled nodes to 50% by this command

    if random.randrange(0,2) == 0:
        continue
    source = each

For generating gold we have written the parameters in final.py.. and automate.py in function main(n)

    if n==23:
        gen_gold(n,100,100,50,30)
    else:
        gen_gold(n,100,100,50,50)

    gen_gold(n,tot1,tot2,gol1,gol2)
    # means out of total labelled L1 nodes in part n gol1 nodes go to
    # gold_labels & out of totl labelled L2 nodes in part n gol2 nodes go to
    # gold_labels

2_graph.py and 3_graph.py are common for all

corresponding edge_weights.txt and part_partno_algo_file.txt should be copied in part<partno.>/step2 and part<partno.> respectively


For automation :
	you can use automate.py(just change the part for which main should be called)
	you can also use final.py

For results :
	you can use individual_results.py(just change the part for which main should be called)
	you can also use final.py

---

For Detailed results:

Running result_important.py simply runs for all parts, step3.

Running result_gen.py will work for particular part. Using prettytable, we generate the results and output parameters
 like precision, recall and accuracy which can be found in results/ folder. Additionally, a csv is also generated for the same.
Only input value needed is part number (2, 15, 23, 26 ,29).
