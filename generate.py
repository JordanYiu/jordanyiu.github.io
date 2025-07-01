import json
from datetime import UTC, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

with Path('data.json').open(encoding='utf-8') as f:
    data = json.load(f)
data['current_year'] = datetime.now(tz=UTC).year

if 'social_links' in data:
    for link in data['social_links']:
        if link.get('svg_path'):
            with Path(link['svg_path']).open(encoding='utf-8') as svg_file:
                link['svg_data'] = svg_file.read()

env = Environment(loader=FileSystemLoader("."), autoescape=True)
index_template =  env.get_template("index_template.html")
# music_template = env.get_template('music_template.html')
# resume_template = env.get_template("resume_template.html")

# Pages to render
html_output = index_template.render(**data)
# music_output = music_template.render(**data)
# resume_output = resume_template.render(**data)

# My site
with Path("index.html").open("w", encoding="utf-8") as f:
    f.write(html_output)

# with Path("jordanyiu.github.io/music.html").open("w", encoding="utf-8") as f:
#     f.write(music_output)

# with Path("resume.html").open("w", encoding="utf-8") as f:
#     f.write(resume_output)

print("HTML file generated successfully!")