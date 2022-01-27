from glob import glob
import os
def cupper(test_str):
 return any(ele.isupper() for ele in test_str)
for folder in glob("*/"):
	for file in glob(folder+"*.png"):
		if cupper(file):
			if not os.path.isfile(file.lower()):
				os.rename(file, file.lower())
			else:
				os.rename(file, file.lower().replace(".png", "0.png"))