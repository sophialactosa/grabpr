from bs4 import BeautifulSoup

def getPR(data):

	idPR = source.find(attrs={"name":"idReport"})
	text = idPR.get_text()

	# break multi-headlines into a line each
	lines = (line.strip() for line in text.splitlines())

	# drop blank lines
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

	#get all new text
	nospacetext = '\n'.join(chunk for chunk in chunks if chunk)
	indnospacetext = []
	indnospacetext = nospacetext.split('\n')

	return indnospacetext

source = BeautifulSoup(open("gocha.html"))
stdName = getPR(source)[5]
spvName = getPR(source)[1]
uniName = getPR(source)[3]
print "Student Name:", stdName
print "Supervisor Name:", spvName
print "University:", uniName