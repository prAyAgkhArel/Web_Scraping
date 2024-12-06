from bs4 import BeautifulSoup   #bs4=beautifulsoup4
#this is the module for easy reading html or xml files

with open("./website.html", "r") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "html.parser")
#html.parser is passed as argument so that bs4 understands the contents

print(soup)
print("\n\n\n")
print(soup.title)  #prints whole title tag
print("\n\n\n")
print(soup.title.name) #prints name of title i.e "title"
print("\n\n\n")
print(soup.title.string) # prints string of title tag
print("\n\n\n")
print(soup.h1.string)  #prints first h1 content
print(soup.prettify())  #prints html with proper indentation

all_anchor_tags = soup.find_all("a")
print(all_anchor_tags)  # i.e  a list of all anchor tags used
print("\n")

for tag in all_anchor_tags:
    text = tag.getText()   # to get hold of content of anchor tags, use .getText()
    print(text)
    link = tag.get("href")  # to get hold of value of the attribute, use .get("attribute")
    print(link)
    print("\n")

heading = soup.find("h1", id="name")
# to get hold of element with its name and attribute
# since find() is used , it finds the first element that matches the condition
print(heading)
print("\n")

h3 = soup.find("h3", class_ = "heading")
# since class is a keyword, underscore is used to say it is not keyword
print(h3)
print("\n")

company_url = soup.select_one("p a") # selects anchor tag inside of paragraph tag i.e html selector
#if we want to use css selectors as an argument to select element, use .select_one(selector = "") or select(selector)
print(company_url)

name = soup.select("#name") #using id selector
print(name) # prints elements with id="name"
#note: if .select_one() is used, it selects first element that has id="name"


