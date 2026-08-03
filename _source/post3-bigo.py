#!/usr/bin/env python3
"""Post 3 — The Big O. 5-slide carousel: question → 3 reasons → payoff.
1080x1350 each, Hello Nancy brand kit."""
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
  .frame{position:absolute;inset:0;padding:78px 76px 62px;display:flex;flex-direction:column;align-items:center;
         text-align:center;justify-content:space-between}
  .head{font-family:'Fraunces',serif;font-weight:900;font-size:74px;line-height:1.22;letter-spacing:-.018em;position:relative}
  .circ{position:relative;display:inline-block;padding:0 12px}
  .circ svg{position:absolute;left:-18px;top:-10px;width:calc(100% + 36px);height:calc(100% + 20px);overflow:visible}
  .mid{flex:1;width:100%;display:flex;align-items:center;justify-content:center}
  .foot{width:100%;display:flex;align-items:center;justify-content:space-between}
  .wordmark{font-family:'Fraunces',serif;font-weight:900;font-style:italic;font-size:32px}
  .tag{font-family:'Fraunces',serif;font-weight:600;font-style:italic;font-size:30px;opacity:.55}
  .spark{position:absolute}
  .body{font-size:33px;line-height:1.42;max-width:840px;font-weight:500}
  .body b{font-weight:700}
  .num{font-family:'Fraunces',serif;font-weight:900;font-size:150px;line-height:1}
