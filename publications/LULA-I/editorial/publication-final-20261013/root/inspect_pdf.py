"""Read-only PDF inspection and rendering for the final mechanism-paper review."""
from pathlib import Path
import argparse, hashlib, json, re, subprocess
import fitz
from PIL import Image, ImageDraw

ap=argparse.ArgumentParser()
ap.add_argument('pdf',type=Path)
ap.add_argument('output',type=Path)
args=ap.parse_args()
args.output.mkdir(parents=True,exist_ok=True)
doc=fitz.open(args.pdf)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pages=[];texts=[]
for i,page in enumerate(doc):
    text=page.get_text();texts.append(text)
    image=args.output/f'page-{i+1:02d}.png'
    page.get_pixmap(dpi=150,alpha=False).save(image)
    outside=[]
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line['spans']:
                if not span['text'].strip():continue
                r=fitz.Rect(span['bbox'])
                if r.x0 < -0.5 or r.y0 < -0.5 or r.x1 > page.rect.width+0.5 or r.y1 > page.rect.height+0.5:
                    outside.append({'text':span['text'],'bbox':list(r)})
    pages.append({'page':i+1,'width_pt':page.rect.width,'height_pt':page.rect.height,
                  'text_characters':len(text),'outside_page_spans':outside,'render_sha256':sha(image)})
for start in range(0,len(pages),4):
    canvas=Image.new('RGB',(1200,1740),'#dadada');draw=ImageDraw.Draw(canvas)
    for j,i in enumerate(range(start,min(start+4,len(pages)))):
        im=Image.open(args.output/f'page-{i+1:02d}.png').convert('RGB');im.thumbnail((580,825))
        x=(j%2)*600+10;y=(j//2)*870+30
        canvas.paste(im,(x,y));draw.text((x,y-22),f'Page {i+1}',fill='black')
    canvas.save(args.output/f'sheet-{start//4+1:02d}.jpg',quality=94)
text='\n\f\n'.join(texts)
(args.output/'text.txt').write_text(text,encoding='utf8')
fonts=subprocess.run(['pdffonts',str(args.pdf)],capture_output=True,text=True,encoding='utf8',check=True).stdout
(args.output/'fonts.txt').write_text(fonts,encoding='utf8')
info=subprocess.run(['pdfinfo',str(args.pdf)],capture_output=True,text=True,encoding='utf8',check=True).stdout
(args.output/'info.txt').write_text(info,encoding='utf8')
font_rows=[line.split() for line in fonts.splitlines()[2:] if line.strip()]
record={'pdf_sha256':sha(args.pdf),'pages':pages,'page_count':len(pages),
        'metadata':doc.metadata,'outline':doc.get_toc(),
        'blank_pages':[r['page'] for r in pages if r['text_characters']<10],
        'text_outside_page':sum(len(r['outside_page_spans']) for r in pages),
        'forbidden_public_terms':re.findall(r'RA36|RA-dual|R6A|evidence[- ]manifest|evidence cutoff|public deposit to.?do|TODO|FIXME|CC BY|Creative Commons',text,re.I),
        'type3_fonts':'Type 3' in fonts,
        'all_fonts_embedded':all(row[-5]=='yes' for row in font_rows),
        'visual_review':'PENDING actual inspection of every contact sheet and detailed figure/table pages'}
(args.output/'INSPECTION.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in record.items() if k not in ('pages','outline','metadata')}))
