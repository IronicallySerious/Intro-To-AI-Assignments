import os
import json

def print_probability(dictionary):
	prob = {}
	for word in dictionary:
		word_tags = dictionary[word]

		sorted_tags = sorted(word_tags)

		# tag -> tag frequency
		tag_frequency = {}
		for tag in list(sorted(set(sorted_tags))):
			tag_frequency[tag] = sorted_tags.count(tag)

		total_tag_count = 0
		for tag in tag_frequency:
			total_tag_count = total_tag_count + tag_frequency[tag]
		max_frequency = 0
		for tag in tag_frequency:
			print("Probability of '" + word + "' as a " + tag + " is " + str(tag_frequency[tag] / total_tag_count * 100) + "%")
			if max_frequency < tag_frequency[tag]: max_frequency = tag_frequency[tag]
		prob[word] = tag

	with open('probabilities.json', 'w') as fp:
		json.dump(prob, fp)

def main():
	# file_1 = open("week1/corpus.csv", "r")

	# lines = file_1.readlines()

	# # word -> [tags]
	# dictionary = {}
	# for line in lines:

	# 	word_pair = line.replace("\n", "")
	# 	word_tag = word_pair.split(",")
	# 	word = word_tag[0]
	# 	tag = word_tag[1]

	# 	if dictionary.get(word) == None:
	# 		dictionary[word] = []

	# 	dictionary[word].append(tag)

	with open('new_pairs.json', 'r') as fp:
		dictionary = json.load(fp)

	print_probability(dictionary)

if __name__ == "__main__":
	main()
