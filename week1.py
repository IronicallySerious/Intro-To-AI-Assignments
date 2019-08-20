import xml.dom.minidom

def main():
	dom = xml.dom.minidom.parse('D:\\Python Projects\\Train-corpus\\A00.xml')
	words = dom.getElementsByTagName("w")
	file_1 = open("week1.csv","w+")

	for word in words:
		attributes = dict(word.attributes.items())
		if attributes['c5'] == 'CRD': continue
		entry = word.firstChild.nodeValue.strip() + "," + attributes['c5'] + "\n"
		file_1.write(entry)

	file_1.close()

if __name__ == "__main__":
	main()
