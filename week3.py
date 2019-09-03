import xml.dom.minidom
import os
import json

def main():
    with open('words.json', 'r') as fp:
        word_dict = json.load(fp)

    s = [(k, word_dict[k]) for k in sorted(word_dict, key = word_dict.get, reverse = True)]

    print(s[:10])

    with open('tags.json', 'r') as fp:
        tag_dict = json.load(fp)

    s = [(k, tag_dict[k]) for k in sorted(tag_dict, key = tag_dict.get, reverse = True)]

    print(s[:10])

if __name__ == "__main__":
	main()
