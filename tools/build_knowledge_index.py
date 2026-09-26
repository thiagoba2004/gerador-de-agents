#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, html, json, re, unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

TEXT_EXTS={'.md','.html','.htm','.json','.jsonl','.csv','.txt','.yml','.yaml','.py','.js','.css'}
EXCLUDE_DIRS={'.git','_site','node_modules','vendor','.venv','venv','__pycache__'}
EXCLUDE_FILES={'governanca/KNOWLEDGE_INDEX.jsonl','governanca/KNOWLEDGE_INDEX_META.json','tools/build_knowledge_index.py','tools/query_knowledge_index.py'}
STOP=set('a o os as um uma uns umas de da do das dos e ou em no na nos nas por para com sem sob sobre entre ao aos que se ser foi sao como quando onde qual quais mais menos muito muita muitos muitas este esta estes estas isso isto aquele aquela seu sua seus suas the and of to in for on with from is are be by as at an or'.split())
URL_RE=re.compile(r'https?://[^\s<>\]\[)"\']+')
ID_PATTERNS={
 'project_codes':re.compile(r'\bPRJ-\d{6}\b'),
 'strategy_codes':re.compile(r'\bEA-\d{6}-\d{6}\b'),
 'phase_codes':re.compile(r'\bF-\d{6}-\d{6}-\d{3}\b'),
 'request_ids':re.compile(r'\bREQ-\d{8}-\d{3}\b'),
 'doi':re.compile(r'\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b',re.I),
 'handles':re.compile(r'https?://(?:hdl\.handle\.net|handle\.net)/[^\s<>\]\[)"\']+',re.I)
}
TAG_RULES={
 'bdtd_ibict':['bdtd','biblioteca digital brasileira de teses e dissertacoes','ibict'],
 'pesquisa_academica':['tese','teses','dissertacao','dissertacoes','producao academica','pos-graduacao'],
 'superendividamento':['superendividamento','repactuacao de dividas'],
 'juridico':['jurisprudencia','legislacao','tribunal','processo judicial','direito'],
 'financeiro':['planejamento financeiro','investimento','divida','credito','liquidez','cfp'],
 'trabalho_sindical':['sindicato','bancario','greve','trabalhador','relacoes de trabalho'],
 'governanca':['agents.md','project_state','strategy_log','request_log','governanca'],
 'editorial':['artigo','noticia','observatorio','publicacao','pauta editorial'],
 'fonte':['source_registry','fontes','referencias','bibliografia']
}
SOURCE_SYSTEMS={
 'bdtd.ibict.br':'BDTD/IBICT','ibict.br':'IBICT','stj.jus.br':'STJ','tst.jus.br':'TST','stf.jus.br':'STF',
 'gov.br':'GOV.BR','planalto.gov.br':'Planalto','cnj.jus.br':'CNJ','bcb.gov.br':'Banco Central do Brasil',
 'usp.br':'USP','ufba.br':'UFBA','ufpe.br':'UFPE','ufc.br':'UFC','ufpb.br':'UFPB','unb.br':'UnB','ufu.br':'UFU','ufsc.br':'UFSC'
}
def norm(s):
    return re.sub(r'\s+',' ',unicodedata.normalize('NFKD',str(s)).encode('ascii','ignore').decode('ascii').lower()).strip()
def read_text(p):
    try:return p.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        try:return p.read_text(encoding='latin-1')
        except Exception:return None
    except Exception:return None
def plain_text(text,ext):
    if ext in {'.html','.htm'}:
        text=re.sub(r'(?is)<script.*?</script>|<style.*?</style>',' ',text)
        text=re.sub(r'(?s)<[^>]+>',' ',text); text=html.unescape(text)
    return text
def title_headings(text,ext,fallback):
    title=None; hs=[]
    if ext=='.md':
        for line in text.splitlines():
            m=re.match(r'^\s*(#{1,6})\s+(.+?)\s*$',line)
            if m:
                v=re.sub(r'\s+#+\s*$','',m.group(2)).strip(); hs.append(v)
                if title is None and len(m.group(1))==1:title=v
    elif ext in {'.html','.htm'}:
        m=re.search(r'(?is)<title[^>]*>(.*?)</title>',text)
        if m:title=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',m.group(1)))).strip()
        for m in re.finditer(r'(?is)<h[1-6][^>]*>(.*?)</h[1-6]>',text):
            v=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',m.group(1)))).strip()
            if v:hs.append(v)
        if not title and hs:title=hs[0]
    return title or fallback,hs[:24]
def keywords(text,limit=24):
    toks=[norm(x) for x in re.findall(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_-]{2,}",text)]
    return [w for w,_ in Counter(x for x in toks if x and x not in STOP and not x.isdigit()).most_common(limit)]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--out',default='governanca/KNOWLEDGE_INDEX.jsonl'); ap.add_argument('--meta',default='governanca/KNOWLEDGE_INDEX_META.json'); a=ap.parse_args()
    root=Path(a.root).resolve(); rows=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file() or any(x in EXCLUDE_DIRS for x in p.parts) or p.suffix.lower() not in TEXT_EXTS:continue
        rel=p.relative_to(root).as_posix()
        if rel in EXCLUDE_FILES:continue
        text=read_text(p)
        if text is None:continue
        raw=p.read_bytes(); ext=p.suffix.lower(); title,hs=title_headings(text,ext,p.stem.replace('-',' ').replace('_',' ')); plain=plain_text(text,ext)
        urls=[]
        for u in URL_RE.findall(text):
            u=u.rstrip('.,;:')
            if u not in urls:urls.append(u)
        domains=[]
        for u in urls:
            d=urlparse(u).netloc.lower().split(':')[0]
            if d.startswith('www.'):d=d[4:]
            if d and d not in domains:domains.append(d)
        systems=[]
        for d in domains:
            for suffix,label in SOURCE_SYSTEMS.items():
                if d==suffix or d.endswith('.'+suffix):
                    if label not in systems:systems.append(label)
        hay=norm(' '.join([rel,title,*hs])+' '+plain[:120000])
        tags=sorted(tag for tag,needles in TAG_RULES.items() if any(norm(n) in hay for n in needles))
        ids={k:sorted(set(rx.findall(text)))[:100] for k,rx in ID_PATTERNS.items()}
        rows.append({'path':rel,'extension':ext,'size_bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'title':title,'headings':hs,'keywords':keywords(plain),'semantic_tags':tags,'external_domains':domains[:50],'source_systems':systems,'identifiers':ids})
    out=root/a.out; meta=root/a.meta; out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')
    tc=Counter(t for r in rows for t in r['semantic_tags']); sc=Counter(s for r in rows for s in r['source_systems'])
    meta.write_text(json.dumps({'schema_version':'1.0','record_count':len(rows),'extensions':dict(sorted(Counter(r['extension'] for r in rows).items())),'semantic_tag_counts':dict(sorted(tc.items())),'source_system_counts':dict(sorted(sc.items())),'index_file':a.out,'generator':'tools/build_knowledge_index.py','deterministic':True},ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('indexed='+str(len(rows)))
if __name__=='__main__':main()
