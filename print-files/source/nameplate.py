"""True Tech Solutions door plate: 30 x 16 in trim, 0.25 in bleed. Units: 0.01 in."""
from lib import text, text_width, icon, mark, MARK_GRADIENT
import cairosvg, sys

TW, TH, B = 3000, 1600, 25          # trim size and bleed
W, H = TW + 2 * B, TH + 2 * B
NAVY, CYAN, DEEP, GREY = '#0143a3', '#05a5fd', '#012d74', '#4a4f55'
PHONE = sys.argv[1] if len(sys.argv) > 1 else '+92 51 6109291'
X = lambda v: v + B                  # trim coords -> artboard coords
Y = lambda v: v + B

art = []

# Background (runs into bleed)
art.append(f'<rect id="Background" x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')

# Top-left corner accent: kept small so it clears the logo
art.append(f'<g id="Corner_Accent">'
           f'<path fill="{NAVY}" d="M0,0 H{X(240)} L0,{Y(200)} Z"/>'
           f'<path fill="{CYAN}" d="M{X(290)},0 H{X(360)} L0,{Y(300)} V{Y(242)} Z"/>'
           f'</g>')

# Bottom wave: light cyan swoosh over a navy base, both bleeding off the edges
art.append('<g id="Bottom_Wave">'
           f'<path fill="{CYAN}" d="M0,{Y(1150)} C{X(900)},{Y(1420)} {X(2100)},{Y(1420)} {W},{Y(1150)} V{H} H0 Z"/>'
           f'<path fill="#ffffff" d="M0,{Y(1215)} C{X(900)},{Y(1465)} {X(2100)},{Y(1465)} {W},{Y(1215)} V{H} H0 Z"/>'
           f'<path fill="{NAVY}" d="M0,{Y(1250)} C{X(900)},{Y(1490)} {X(2100)},{Y(1490)} {W},{Y(1250)} V{H} H0 Z"/>'
           f'<path fill="{DEEP}" d="M0,{Y(1420)} C{X(1000)},{Y(1560)} {X(2000)},{Y(1560)} {W},{Y(1420)} V{H} H0 Z" opacity="0.55"/>'
           '</g>')

# Logo lock-up, centred horizontally and scaled to fit 25.5 in
def lockup_width(cap):
    _, mw = mark(0, 0, cap * 2.8)
    return mw + 0.37 * cap + text_width('TRUE TECH', 800, cap) + 0.30 * cap + text_width('SOLUTIONS', 400, cap)
cap = 150 * min(1, 2550 / lockup_width(150))
mark_h = cap * 2.8
gap_mark, gap_word = 0.37 * cap, 0.30 * cap
w_true = text_width('TRUE TECH', 800, cap)
_, mark_w = mark(0, 0, mark_h)
total = lockup_width(cap)
x0 = (TW - total) / 2
mark_top = 340
base = mark_top + 0.595 * mark_h            # wordmark baseline
m, _ = mark(X(x0), Y(mark_top), mark_h)
tx = x0 + mark_w + gap_mark
d1, _ = text('TRUE TECH', 800, cap, X(tx), Y(base))
d2, _ = text('SOLUTIONS', 400, cap, X(tx + w_true + gap_word), Y(base))
art.append(f'<g id="Logo">{m}<path fill="{NAVY}" d="{d1}"/><path fill="{NAVY}" d="{d2}"/></g>')

# Tagline aligned under the wordmark
d3, _ = text('Building Trust & Relationships', 500, cap * 0.52, X(tx + 4), Y(base + cap * 1.17))
art.append(f'<path id="Tagline" fill="{GREY}" d="{d3}"/>')

# Contact row, centred
ccap = 62
r = 52
w_ph = text_width(PHONE, 500, ccap)
w_web = text_width('www.truetech-sol.com', 500, ccap)
sep = 90
row = (2 * r + 30 + w_ph) + sep + (2 * r + 30 + w_web)
cx = (TW - row) / 2
cy = 960
parts = []
for code, label, w in ((0xf095, PHONE, w_ph), (0xf0ac, 'www.truetech-sol.com', w_web)):
    parts.append(f'<circle cx="{X(cx + r):.1f}" cy="{Y(cy):.1f}" r="{r}" fill="{NAVY}"/>')
    parts.append(f'<path fill="#ffffff" d="{icon(code, 58, X(cx + r), Y(cy))}"/>')
    d, _ = text(label, 500, ccap, X(cx + 2 * r + 30), Y(cy + ccap / 2))
    parts.append(f'<path fill="#2b3036" d="{d}"/>')
    cx += 2 * r + 30 + w
    if label == PHONE:
        parts.append(f'<rect x="{X(cx + sep / 2 - 3):.1f}" y="{Y(cy - 55)}" width="6" height="110" fill="{NAVY}"/>')
        cx += sep
art.append(f'<g id="Contact">{"".join(parts)}</g>')

guides = (f'<g id="GUIDES_do_not_print" fill="none" stroke-width="3">'
          f'<rect x="{B}" y="{B}" width="{TW}" height="{TH}" stroke="#e5007e" stroke-dasharray="20,12"/>'
          f'<rect x="{B + 75}" y="{B + 75}" width="{TW - 150}" height="{TH - 150}" stroke="#00a0e0" stroke-dasharray="8,8"/>'
          '</g>')


def svg(with_guides):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W / 100}in" height="{H / 100}in" viewBox="0 0 {W} {H}">\n'
            f'<title>True Tech Solutions Door Plate 30x16in (+0.25in bleed)</title>\n'
            f'<defs>{MARK_GRADIENT}</defs>\n<g id="ARTWORK">' + '\n'.join(art) + '</g>\n'
            + (guides if with_guides else '') + '</svg>\n')


out = 'print/TrueTech_DoorPlate_30x16in'
open(out + '_PRINT.svg', 'w').write(svg(False))
open(out + '_PROOF_with_guides.svg', 'w').write(svg(True))
cairosvg.svg2pdf(url=out + '_PRINT.svg', write_to=out + '_PRINT.pdf')
cairosvg.svg2png(url=out + '_PROOF_with_guides.svg', write_to=out + '_preview.png', output_width=1600)
print('ok', W, H)
