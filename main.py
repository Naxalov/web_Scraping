# Import libraries

from bs4 import BeautifulSoup

html_data = """
<html>
    <head>
        <title>My Title</title>
    </head>
    <body>
        <h1>My Heading</h1>
        <p>My paragraph 1</p>
        <p>My paragraph 2</p>
    </body>
</html>
"""
soup = BeautifulSoup(html_data, 'html.parser')
title = soup.title
print(title)
print(title.name)
print(title.string)
# Get parent
print(title.parent.name)
# Get p tag
p_tag = soup.p
print(type(p_tag))