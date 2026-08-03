#!/usr/bin/env python3
"""Post 4 — 'Should you fake orgasms to protect your partner's feelings?'
Slides 2-7, matching the dark gradient / Fraunces treatment of slide 1. 1080x1350."""
import os
BASE = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="fonts-embedded.css">
<style>
  :root{--pink:#FF30CC;--lime:#CCFD28;--cream:#FCF7ED;--ink:#282826;--custard:#FBEF82;}
  *{margin:0;padding:0;box-sizing:border-box}
  html,body{width:1080px;height:1350px}
  body{font-family:'DM Sans',sans-serif;color:var(--cream);overflow:hidden;position:relative;
       background:linear-gradient(180deg,#0f0b0f 0%,#170e16 30%,#3d1236 60%,#71195f 82%,#9c2183 100%)}

  /* film grain */
  .grain{position:absolute;inset:0;opacity:.16;pointer-events:none;z-index:1;
    background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/></filter><rect width='180' height='180' filter='url(%23n)' opacity='.55'/></svg>")}
  .glow{position:absolute;left:50%;bottom:-160px;transform:translateX(-50%);width:900px;height:520px;
        background:radial-gradient(ellipse at center,rgba(255,48,204,.34),transparent 70%);z-index:0}

  .frame{position:absolute;inset:0;padding:74px 84px 66px;display:flex;flex-direction:column;z-index:2}
  .logo{width:86px;height:86px;flex:none;border-radius:50%;overflow:hidden;object-fit:cover}
  .mid{flex:1;display:flex;flex-direction:column;justify-content:center}

  .kicker{font-family:'DM Sans';font-weight:700;font-size:20px;letter-spacing:.22em;text-transform:uppercase;
          color:var(--lime);margin-bottom:20px}
  .head{font-family:'Fraunces',serif;font-weight:900;text-transform:uppercase;letter-spacing:-.005em;
        line-height:1.06;color:var(--cream)}
  .body{font-size:31px;line-height:1.5;color:var(--cream);opacity:.9;max-width:860px;margin-top:26px;font-weight:400}
  .body b{font-weight:700;opacity:1;color:var(--custard)}

  .foot{display:flex;align-items:center;justify-content:space-between;margin-top:auto}
  .swipe{font-weight:500;font-size:24px;color:var(--lime)}
  .num{font-family:'Fraunces',serif;font-weight:900;font-size:24px;color:var(--cream);opacity:.4}
</style></head><body>
<div class="glow"></div>
<div class="grain"></div>
"""

def slide(num, kicker, head, head_size, body, last=False):
    swipe = "" if last else '<span class="swipe">swipe &rarr;</span>'
    tail = '<span class="swipe">@hellonancy</span>' if last else swipe
    return f'''
<div class="frame">
  <img class="logo" src="../assets/logo/Nancy_Logo_Circular_Pink.png">
  <div class="mid">
    {f'<div class="kicker">{kicker}</div>' if kicker else ''}
    <div class="head" style="font-size:{head_size}px">{head}</div>
    <div class="body">{body}</div>
  </div>
  <div class="foot">
    <span class="num">{num}</span>
    {tail}
  </div>
</div>
</body></html>'''

S = [
    ("s2", slide("02", "short answer",
        "No.",
        150,
        "It can feel like the kind thing in the moment. It usually just creates a bigger problem later.")),

    ("s3", slide("03", "here&rsquo;s why",
        "He thinks it&rsquo;s working.",
        76,
        "So he keeps doing it. Every time you fake it, you teach him that the thing that isn&rsquo;t working <b>is</b> working &mdash; and the real answer gets further away.")),

    ("s4", slide("04", "the trade",
        "Honesty beats performance.",
        70,
        "Pretending protects the moment. Being open builds the thing you actually want &mdash; two people who know what they&rsquo;re doing.")),

    ("s5", slide("05", "instead",
        "Guide, don&rsquo;t grade.",
        86,
        "You don&rsquo;t have to deliver a review. <b>&ldquo;I love it when you...&rdquo;</b> does more than a whole conversation about what went wrong.")),

    ("s6", slide("06", "also worth saying",
        "It isn&rsquo;t the only scoreboard.",
        66,
        "An orgasm isn&rsquo;t the only measure of good sex. Connection, trust and actually enjoying each other count too.")),

    ("s7", slide("07", "",
        "Protect his feelings by being honest with him.",
        66,
        "Not by pretending. That&rsquo;s the version that lasts.", last=True)),
]

for name, body in S:
    open(os.path.join(BASE, f"post4-{name}.html"), "w").write(HEAD + body)
    print("wrote", name)
