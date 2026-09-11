#!/usr/bin/env python3
"""Validate the local persona and the arithmetic actually claimed by its audit."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import token_count,cluster_budget
ROOT=Path(__file__).resolve().parents[1]
RUNTIME=ROOT/'.agents/skills/kaplan-perspective'
AUDIT=ROOT/'fidelity-ledger/audit'
def check(condition,message):
    if not condition: raise ValueError(message)
def load(name): return json.loads((AUDIT/name).read_text())
def main():
    subprocess.run([sys.executable,str(ROOT/'scripts/distiller_validate.py'),str(ROOT),'--strict'],check=True)
    check(not RUNTIME.is_symlink(),'canonical runtime must be a real directory')
    check((ROOT/'SKILL.md').is_symlink() and (ROOT/'SKILL.md').resolve()==RUNTIME/'SKILL.md','root skill alias is wrong')
    check((ROOT/'references').is_symlink() and (ROOT/'references').resolve()==RUNTIME/'references','root references alias is wrong')
    files={str(p.relative_to(RUNTIME)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(RUNTIME.rglob('*')) if p.is_file()}
    record=load('runtime-hashes.json');check(files==record['files'],'runtime bytes changed; fidelity seal is stale')
    digest='sha256:'+hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    check(digest==record['content_hash']==load('fidelity.json')['content_hash'],'runtime hash mismatch')
    check(not load('fidelity.json')['stale'],'audit is marked stale')
    budgets=load('budgets.json');check(len(budgets)==10,'expected core, two standing files, seven modules')
    for row in budgets:
        actual=token_count.count(str(RUNTIME/row['path']),1/0.6,1.3)['tokens_est']
        check(abs(actual-row['realised'])<.02,'wrong size: '+row['path'])
        check(.9*row['budget']<=actual<=1.1*row['budget'],'budget exceeded: '+row['path'])
    scores=load('scores.json');c=scores['core_budget']['counts']
    supply=2200+250*min(c['cost_refusal'],6)+180*min(c['projectible'],7)+200*min(c['procedure'],5)+150*min(c['verdict'],8)+140*min(c['interactional'],5)+120*min(c['variation'],4)
    check(supply==scores['core_budget']['supply']==6350,'core supply mismatch')
    check(abs(sum(scores['weights'].values())-1)<1e-9,'weights do not sum to one')
    ex={e['id']:e for e in load('extractions.json')};ids={c['id']for c in load('clusters-manifest.json')['clusters']}
    check(len(ex)==len(scores['decisions']),'candidate inventory mismatch')
    for row in scores['decisions']:
        check(row['id'] in ex,'unknown candidate')
        check(set(ex[row['id']]['clusters'])<=ids,'unknown source unit')
        value=sum(scores['weights'][k]*v for k,v in row['scores'].items())
        check(abs(value-row['composite'])<1e-8,'composite mismatch: '+row['id'])
        if row['decision']=='core':check(value>=.55,'core threshold failed: '+row['id'])
    for row in scores['cluster_budgets']:
        check(row['cluster_id']in ids,'unknown module anchor')
        sup,bud,*_=cluster_budget.compute(row['counts'],row['words'],row['words_firsthand'],6)
        check(sup==row['supply'] and bud==row['budget'],'module supply mismatch')
    check(scores['standing_budgets']['frameworks']['supply']==700+120*10+200*5+130*5+90*13+110*5+70*3+25*10,'framework supply mismatch')
    check(scores['standing_budgets']['voice']['supply']==600+550*4+250+90*10+40*6+120*8+60*2,'voice supply mismatch')
    for row in budgets[1:3]:
        standing=scores['standing_budgets'][Path(row['path']).stem]
        check(standing['budget']==row['budget'] and standing['realised']==round(row['realised']),'standing realized size mismatch')
    reg=load('registers.json');check(reg['n_registers']==5 and sum(f.get('is_default',False)for f in reg['families'])==1,'register/default mismatch')
    check(len(ids)==98 and load('coverage-map.json')['n_clusters']==98,'coverage mismatch')
    core=(RUNTIME/'SKILL.md').read_text()
    for anchor in ['Iraq remains an error','Good intentions do not release a writer','A hostile judgment can contain an education']:
        check(anchor in core,'missing cost-bearing core anchor: '+anchor)
    for path in RUNTIME.rglob('*.md'):
        for ref in re.findall(r'`(references/[^`]+\.md)`',path.read_text()):
            check((RUNTIME/ref).is_file(),'unresolved path: '+ref)
    for name in ['projection-gate-results.json','final-projection-results.json']:
        result=load(name);check(abs(sum(x['score']for x in result['items'])/(2*len(result['items']))-result['overall'])<1e-9,'projection arithmetic mismatch')
    check(load('fidelity.json')['style']['modulation_reproduced'] is False,'unvalidated modulation must stay disclosed')
    print('\nPASS — layout, runtime hashes, references, budget arithmetic, curation, cost presence, and audit consistency.')
    print('This validates the package, not a claim of complete literary or conversational fidelity.')
if __name__=='__main__':
    try: main()
    except (ValueError,KeyError,OSError,subprocess.CalledProcessError) as exc:
        print('FAIL:',exc,file=sys.stderr);sys.exit(1)
