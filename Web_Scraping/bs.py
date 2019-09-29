from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" class="special">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Document</title>
</head>
<body>
	<div id="first">
		<h3 data-example="yes">hi</h3>
		<p>more text.</p>
	</div>
	<ol>
		<li class="special super-special">This list item is special.</li>
		<li class="special">This list item is also special.</li>
		<li>This list item is not special.</li>
	</ol>
	<div>bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
# d = soup.body
# d = soup.find("div")
# d = soup.find_all("div")
# d = soup.find(id="first")
# d = soup.find_all(class_="special")
# d = soup.find(attrs={"data-example": "yes"})
# d = soup.select("#first")
# d = soup.select(".special")
# d= soup.select("[data-example]")
# print(d)
# print(type(d))

# elements = soup.select(".special")
# for el in elements:
# 	print(el.name)
# 	print(el.get_text())
# 	print(el.attrs)

# attr = soup.find("div")["id"]
# print(attr)

# data = soup.body.contents[1].next_sibling.next_sibling
# data = soup.find(class_="super-special").parent.parent
# data = soup.find(id="first").find_next_sibling().find_next_sibling()
# data = soup.select("li")[1].find_previous_sibling()
data = soup.find("h3").find_parent()
print(data)

