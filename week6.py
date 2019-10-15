import os
import json

def main():
	with open('results.json', 'r', encoding='utf-8') as fp:
		results = json.load(fp)

	file_1 = open("New/cleaned/corpus.csv", "r", encoding='utf-8')

	lines = file_1.readlines()

	tp = 0
	fp = 0
	tn = 0
	fn = 0

	print(results)

	for line in lines:
		word = line.split(',')[0]
		tag = line.split(',')[1]
		try:
			if results[word] == tag: tp = tp + 1
			elif results[word] != tag: fp = fp + 1
		except:
			print('Model needs more training for ' + word)

	print("TP = " + tp.__str__() + " FP = " + fp.__str__())
	
if __name__ == "__main__":
	main()
