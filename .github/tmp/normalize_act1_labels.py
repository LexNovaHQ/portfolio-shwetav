from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

replacements = {
    'ACT I · LEGAL REASONING': 'ACT I · LEGAL GRAMMAR',
    "{title:'Harm',question:'What is the terminal legal wrong?'": "{title:'Terminal Harm',question:'What is the terminal legal wrong?'"
}

for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'Expected exactly one occurrence of {old!r}; found {count}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('Act I labels normalized.')
