import os, datetime

def index_section(path, header):
    lines = [f"### {header}\n"]
    for fname in sorted(os.listdir(path)):
        if fname.endswith('.md'):
            lines.append(f"- [{fname[:-3]}]({path}/{fname})")
    return '\n'.join(lines)

sections = []
sections.append(index_section('docs', 'Documentation'))
sections.append(index_section('videos', 'Videos'))
# Write back to README.md
with open('README.md','w') as f:
    f.write('# My Knowledge Base\n\n')
    f.write('\n\n'.join(sections))
    f.write(f'\n\n_Last updated: {datetime.date.today()}_')
python scripts/update_index.py
