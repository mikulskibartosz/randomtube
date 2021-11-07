import gzip
import random
import os

with gzip.open('links.txt.gz', 'rt') as input_file:
    lines = input_file.readlines()

selected_articles = random.sample(lines, 1000)

def turn_into_youtube_search_link(text):
    no_new_line = text.strip()
    remove_list_of = no_new_line.replace('list_of_', '')
    no_disambiguation = remove_list_of.replace('disambiguation', '')
    underscore_to_plus = no_disambiguation.replace('_', '+')
    underscore_to_space = no_disambiguation.replace('_', ' ')
    return f'https://www.youtube.com/results?search_query={underscore_to_plus}', underscore_to_space

youtube_links = map(turn_into_youtube_search_link, selected_articles)

def generate_html(links):
    def generate_link(link):
        return f'<a href="{link[0]}" target="_blank">{link[1]}</a><br>'
    
    links_html = "\n".join(list(map(generate_link, links)))
    
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Random YouTube links</title>
  </head>
  <body>
    <center>
        {links_html}
    </center>
  </body>
</html>
    """

html = generate_html(youtube_links)

if not os.path.exists('public'):
    os.mkdir('public')

with open('public/index.html', 'w') as output_file:
    output_file.write(html)
