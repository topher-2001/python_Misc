import re
import urllib.request

#url = 'http://www.chrisdoesartz.com/'
url = "https://bsaber.com/?s=ajr&orderby=relevance&order=DESC&post_type=post%2Cpage"

#regex = re.compile(r"<a href=\"(.*?)\" .*?>")
regex = re.compile(r"<h4 class=\"entry-title\" .*?><a .*?>(.*?)</a></h4>")

raw_html = urllib.request.urlopen(url).read()
matches = regex.findall(str(raw_html))

if len(matches) <= 0:
	print(matches)
	print("Unable to find match")
	exit()

print(str(matches) + "\n")
for match in matches:
	print(match)