</style></head><body>
"""

def circle(color="#FF30CC"):
    return f'''<svg viewBox="0 0 460 120" preserveAspectRatio="none">
        <path d="M26,62 C24,28 118,10 232,12 C358,14 438,32 434,62 C430,92 326,107 208,104 C96,101 22,86 28,54 C32,34 72,19 138,14"
              stroke="{color}" stroke-width="7" fill="none" stroke-linecap="round"/>
      </svg>'''

def sparks(color="#282826"):
    return f'''
  <svg class="spark" style="left:44px;top:210px" width="76" height="76" viewBox="0 0 76 76">
    <g stroke="{color}" stroke-width="5" stroke-linecap="round">
      <path d="M12 38 H2"/><path d="M18 20 L10 12"/><path d="M18 56 L10 64"/>
    </g>
  </svg>
  <svg class="spark" style="right:40px;top:300px" width="80" height="80" viewBox="0 0 80 80">
    <g stroke="{color}" stroke-width="5" stroke-linecap="round">
      <path d="M64 38 H74"/><path d="M58 20 L66 12"/><path d="M58 56 L66 64"/>
    </g>
  </svg>'''

def footer(wm="var(--pink)", tag_col="var(--ink)", tag="swipe &rarr;"):
    return f'''
  <div class="foot">
    <span class="wordmark" style="color:{wm}">Nancy</span>
    <span class="tag" style="color:{tag_col}">{tag}</span>
  </div>
</div>
</body></html>'''

S = []

# ---- Slide 1: the question + stat card
S.append(("s1", f'''
<style>body{{background:var(--cream)}}
  .stage{{position:relative;width:100%;border-radius:44px;overflow:hidden;background:#fff;
         box-shadow:0 20px 50px rgba(40,40,38,.13)}}
  .photo{{width:100%;height:340px;overflow:hidden;position:relative}}
  .photo img{{width:112%;position:absolute;left:-6%;top:-4%}}
  .bar{{width:100%;background:#fff;padding:30px 44px;display:flex;align-items:center;gap:24px;
       border-top:2px solid rgba(40,40,38,.08)}}
  .bar .lab{{font-weight:700;font-size:28px;white-space:nowrap}}
  .bar .n{{font-family:'Fraunces',serif;font-weight:900;font-size:40px}}
  .bar .sep{{flex:1;height:3px;background:rgba(40,40,38,.12);border-radius:2px}}
</style>
<div class="frame">
  {sparks()}
  <div class="head">
    Why do most women<br>
    reach the <span style="color:var(--pink)">Big O</span> during<br>
    <span class="circ">foreplay,{circle()}</span> but not while<br>
    doing it with a partner?
  </div>
  <div class="mid">
    <div class="stage">
      <div class="photo"><img src="../assets/product-photos/lem-inhand.png"></div>
      <div class="bar">
        <span class="lab">Alone <span class="n" style="color:var(--pink)">95%</span></span>
        <span class="sep"></span>
        <span class="lab" style="color:var(--dawn)">Together <span class="n">69%</span></span>
      </div>
    </div>
  </div>
''' + footer(tag_col="var(--ink)")))

# ---- Slide 2: reason 1
S.append(("s2", f'''
<style>body{{background:var(--lime)}}</style>
<div class="frame">
  {sparks()}
  <div class="mid">
    <div>
      <div class="num" style="color:var(--ink);opacity:.25">01</div>
      <div class="head" style="font-size:66px;margin-top:10px">Foreplay is where the<br>
        <span class="circ">stimulation{circle("#282826")}</span><br>actually happens.</div>
      <div class="body" style="margin-top:38px">Most women need <b>external stimulation</b> to finish. Foreplay is where she's getting it.</div>
    </div>
  </div>
''' + footer(wm="var(--ink)", tag_col="var(--ink)")))

# ---- Slide 3: reason 2
S.append(("s3", f'''
<style>body{{background:var(--cream)}}</style>
<div class="frame">
  {sparks()}
  <div class="mid">
    <div>
      <div class="num" style="color:var(--ink);opacity:.18">02</div>
      <div class="head" style="font-size:66px;margin-top:10px">Then the <span class="circ">script{circle()}</span><br>kicks in.</div>
      <div class="body" style="margin-top:38px">Warm up. Main event. Done.<br><b>The part that was working stops.</b></div>
    </div>
  </div>
''' + footer(tag_col="var(--ink)")))

# ---- Slide 4: reason 3
S.append(("s4", f'''
<style>body{{background:var(--pink)}}
  .head,.body{{color:var(--cream)}}
</style>
<div class="frame">
  {sparks("#FBEF82")}
  <div class="mid">
    <div>
      <div class="num" style="color:var(--custard);opacity:.45">03</div>
      <div class="head" style="font-size:66px;margin-top:10px">And she's still<br><span class="circ">in her head.{circle("#FBEF82")}</span></div>
      <div class="body" style="margin-top:38px;color:var(--custard)">The angle. The time it's taking. Whether he's getting bored. <b style="color:var(--cream)">Hard to arrive anywhere when you never left.</b></div>
    </div>
  </div>
''' + footer(wm="var(--cream)", tag_col="var(--custard)")))

# ---- Slide 5: payoff + CTA
S.append(("s5", f'''
<style>body{{background:var(--ink)}}
  .head{{color:var(--cream)}}
</style>
<div class="frame">
  {sparks("#CCFD28")}
  <div class="mid">
    <div>
      <div class="head" style="font-size:84px">Not chemistry.<br>Not you.<br><span style="color:var(--pink)">Just the order.</span></div>
      <div class="body" style="margin-top:44px;color:var(--cream);opacity:.92">The thing that works keeps getting treated like a warm-up.</div>
      <div style="margin-top:46px;background:var(--cream);border-radius:26px;padding:30px 40px;display:inline-block">
        <div style="font-family:'Fraunces',serif;font-weight:900;font-size:36px;color:var(--ink)">If this is you, <span style="color:var(--pink)">say so.</span></div>
        <div style="font-size:24px;color:var(--ink);margin-top:10px;opacity:.75">You won't be the first in these comments.</div>
      </div>
    </div>
  </div>
''' + footer(wm="var(--pink)", tag_col="var(--lime)", tag="Let&rsquo;s talk about this")))

for name, body in S:
    open(os.path.join(BASE, f"post3-{name}.html"), "w").write(HEAD + body)
    print("wrote", name)
