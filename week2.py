import xml.dom.minidom
import os
import json

def main():
	word_dict = {}
	tag_dict = {}
	file_1 = open("week1/" + "corpus" + ".csv", "r")

	lines = file_1.readlines()
	for line in lines:
		word_pair = line.replace("\n", "")
		word_tag = word_pair.split(",")
		word = word_tag[0]
		tag = word_tag[1]

		word_frequency = word_dict.get(word, 0)
		tag_frequency = tag_dict.get(tag, 0)

		word_dict[word] = word_frequency + 1
		tag_dict[tag] = tag_frequency + 1

	print(tag_dict)

	with open('words.json', 'w') as fp:
    		json.dump(word_dict, fp)

	with open('tags.json', 'w') as fp:
    		json.dump(tag_dict, fp)


if __name__ == "__main__":
	main()
