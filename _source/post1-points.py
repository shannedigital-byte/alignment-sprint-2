#!/usr/bin/env python3
"""Post 1 slides 2-9 — eight things worth knowing. Each slide gets its own visual device.
1080x1350, Hello Nancy brand kit."""
import os
BASE = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="fonts-embedded.css">
<style>
  :root{--pink:#FF30CC;--lime:#CCFD28;--cream:#FCF7ED;--ink:#282826;--custard:#FBEF82;
        --jam:#F3DCE2;--heart:#E94362;--dawn:#7E7F84;}
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{width:1080px;height:1350px}
  body{font-family:'DM Sans',sans-serif;color:var(--ink);overflow:hidden;position:relative}
  .frame{position:absolute;inset:0;padding:80px 80px 64px;display:flex;flex-direction:column;z-index:2}
  .badge{width:76px;height:76px;border-radius:50%;display:flex;align-items:center;justify-content:center;
         font-family:'Fraunces',serif;font-weight:900;font-size:36px;flex:none}
  .head{font-family:'Fraunces',serif;font-weight:900;line-height:1.06;letter-spacing:-.014em;margin-top:26px}
  .body{font-size:28px;line-height:1.45;margin-top:22px;max-width:880px}
  .body b{font-weight:700}
  .mid{flex:1;display:flex;align-items:center;justify-content:center;margin:20px 0}
  .foot{display:flex;align-items:center;justify-content:space-between;margin-top:auto}
  .wordmark{font-family:'Fraunces',serif;font-weight:900;font-style:italic;font-size:30px}
  .swipe{font-weight:700;font-size:22px}
  .photo{border-radius:50%;overflow:hidden;box-shadow:0 16px 40px rgba(40,40,38,.16)}
  .photo img{width:100%;height:100%;object-fit:cover}
  .chip{display:inline-flex;align-items:center;gap:12px;border-radius:100px;padding:14px 24px;
        font-weight:700;font-size:22px}
</style></head><body>
"""

def foot(wm="var(--pink)", sw="var(--ink)", last=False):
    txt = "@hellonancy" if last else "swipe &rarr;"
    return f'''
  <div class="foot">
    <span class="wordmark" style="color:{wm}">Nancy</span>
    <span class="swipe" style="color:{sw}">{txt}</span>
  </div>
</div>
</body></html>'''

S = []

# ---- 01  penetration alone  (ink bg, scale-comparison circles)
S.append(("s2", f'''
<style>body{{background:var(--ink)}} .head,.body{{color:var(--cream)}}</style>
<div class="frame">
  <div class="badge" style="background:var(--lime);color:var(--ink)">1</div>
  <div class="head" style="font-size:60px">Most women don&rsquo;t orgasm<br>from penetration alone.</div>
  <div class="body" style="font-size:26px">Clitoral stimulation plays a much bigger role in reaching orgasm than penetration by itself.</div>
  <div class="mid">
    <div style="display:flex;align-items:center;gap:40px">
      <div style="text-align:center">
        <div style="width:290px;height:290px;border-radius:50%;background:var(--pink);display:flex;
             align-items:center;justify-content:center;flex-direction:column;color:var(--cream)">
          <div style="font-family:'Fraunces',serif;font-weight:900;font-size:40px">External</div>
          <div style="font-size:17px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;margin-top:6px;opacity:.85">does the work</div>
        </div>
      </div>
      <div style="font-family:'Fraunces',serif;font-weight:900;font-style:italic;font-size:32px;color:var(--dawn)">vs</div>
      <div style="width:145px;height:145px;border-radius:50%;background:rgba(252,247,237,.16);display:flex;
           align-items:center;justify-content:center;color:var(--cream);text-align:center;
           font-family:'Fraunces',serif;font-weight:900;font-size:22px;line-height:1.15">Penetration<br>alone</div>
    </div>
  </div>
''' + foot(sw="var(--lime)")))

# ---- 02  arousal takes time  (lime bg, timeline arc)
S.append(("s3", f'''
<style>body{{background:var(--lime)}}</style>
<div class="frame">
  <div class="badge" style="background:var(--ink);color:var(--lime)">2</div>
  <div class="head" style="font-size:66px">Arousal takes time.</div>
  <div class="body">Unlike what movies show, it&rsquo;s completely normal for arousal to build gradually. <b>There&rsquo;s no &ldquo;right&rdquo; timeline.</b></div>
  <div class="mid">
    <svg width="820" height="300" viewBox="0 0 820 300">
      <path d="M60 250 A350 210 0 0 1 760 250" stroke="rgba(40,40,38,.22)" stroke-width="16" fill="none" stroke-linecap="round"/>
      <path d="M60 250 A350 210 0 0 1 560 78" stroke="#FF30CC" stroke-width="16" fill="none" stroke-linecap="round"/>
      <circle cx="60" cy="250" r="16" fill="#282826"/>
      <circle cx="560" cy="78" r="22" fill="#FF30CC" stroke="#282826" stroke-width="6"/>
      <text x="46" y="292" font-family="DM Sans" font-size="24" font-weight="700" fill="#282826">start</text>
      <text x="470" y="46" font-family="Fraunces" font-size="40" font-weight="900" fill="#282826">20+ min</text>
      <text x="690" y="292" font-family="DM Sans" font-size="24" font-weight="700" fill="#282826" opacity=".6">no rush</text>
    </svg>
  </div>
''' + foot(wm="var(--ink)")))

# ---- 03  every body is different  (cream bg, two products + wave icons)
S.append(("s4", f'''
<style>body{{background:var(--cream)}}</style>
<div class="frame">
  <div class="badge" style="background:var(--pink);color:var(--cream)">3</div>
  <div class="head" style="font-size:66px">Every body is different.</div>
  <div class="body">What feels amazing for one person may do nothing for someone else. <b>Pleasure isn&rsquo;t one-size-fits-all.</b></div>
  <div class="mid">
    <div style="display:flex;gap:56px;align-items:flex-start">
      <div style="text-align:center">
        <div class="photo" style="width:250px;height:250px"><img src="../assets/product-photos/lem-front.png" style="object-position:center 46%;transform:scale(1.1)"></div>
        <svg width="70" height="34" viewBox="0 0 70 34" style="margin-top:18px"><path d="M4 17 Q14 2 24 17 T44 17 T66 17" stroke="#FF30CC" stroke-width="6" fill="none" stroke-linecap="round"/></svg>
        <div style="font-weight:700;font-size:21px;margin-top:4px">steady pressure</div>
      </div>
      <div style="text-align:center">
        <div class="photo" style="width:250px;height:250px"><img src="../assets/product-photos/berri-front.png" style="object-position:center 50%;transform:scale(1.1)"></div>
        <svg width="70" height="34" viewBox="0 0 70 34" style="margin-top:18px"><circle cx="12" cy="17" r="7" fill="#E94362"/><circle cx="35" cy="17" r="7" fill="#E94362"/><circle cx="58" cy="17" r="7" fill="#E94362"/></svg>
        <div style="font-weight:700;font-size:21px;margin-top:4px">rhythmic tapping</div>
      </div>
    </div>
  </div>
''' + foot()))

# ---- 04  communication  (pink bg, speech bubbles)
S.append(("s5", f'''
<style>body{{background:var(--pink)}} .head{{color:var(--cream)}} .body{{color:var(--custard)}}
  .bub{{border-radius:30px;padding:24px 30px;font-size:26px;font-weight:600;max-width:620px;position:relative}}
</style>
<div class="frame">
  <div class="badge" style="background:var(--custard);color:var(--ink)">4</div>
  <div class="head" style="font-size:64px">Communication is part<br>of good sex.</div>
  <div class="body">Your partner can&rsquo;t read your mind. Talking about what you enjoy often leads to a better experience <b style="color:var(--cream)">for both of you.</b></div>
  <div class="mid">
    <div style="display:flex;flex-direction:column;gap:24px;width:100%">
      <div class="bub" style="background:var(--cream);color:var(--ink);align-self:flex-start;border-bottom-left-radius:8px">
        &ldquo;I really like it when you do that.&rdquo;</div>
      <div class="bub" style="background:rgba(252,247,237,.18);color:var(--cream);align-self:flex-end;border-bottom-right-radius:8px">
        &ldquo;Can we stay here a little longer?&rdquo;</div>
      <div class="bub" style="background:var(--custard);color:var(--ink);align-self:flex-start;border-bottom-left-radius:8px">
        &ldquo;Try a little softer.&rdquo;</div>
    </div>
  </div>
''' + foot(wm="var(--cream)", sw="var(--custard)")))

# ---- 05  self-exploration  (custard bg, in-hand photo card)
S.append(("s6", f'''
<style>body{{background:var(--custard)}}</style>
<div class="frame">
  <div class="badge" style="background:var(--ink);color:var(--custard)">5</div>
  <div class="head" style="font-size:66px">Self-exploration<br>is healthy.</div>
  <div class="body">Understanding your own body helps you communicate your preferences <b>and build confidence during intimacy.</b></div>
  <div class="mid">
    <div style="width:100%;border-radius:38px;overflow:hidden;box-shadow:0 20px 46px rgba(40,40,38,.16);height:330px;position:relative">
      <img src="../assets/product-photos/lem-inhand.png" style="width:112%;position:absolute;left:-6%;top:-6%">
    </div>
  </div>
''' + foot()))

# ---- 06  lube  (jam bg, friction meter + droplets)
S.append(("s7", f'''
<style>body{{background:var(--jam)}}</style>
<div class="frame">
  <div class="badge" style="background:var(--heart);color:var(--cream)">6</div>
  <div class="head" style="font-size:64px">Lubricant isn&rsquo;t just<br>for dryness.</div>
  <div class="body">Lube increases comfort and reduces friction, making intimacy more enjoyable <b>for many people, regardless of age.</b></div>
  <div class="mid">
    <div style="width:100%">
      <div style="display:flex;justify-content:space-between;font-weight:700;font-size:22px;margin-bottom:14px">
        <span>more friction</span><span style="color:var(--heart)">more comfort</span>
      </div>
      <div style="height:34px;border-radius:100px;background:linear-gradient(90deg,rgba(40,40,38,.22),#E94362)"></div>
      <div style="display:flex;justify-content:center;gap:34px;margin-top:40px">
        <svg width="70" height="90" viewBox="0 0 70 90"><path d="M35 4 C58 36 66 50 66 60 A31 31 0 0 1 4 60 C4 50 12 36 35 4Z" fill="#E94362" opacity=".85"/></svg>
        <svg width="56" height="72" viewBox="0 0 70 90"><path d="M35 4 C58 36 66 50 66 60 A31 31 0 0 1 4 60 C4 50 12 36 35 4Z" fill="#FF30CC" opacity=".7"/></svg>
        <svg width="42" height="54" viewBox="0 0 70 90"><path d="M35 4 C58 36 66 50 66 60 A31 31 0 0 1 4 60 C4 50 12 36 35 4Z" fill="#282826" opacity=".3"/></svg>
      </div>
    </div>
  </div>
''' + foot()))

# ---- 07  stress  (ink bg, tangle → straight line)
S.append(("s8", f'''
<style>body{{background:var(--ink)}} .head,.body{{color:var(--cream)}}</style>
<div class="frame">
  <div class="badge" style="background:var(--pink);color:var(--cream)">7</div>
  <div class="head" style="font-size:64px">Stress can affect<br>pleasure.</div>
  <div class="body">Anxiety, fatigue and relationship stress all make it harder to become aroused or orgasm. <b style="color:var(--lime)">That&rsquo;s completely normal.</b></div>
  <div class="mid">
    <svg width="860" height="260" viewBox="0 0 860 260">
      <path d="M40 130 C90 40 120 220 170 120 C210 40 240 210 290 110 C330 40 360 200 410 130"
            stroke="#FF30CC" stroke-width="10" fill="none" stroke-linecap="round"/>
      <text x="40" y="228" font-family="DM Sans" font-size="23" font-weight="700" fill="#FCF7ED" opacity=".65">mental load</text>
      <path d="M470 130 H820" stroke="rgba(252,247,237,.25)" stroke-width="10" stroke-linecap="round" stroke-dasharray="4 26"/>
      <text x="470" y="228" font-family="DM Sans" font-size="23" font-weight="700" fill="#CCFD28">what's left for you</text>
    </svg>
  </div>
''' + foot(sw="var(--lime)")))

# ---- 08  closing  (pink bg, checklist)
S.append(("s9", f'''
<style>body{{background:var(--pink)}} .head{{color:var(--cream)}} .body{{color:var(--custard)}}
  .tick{{display:flex;align-items:center;gap:18px;font-size:29px;font-weight:700;color:var(--cream)}}
</style>
<div class="frame">
  <div class="badge" style="background:var(--custard);color:var(--ink)">8</div>
  <div class="head" style="font-size:62px">Pleasure isn&rsquo;t measured<br>by orgasm.</div>
  <div class="body">A satisfying experience isn&rsquo;t only about reaching orgasm. <b style="color:var(--cream)">These matter just as much.</b></div>
  <div class="mid">
    <div style="display:flex;flex-direction:column;gap:26px;width:100%">
      <div class="tick"><svg width="42" height="42" viewBox="0 0 42 42"><circle cx="21" cy="21" r="19" fill="none" stroke="#FBEF82" stroke-width="4"/><path d="M12 22 L18 28 L30 15" stroke="#FBEF82" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>Feeling safe</div>
      <div class="tick"><svg width="42" height="42" viewBox="0 0 42 42"><circle cx="21" cy="21" r="19" fill="none" stroke="#FBEF82" stroke-width="4"/><path d="M12 22 L18 28 L30 15" stroke="#FBEF82" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>Feeling connected</div>
      <div class="tick"><svg width="42" height="42" viewBox="0 0 42 42"><circle cx="21" cy="21" r="19" fill="none" stroke="#FBEF82" stroke-width="4"/><path d="M12 22 L18 28 L30 15" stroke="#FBEF82" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>Feeling respected</div>
      <div class="tick"><svg width="42" height="42" viewBox="0 0 42 42"><circle cx="21" cy="21" r="19" fill="none" stroke="#FBEF82" stroke-width="4"/><path d="M12 22 L18 28 L30 15" stroke="#FBEF82" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>Actually enjoying it</div>
    </div>
  </div>
''' + foot(wm="var(--cream)", sw="var(--custard)", last=True)))

for name, body in S:
    open(os.path.join(BASE, f"post1-{name}.html"), "w").write(HEAD + body)
    print("wrote", name)
