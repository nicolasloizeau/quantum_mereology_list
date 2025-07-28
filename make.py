import bibtexparser

with open('mereology.bib', 'r') as f:
    bib_string = f.read()

library = bibtexparser.parse_string(bib_string)

markdown = ""

entries = []


for entry in library.entries:
    doi = entry['doi']
    if "doi.org" in doi:
        doi = doi.split("doi.org/")[-1]
    url = "https://doi.org/"+doi
    entries.append({
        'title': entry['title'],
        'author': entry['author'],
        'year': int(entry['year']),
        'url': url})

entries = sorted(entries, key=lambda x: x['year'], reverse=True)

for entry in entries:
    url = "https://doi.org/"+doi
    entry  = "- [{}]({}) {}".format(entry["title"], entry["url"], entry["year"])
    markdown += entry
    markdown += "\n"


with open('list.md', 'w') as f:
    f.write(markdown)
