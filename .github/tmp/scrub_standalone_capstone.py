from pathlib import Path
import json
import re

index_path=Path('index.html')
content_path=Path('content.json')
text=index_path.read_text(encoding='utf-8')

pattern=re.compile(r'(<script id="content-data" type="application/json">)(.*?)(</script>)',re.S)
match=pattern.search(text)
if not match:
    raise SystemExit('Embedded content block missing')
embedded=json.loads(match.group(2))
embedded.pop('capstone',None)
if isinstance(embedded.get('act3'),dict) and isinstance(embedded['act3'].get('close_bridge'),dict):
    embedded['act3']['close_bridge'].pop('cta',None)
embedded_json=json.dumps(embedded,ensure_ascii=False,separators=(',',':'))
text=text[:match.start(2)]+embedded_json+text[match.end(2):]
index_path.write_text(text,encoding='utf-8')

content=json.loads(content_path.read_text(encoding='utf-8'))
content.pop('capstone',None)
if isinstance(content.get('act3'),dict) and isinstance(content['act3'].get('close_bridge'),dict):
    content['act3']['close_bridge'].pop('cta',None)
content_path.write_text(json.dumps(content,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Standalone Capstone content removed.')
