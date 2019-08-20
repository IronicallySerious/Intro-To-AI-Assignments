import xml.dom.minidom
import os

def main():
	myPath = "./Train-corpus/"
	onlyfiles = [f for f in os.listdir(myPath) if os.path.isfile(os.path.join(myPath, f))]
	for file in onlyfiles:
		dom = xml.dom.minidom.parse(myPath + file)
		words = dom.getElementsByTagName("w")
		file_1 = open("week1/" + file + ".csv", "w+")

		for word in words:
			attributes = dict(word.attributes.items())
			if attributes['c5'] == 'CRD': continue
			word_str = word.firstChild.nodeValue.strip()
			if word_str.isalnum() == False: continue
			entry = word_str.lower().strip() + "," + attributes['c5'] + "\n"
			file_1.write(entry)

		file_1.close()

if __name__ == "__main__":
	main()
