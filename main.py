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

# Get all the p tags
p_tags = soup.find_all('p')
for p in p_tags:
    print(p.text)