#!/usr/local/bin/python
import urllib

from datetime import datetime
from sys import argv


TEMPLATE_FILE = 'new_post_template.md'

def generate_new_post(name, date):
  content = open(TEMPLATE_FILE, 'r').read()
  result_content = content.format(
    title=name,
    date=date.strftime("%Y-%m-%d %H:%M:%S")
  )

  result_filename = "_posts/{date}-{title}.md".format(
    date=date.strftime("%Y-%m-%d"),
    title=urllib.quote(name.lower().replace(" ", "-").replace(":","-"))
  )

  open(result_filename, 'w').write(result_content)
  print "Sample written into %s" % result_filename


if __name__ == '__main__':
  if len(argv) != 2:
    print "Usage: new_post.py 'Post Title Goes Here'"
    exit()

  postname = argv[1]
  postdate = datetime.now()
  generate_new_post(postname, postdate)
