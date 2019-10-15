import os
import json

def main():
	with open('probabilities.json', 'r', encoding='utf-8') as fp:
		prob = json.load(fp)

	file_1 = open("New/cleaned/corpus.csv", "r", encoding='utf-8')

	lines = file_1.readlines()

	for line in lines:
		word = line.split(',')[0]
		try:
			a = 1
			print(word + 'is predicted to be ' + prob[word])
		except:
			prob[word] = "UNKNOWN"
			print('Model needs more training for ' + word)
	
	with open('results.json', 'w') as fp:
		json.dump(prob, fp)

if __name__ == "__main__":
	main()
