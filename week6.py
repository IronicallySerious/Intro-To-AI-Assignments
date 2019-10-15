import os
import json

def most_frequent(List): 
    return max(set(List), key = List.count)

def main():
	with open('train_pairs.json', 'r', encoding='utf-8') as fp:
		results = json.load(fp)

	with open('test_pairs.json', 'r', encoding='utf-8') as fp:
		test = json.load(fp)

	tp = 0
	fp = 0
	tn = 0
	fn = 0

	for word in test.keys():
		tag = test[word]
		if tag == "": continue
		try:
			if results[word] == tag:
				tp = tp + 1
				fp = fp + 0
				tn = tn + len(tags) - 1
				fn = fn + 0
			elif results[word] != tag:
				print("We predicted " + results[word] + "for " + tag)
				tp = tp
				fp = fp + 1
				tn = tn
				fn = fn + len(tags) - 1
		except:
			print('Model needs more training for ' + word)

	print("TP = " + tp.__str__() + " FP = " + fp.__str__())
	print("TN = " + tn.__str__() + " FN = " + fn.__str__())
	
if __name__ == "__main__":
	main()
