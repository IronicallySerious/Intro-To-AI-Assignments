import os
import json

def most_frequent(List): 
    return max(set(List), key = List.count)

def main():
	file_1 = open("New/cleaned/corpus.csv", "r", encoding='utf-8')
	# myPath = "./New/Train-corpus/Cleaned_files/"
	myPath = "./New/Test-corpus/Cleaned_files/"
	onlyfiles = [f for f in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, f))]

	pairs = {}
	for file in onlyfiles:
		opened_file = open(os.path.join(myPath, file), "r", encoding='utf-8')
		lines = opened_file.readlines()

		for line in lines:
			array = line.split(" ")
			for pair in array:
				if pair.find("_") == -1: continue 
				word = pair.split("_")[0]
				tag = pair.split("_")[1]
				try:
					pairs[word].append(tag)
				except:
					pairs[word] = []

	for word in pairs.keys():
		if pairs[word] == []: continue
		tag = most_frequent(pairs[word])
		pairs[word] = tag

	# with open('train_pairs.json', 'w') as fp:
	# 	json.dump(pairs, fp)
	with open('test_pairs.json', 'w') as fp:
		json.dump(pairs, fp)

	lines = file_1.readlines()

	
	
if __name__ == "__main__":
	main()
