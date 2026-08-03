#!/usr/bin/env python3
"""Post 2 — The Orgasm Gap, 3-slide carousel (1080x1350). Official Nancy brand kit."""
import os
BASE = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="fonts-embedded.css">
<style>
  :root{--pink:#FF30CC;--lime:#CCFD28;--cream:#FCF7ED;--ink:#282826;--custard:#FBEF82;--dawn:#7E7F84;}
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{width:1080px;height:1350px}
  body{font-family:'DM Sans',sans-serif;color:var(--ink);overflow:hidden;position:relative}
  .frame{position:absolute;inset:0;padding:86px 84px 70px;display:flex;flex-direction:column}
  .foot{display:flex;align-items:center;justify-content:space-between;margin-top:auto}
  .wordmark{font-family:'Fraunces',serif;font-weight:900;font-style:italic;font-size:32px}
  .swipe{font-weight:700;font-size:22px}
  .big{font-family:'Fraunces',serif;font-weight:900;letter-spacing:-.012em}
</style></head><body>
"""

def footer(logo, swipe_color, swipe="swipe →"):
    return f'''
  <div class="foot">
    <span class="wordmark" style="color:{logo}">Nancy</span>
    <span class="swipe" style="color:{swipe_color}">{swipe}</span>
  </div>
</div>
</body></html>'''

S = []

# ---- Slide 1: the stat, ink bg, giant numbers + fruit motifs + kicker
S.append(("s1", f'''
<style>body{{background:var(--ink)}}
  .statrow{{display:flex;align-items:baseline;gap:26px}}
  .statnum{{font-family:'Fraunces',serif;font-weight:900;letter-spacing:-.02em;line-height:.9}}
  .statlbl{{font-size:33px;font-weight:500;line-height:1.3}}
  .bar{{height:26px;border-radius:100px;margin-top:18px;position:relative;overflow:hidden}}
  .bar::after{{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.35),rgba(255,255,255,0));width:40%}}
  .kicker{{font-weight:700;font-size:19px;letter-spacing:.2em;text-transform:uppercase;color:var(--dawn)}}
</style>
<div class="frame">
  <div class="kicker">The data nobody puts on the syllabus</div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:64px">
    <div>
      <div class="statrow"><span class="statnum" style="font-size:190px;color:var(--lime)">95%</span></div>
      <div class="statlbl" style="color:var(--cream)">of men <b>finish.</b></div>
      <div class="bar" style="width:95%;background:var(--lime)"></div>
    </div>
    <div>
      <div class="statrow"><span class="statnum" style="font-size:190px;color:var(--pink)">65%</span></div>
      <div class="statlbl" style="color:var(--cream)">of women <b>don't get that courtesy.</b></div>
      <div class="bar" style="width:35%;background:var(--pink)"></div>
    </div>
  </div>
  <svg width="150" height="110" viewBox="0 0 150 110" style="position:absolute;right:60px;top:70px;opacity:.15" xmlns="http://www.w3.org/2000/svg">
    <path d="M20 55C20 27 42 14 75 14C108 14 130 27 130 55C130 83 108 96 75 96C42 96 20 83 20 55Z" fill="#FF30CC"/>
    <path d="M20 50 Q6 44 2 48 Q7 60 21 62 Q19 55 20 50Z" fill="#FF30CC"/>
    <path d="M130 50 Q144 44 148 48 Q143 60 129 62 Q131 55 130 50Z" fill="#FF30CC"/>
  </svg>
  <svg width="100" height="100" viewBox="0 0 90 90" style="position:absolute;right:75px;top:1080px;opacity:.16" xmlns="http://www.w3.org/2000/svg">
    <g fill="#CCFD28"><circle cx="30" cy="20" r="16"/><circle cx="55" cy="18" r="15"/><circle cx="20" cy="42" r="15"/><circle cx="45" cy="44" r="17"/><circle cx="68" cy="38" r="14"/><circle cx="33" cy="65" r="15"/><circle cx="58" cy="64" r="15"/></g>
  </svg>
''' + footer("var(--pink)", "var(--lime)")))

# ---- Slide 2: the definition, cream bg, real Lem photo as corner element
S.append(("s2", f'''
<style>body{{background:var(--cream)}}
  .defchip{{display:inline-block;background:var(--ink);color:var(--lime);font-weight:700;font-size:22px;
     letter-spacing:.16em;text-transform:uppercase;padding:14px 28px;border-radius:100px;margin-bottom:36px}}
  .photocorner{{position:absolute;right:20px;bottom:150px;width:340px;height:340px;border-radius:50%;overflow:hidden;
     box-shadow:0 30px 60px rgba(40,40,38,.18);z-index:1}}
  .photocorner img{{width:100%;height:100%;object-fit:cover;object-position:60% 30%}}
  .foot{{position:relative;z-index:2}}
</style>
<div class="frame">
  <div style="height:6px"></div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <span><span class="defchip">noun &middot; the orgasm gap</span></span>
    <div class="big" style="font-size:66px;line-height:1.05;color:var(--ink);max-width:760px">It's not anatomy's fault &mdash; anatomy was <span style="color:var(--pink)">doing fine.</span></div>
    <div style="margin-top:34px;font-size:31px;line-height:1.45;max-width:640px;font-weight:500">
      It's an <b>information problem.</b><br>And information problems <b style="color:var(--pink)">have fixes.</b></div>
  </div>
  <div class="photocorner"><img src="../assets/product-photos/lem-front.png"></div>
''' + footer("var(--pink)", "var(--pink)")))

# ---- Slide 3: CTA, pink bg, custard text (official pairing) + photo badge
S.append(("s3", f'''
<style>body{{background:var(--pink)}}
  .photobadge{{position:absolute;right:70px;top:70px;width:180px;height:180px;border-radius:50%;overflow:hidden;
     border:5px solid var(--custard);box-shadow:0 20px 40px rgba(40,40,38,.25)}}
  .photobadge img{{width:100%;height:100%;object-fit:cover;object-position:center 35%}}
</style>
<div class="frame">
  <div style="height:6px"></div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <div class="big" style="font-size:120px;line-height:.98;color:var(--cream)">Comment</div>
    <div class="big" style="font-size:200px;line-height:.95;color:var(--custard)">GAP</div>
    <div style="margin-top:44px;font-size:36px;font-weight:700;color:var(--cream);max-width:840px;line-height:1.35">
      We'll send the fix. &rarr;</div>
    <div style="margin-top:16px;font-size:26px;font-weight:500;color:var(--custard);max-width:840px;line-height:1.4;opacity:.95">
      Straight to your DMs. Free. No awkward small talk.</div>
  </div>
  <div class="photobadge"><img src="../assets/product-photos/berri-inhand.png"></div>
''' + footer("var(--cream)", "var(--custard)", swipe="♥ share this")))

for name, body in S:
    open(os.path.join(BASE, f"post2-{name}.html"), "w").write(HEAD + body)
    print("wrote", name)
