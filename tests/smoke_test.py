from playwright.sync_api import sync_playwright
from pathlib import Path
import json
HTML=(Path(__file__).resolve().parents[1]/'index.html').read_text()
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 ctx=browser.new_context(accept_downloads=True, viewport={'width':1360,'height':900})
 page=ctx.new_page();errors=[];dialogs=[]
 page.on('pageerror',lambda e: errors.append(str(e)))
 page.on('dialog',lambda d:(dialogs.append(d.message),d.accept()))
 page.evaluate("Object.defineProperty(window,'localStorage',{value:{store:{},getItem(k){return this.store[k]||null},setItem(k,v){this.store[k]=v},removeItem(k){delete this.store[k]}},configurable:true})")
 page.set_content(HTML)
 def data(s):return page.evaluate(s)
 def tab(n):page.locator(f'[data-tab="{n}"]').click()
 def check(condition,msg):
  if not condition:raise AssertionError(msg)
  print('PASS',msg)
 check(data('db.items.length')==5,'first-visit 5 seeded projects')
 check(data("db.items.find(p=>p.id==='OBG-001').resources.expert[1]")==301,'historical expert resource overage fixture')
 check('OBG-001' in page.locator('#v11Overages').inner_text(),'category-level overage shown despite overall balance')
 check(data("db.evalRuns.length")==7,'seven manually authored evaluation examples')
 check('4 / 4' in page.locator('#v12EvaluationGovernance').inner_text(),'unique-case coverage in evaluation panel')
 # guided authorization targeting
 page.locator('#v11Tour').click();page.locator('[data-v12-tour="authorization"]').click()
 check(page.locator('#authProject').input_value()=='OBG-005','guided navigation selects pending project')
 check('pending' in page.locator('#v11Readiness').inner_text().lower() or 'requirements' in page.locator('#v11Readiness').inner_text().lower(),'readiness actionable for new activation')
 # decision reversal without or with stale rationale must block
 orig=data("db.items.find(p=>p.id==='OBG-005').awardApprovals.second.decision")
 check(orig=='Rejected','seeded second approver rejected')
 page.locator('[data-v10-approval="second.decision"]').select_option('Approved')
 page.locator('[data-v10-save-approvals]').click()
 check(data("db.items.find(p=>p.id==='OBG-005').awardApprovals.second.decision")==orig,'blank/new-rationale missing prevents decision reversal')
 page.locator('[data-v10-approval="second.notes"]').fill('Supporting institutional evidence not yet complete.')
 page.locator('[data-v10-save-approvals]').click()
 check(data("db.items.find(p=>p.id==='OBG-005').awardApprovals.second.decision")==orig,'reused prior comment cannot authorize reversal')
 page.locator('[data-v10-approval="second.notes"]').fill('New fictional evidence supports reconsidering approval once authorization gates are completed.')
 page.locator('[data-v10-save-approvals]').click()
 check(data("db.items.find(p=>p.id==='OBG-005').awardApprovals.second.decision")=='Approved','new rationale allows documented decision reversal')
 audit=data("db.audit.find(a=>a.field==='second.decision')")
 check(audit and audit['before']=='Rejected' and audit['after']=='Approved','decision audit tracks previous/new')
 # status active legacy changes
 page.locator('#authProject').select_option('OBG-001');page.wait_for_timeout(50)
 check('Historical authorization evidence' in page.locator('#v11Readiness h3').inner_text(),'legacy evidence distinguished from new activation')
 # resource overage attempt blocked
 tab('usage')
 page.locator('#which').select_option('OBG-001');page.locator('#type').select_option('expert');page.fill('#amount','1');page.locator('#record').click()
 check(data("db.items.find(p=>p.id==='OBG-001').resources.expert[1]")==301,'over-allocation new usage blocked')
 # request + no allocation mutation
 page.locator('#v12AmendProject').select_option('OBG-001');page.locator('#v12AmendCategory').select_option('expert');page.fill('#v12AmendTotal','310');page.fill('#v12AmendRequestor','Request Person');page.fill('#v12AmendReference','REQ-1');page.fill('#v12AmendWhy','Need additional authorized expert time to complete planned benchmark review.');page.locator('#v12RequestAmend').click()
 check(data("db.items.find(p=>p.id==='OBG-001').resources.expert[0]")==300,'request not effective until reviewed')
 # same person cannot approve
 page.fill('#v12AmendApprover','request person');page.fill('#v12AmendApprovalRef','DEC-1');page.fill('#v12AmendDecisionWhy','I have reviewed this project and determined the resource adjustment is valid.');page.locator('#v12DecideAmend').click()
 check(data("db.resourceAmendments[0].status")=='Pending','separation of duties enforced')
 page.fill('#v12AmendApprover','Independent Example Reviewer');page.locator('#v12DecideAmend').click()
 check(data("db.resourceAmendments[0].status")=='Approved','qualified example decision recorded')
 check(data("db.items.find(p=>p.id==='OBG-001').resources.expert[0]")==310,'approved new authorization reflected')
 check('OBG-001' not in page.locator('#v11Overages').inner_text(),'approved amendment resolves category overage')
 # Evaluate human review and reject unsupported labels
 tab('evaluation');page.locator('#v12EvalRun').select_option('1')
 page.locator('#v12EvalDisposition').select_option('Uphold predefined reference')
 page.fill('#v12EvalReviewer','Example Scientific Reviewer');page.fill('#v12EvalEvidence','E03-SCOPE');page.fill('#v12EvalRationale','The reported deliverable is outside authorized scope; the reviewer should request evidence.')
 page.locator('#v12SaveEvalReview').click()
 check(not data('db.evalRuns[1].humanReview'),'unselected root cause hypothesis blocks review')
 page.locator('#v12EvalRun').select_option('1');page.locator('#v12EvalCause').select_option('Scope deviation overlooked');page.locator('#v12EvalDisposition').select_option('Uphold predefined reference');page.fill('#v12EvalReviewer','Example Scientific Reviewer');page.fill('#v12EvalEvidence','E03-SCOPE');page.fill('#v12EvalRationale','The reported deliverable is outside authorized scope; the reviewer should request evidence.');page.locator('#v12SaveEvalReview').click()
 check(data('db.evalRuns[1].humanReview.cause')=='Scope deviation overlooked','named human disposition, evidence and hypothesis recorded')
 check(data('db.evalRuns[1].reference')=='Potential deviation','human disposition does not silently alter reference')
 # Simulate a true new browser document with a fresh JS realm and preserved local storage.
 stored=page.evaluate('localStorage.store')
 page.close();page=ctx.new_page()
 page.on('pageerror',lambda e: errors.append(str(e)))
 page.on('dialog',lambda d:(dialogs.append(d.message),d.accept()))
 page.evaluate("Object.defineProperty(window,'localStorage',{value:{store:"+json.dumps(stored)+",getItem(k){return this.store[k]||null},setItem(k,v){this.store[k]=v},removeItem(k){delete this.store[k]}},configurable:true})")
 page.set_content(HTML)
 check(data('db.resourceAmendments[0].status')=='Approved','browser-local amendment persists after document reload')
 check(data('db.evalRuns[1].humanReview.decision')=='Uphold predefined reference','browser-local human decision persists')
 # queue compact filtering
 tab('review');print('queue details',page.locator('#queue details').count())
 check(page.locator('#queue details').count()>=1,'review cards collapsed and navigable')
 page.fill('#v12ReviewSearch','Cedar');check('1 of ' in page.locator('#v12ReviewCount').inner_text(),'search filters review queue')
 # Structured audit shape present through source inspection and export handler
 check('audit_structured_v11.csv' in HTML and 'resource_amendments.csv' in HTML and 'evaluation_governance.csv' in HTML,'three governance CSV export actions present')
 # no unhandled errors
 check(not errors,'no uncaught JavaScript exceptions')
 print('dialogs:',len(dialogs),'total audit:',data('db.audit.length'))
 page.screenshot(path='/mnt/data/obg_release_review_queue.png',full_page=True)
 ctx.close();browser.close()
