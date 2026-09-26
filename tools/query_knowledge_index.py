#!/usr/bin/env python3
import argparse,json,re,unicodedata
from pathlib import Path
def n(s):return re.sub(r'\\s+',' ',unicodedata.normalize('NFKD',str(s)).encode('ascii','ignore').decode('ascii').lower()).strip()
def blob(r):
    x=[r.get('path',''),r.get('title',''),' '.join(r.get('headings',[])),' '.join(r.get('keywords',[])),' '.join(r.get('semantic_tags',[])),' '.join(r.get('external_domains',[])),' '.join(r.get('source_systems',[]))]
    for v in r.get('identifiers',{}).values():x.append(' '.join(v))
    return n(' '.join(x))
def score(r,terms):
    p=n(r.get('path',''));t=n(r.get('title',''));tags=n(' '.join(r.get('semantic_tags',[])));src=n(' '.join(r.get('source_systems',[])));b=blob(r);s=0
    for q in terms:
        if q not in b:return 0
        s+=12 if q in t else 0;s+=10 if q in tags else 0;s+=10 if q in src else 0;s+=8 if q in p else 0;s+=3
    return s
ap=argparse.ArgumentParser();ap.add_argument('query');ap.add_argument('indexes',nargs='+');ap.add_argument('--limit',type=int,default=20);a=ap.parse_args()
terms=[n(x) for x in a.query.split() if n(x)];hits=[]
for idx in a.indexes:
    for line in Path(idx).read_text(encoding='utf-8').splitlines():
        if not line.strip():continue
        r=json.loads(line);s=score(r,terms)
        if s:hits.append((s,idx,r))
for s,idx,r in sorted(hits,key=lambda x:(-x[0],x[2].get('path','')))[:a.limit]:print(json.dumps({'score':s,'index':idx,**r},ensure_ascii=False))
