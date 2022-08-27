file=("priyanka - shimla"
"neela - delhi"
"sashi - jaipur"
"sarika - delhi"
"deepti - shimla"
"harshad - delhi"
"trishna - delhi"
"pradeep - jaipur"
"sekhar - delhi"
"nand - delhi"
"anoop - delhi"
"balwinder - jaipur")
my_file = open("people1.txt","w")
for names in file:
    (my_file.write(names))