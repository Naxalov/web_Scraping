# Import libraries

from bs4 import BeautifulSoup

html_data = """
<html>
    <head>
        <title>My Title</title>
    </head>
    <body>
        <h1>My Heading</h1>
        <p>My paragraph</p>
    </body>
</html>
"""
soup = BeautifulSoup(html_data, 'html.parser')
title = soup.title
print(title)
print(title.name)
print(title.string)