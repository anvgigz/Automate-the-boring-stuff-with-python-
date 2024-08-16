import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.code.ok
len(res.text)
print(res.text[:250])

#404 client side error  >>> https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
