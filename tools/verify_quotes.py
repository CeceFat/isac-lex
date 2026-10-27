"""Check every English double-quoted phrase in reports/*.md against the official sources.

Run tools/extract_sources.py first (it writes the gitignored source/ folder), then:

    python tools/verify_quotes.py

Rules
- A quote on a line that cites ¶ paragraph numbers must appear in one of those paragraphs of
  TR 23.700-14 v20.0.0 (a window of ±2 paragraphs is allowed, for citations that point at the step a
  sentence continues from). Finding it elsewhere in the TR counts as a failure: the coordinate is wrong.
- A quote without ¶ must appear somewhere in the sources: the TR text and tables, TR v0.2.0,
  TS 22.137, TR 22.870, the SA2#173 documents, the SA2 chair notes, or IEEE 802.11bf.
- Quotes with an ellipsis are checked fragment by fragment.
Exit code 1 if anything fails.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'source')


def norm(s):
    s = (s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
         .replace(' ', ' ').replace('\t', ' '))
    return re.sub(r'\s+', ' ', s).strip().lower()


def load():
    paras = {}
    with open(os.path.join(SRC, 'tr23700-14_v20.txt'), encoding='utf-8') as f:
        for line in f:
            parts = line.rstrip('\n').split('\t', 2)
            if len(parts) == 3 and parts[0].isdigit():
                paras[int(parts[0])] = norm(parts[2])
    others = {}
    for pattern in ('tr23700-14_v20_tables.txt', 'extra/*.txt', 'tdocs/*.txt', 'chair/*.txt', 'ieee80211bf.txt'):
        for f in glob.glob(os.path.join(SRC, pattern)):
            t = open(f, encoding='utf-8', errors='replace').read()
            if f.endswith('ieee80211bf.txt'):
                t = re.sub(r'-\n', '', t)
            others[os.path.relpath(f, SRC)] = norm(t)
    return paras, others


def main():
    paras, others = load()
    tr_all = ' \n '.join(paras.values())
    qre = re.compile(r'"([^"]{3,400})"')
    total, bad = 0, []
    for rep in sorted(glob.glob(os.path.join(ROOT, 'reports', '*.md'))):
        for ln, line in enumerate(open(rep, encoding='utf-8'), 1):
            cites = [int(x) for x in re.findall(r'¶(\d{3,4})', line)]
            for a, b in re.findall(r'¶(\d{3,4})–(\d{3,4})', line):
                cites += list(range(int(a), int(b) + 1))
            for q in qre.findall(line):
                nq = norm(q).strip(' .,;:')
                if not re.search(r'[a-z]', nq) or len(nq) < 4:
                    continue
                frags = [x.strip(' .,;:') for x in re.split(r'\s*(?:\.\.\.|…)\s*', nq) if x.strip(' .,;:')]
                total += 1
                found = None
                if cites:
                    window = {p for c in cites for p in range(c - 2, c + 3)}
                    if all(any(fr in paras.get(p, '') for p in window) for fr in frags):
                        found = 'cited paragraph'
                if found is None and not cites and all(fr in tr_all for fr in frags):
                    found = 'TR'
                if found is None and not cites:
                    for k, v in others.items():
                        if all(fr in v for fr in frags):
                            found = k
                            break
                if found is None and cites and any(all(fr in v for fr in frags) for v in others.values()):
                    found = 'other source (line also cites ¶)'
                if found is None:
                    bad.append(f'{os.path.basename(rep)}:{ln}: "{q[:100]}" cites {cites[:5]}')
    print(f'quotes checked: {total}')
    print(f'failures: {len(bad)}')
    for b in bad:
        print('  ' + b)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
