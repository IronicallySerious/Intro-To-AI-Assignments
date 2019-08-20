import xml.dom.minidom
import os

def main():
	myPath = "./Train-corpus/"
	onlyfiles = [f for f in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, f))]

	dictionary = {}
	for file in onlyfiles:
		file_1 = open("week1/" + file + ".csv", "r")

		lines = file_1.readlines()
		for line in lines:
			line_count = lines.count(line)
			word_pair = line.replace("\n", "")
			dictionary[word_pair] = line_count

		print(dictionary)

		file_1.close()

if __name__ == "__main__":
	main()
