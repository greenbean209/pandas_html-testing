import os
import webbrowser
import pandas

# Make a data frame
df = pandas.DataFrame({"Something":['foo', 'bar', 'baz'], "Something Else":[1,2,3]})

# Choose a css file for style definitions
style = "query_table.css"

# Convert data frame to HTML and apply a CSS class
table_html = df.to_html(classes="query_table")

# Define path for html file
path = os.path.abspath('data.html')
url = 'file://' + path

# Template HTML String (allows style and table html to be passed in)
html_template = '''
<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <link rel="stylesheet" type="text/css" href="{style}"/>
  <body>
    {table}
  </body>
</html>.
'''

# Passs in style and table
html = html_template.format(style=style, table=table_html)

# Print to check html formatting worked
print(html)

# Write the HTML to a file
with open(path, 'w') as f:
    f.write(html)

# Open a browser window to the html file
webbrowser.open(url)

