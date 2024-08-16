import bs4
exampleFile = ('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
str(elems[0])
elems[0].getText()
elems[0].attrs