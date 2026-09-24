"""True Tech Solutions glass-door sticker: 42 x 74 in trim, 0.5 in bleed. Units: 0.01 in.

Layers (top-level groups):
  FROST_VINYL        - full-area frosted/etched vinyl, with the handle cut-out
  PRINT              - full-colour artwork printed on top
  GUIDES_do_not_print- trim line, safe area, handle keep-out zone
"""
from lib import text, text_width, icon, mark, MARK_GRADIENT
import cairosvg, sys

TW, TH, B = 4200, 7400, 50
W, H = TW + 2 * B, TH + 2 * B
NAVY, CYAN, DEEP, GREY = '#0143a3', '#05a5fd', '#012d74', '#3f454c'
PHONE = sys.argv[1] if len(sys.argv) > 1 else '+92 51 6109291'
X = lambda v: v + B
Y = lambda v: v + B

# Handle keep-out zone in trim coordinates (right-hand pull handle, as in the mock-up).
# Measure the real door and adjust these four numbers before printing.
HX0, HX1, HY0, HY1 = 3600, TW, 2750, 4650
SAFE = 150

art = []

# ---------- Corner sweep (top-left) ----------
art.append('<g id="Top_Sweep">'
           f'<path fill="{NAVY}" d="M0,0 H{X(1500)} C{X(900)},{Y(120)} {X(300)},{Y(500)} 0,{Y(1050)} Z"/>'
           f'<path fill="{CYAN}" d="M{X(1700)},0 H{X(1850)} C{X(1000)},{Y(150)} {X(350)},{Y(650)} 0,{Y(1400)} V{Y(1230)} C{X(350)},{Y(560)} {X(950)},{Y(110)} {X(1700)},0 Z"/>'
           '</g>')

# ---------- Logo lock-up + ISO badge ----------
badge_r = 290
lock_max = TW - 2 * 300 - 2 * badge_r - 250          # room left of the badge


def lockup_width(cap):
    _, mw = mark(0, 0, cap * 2.8)
    return mw + 0.37 * cap + text_width('TRUE TECH', 800, cap) + 0.30 * cap + text_width('SOLUTIONS', 400, cap)


cap = lock_max / lockup_width(1)
mark_h = cap * 2.8
x0, mark_top = 300, 1150
base = mark_top + 0.595 * mark_h
m, mw = mark(X(x0), Y(mark_top), mark_h)
tx = x0 + mw + 0.37 * cap
d1, w_true = text('TRUE TECH', 800, cap, X(tx), Y(base))
d2, _ = text('SOLUTIONS', 400, cap, X(tx + w_true + 0.30 * cap), Y(base))
d3, _ = text('Building Trust & Relationships', 500, cap * 0.52, X(tx + 3), Y(base + cap * 1.17))
art.append(f'<g id="Logo">{m}<path fill="{NAVY}" d="{d1}"/><path fill="{NAVY}" d="{d2}"/>'
           f'<path fill="{GREY}" d="{d3}"/></g>')

bx, by = TW - 300 - badge_r, mark_top + mark_h / 2
sep_x = bx - badge_r - 125
t_iso, _ = text('ISO', 800, 120, X(bx), Y(by - 10), 'middle')
t_std, _ = text('9001:2015', 700, 50, X(bx), Y(by + 75), 'middle')
t_cer, _ = text('CERTIFIED', 600, 30, X(bx), Y(by + 140), 'middle', tracking=0.2)
art.append(f'<rect id="Divider" x="{X(sep_x) - 4:.1f}" y="{Y(mark_top):.1f}" width="8" height="{mark_h:.1f}" fill="{NAVY}"/>')
art.append('<g id="ISO_Badge_REPLACE_WITH_OFFICIAL_MARK">'
           f'<circle cx="{X(bx)}" cy="{Y(by):.1f}" r="{badge_r}" fill="#ffffff" stroke="{NAVY}" stroke-width="22"/>'
           f'<circle cx="{X(bx)}" cy="{Y(by):.1f}" r="{badge_r - 45}" fill="none" stroke="{NAVY}" stroke-width="6"/>'
           f'<path fill="{NAVY}" d="{t_iso}"/><path fill="{NAVY}" d="{t_std}"/><path fill="{NAVY}" d="{t_cer}"/></g>')

# ---------- Service banners ----------
services = [(0xf233, 'TURNKEY IT INFRASTRUCTURE'),
            (0xf03d, 'SECURITY & SURVEILLANCE'),
            (0xf080, 'ERP & CRM SOLUTIONS'),
            (0xf0eb, 'SOLUTION DESIGN CONSULTANCY'),
            (0xf1b3, 'SYSTEM INTEGRATION')]
row_top, pitch, band_h, circ_r = 1900, 540, 340, 215
left = 380
right = HX0 - SAFE                                   # banners stop before the handle zone
text_x = left + 2 * circ_r + 130
tcap = min(115, (right - 200 - text_x) / max(text_width(s, 700, 1) for _, s in services))
rows = []
for i, (code, label) in enumerate(services):
    cy = row_top + i * pitch + circ_r
    top, bot = cy - band_h / 2, cy + band_h / 2
    # pale band with slanted right end, navy wedge on the left, cyan slash on the right
    rows.append(f'<path fill="#ffffff" fill-opacity="0.92" d="M{X(left + circ_r)},{Y(top):.1f} H{X(right):.1f} L{X(right - 110):.1f},{Y(bot):.1f} H{X(left + circ_r)} Z"/>')
    rows.append(f'<path fill="{NAVY}" d="M{X(left + circ_r)},{Y(top):.1f} H{X(left + 2 * circ_r + 20)} L{X(left + 2 * circ_r + 90)},{Y(bot):.1f} H{X(left + circ_r)} Z"/>')
    rows.append(f'<path fill="{CYAN}" d="M{X(right + 20):.1f},{Y(top):.1f} H{X(right + 80):.1f} L{X(right - 30):.1f},{Y(bot):.1f} H{X(right - 90):.1f} Z"/>')
    rows.append(f'<circle cx="{X(left + circ_r)}" cy="{Y(cy):.1f}" r="{circ_r}" fill="{NAVY}" stroke="#ffffff" stroke-width="18"/>')
    rows.append(f'<path fill="#ffffff" d="{icon(code, 210, X(left + circ_r), Y(cy))}"/>')
    d, _ = text(label, 700, tcap, X(text_x), Y(cy + tcap / 2))
    rows.append(f'<path fill="{DEEP}" d="{d}"/>')
art.append(f'<g id="Services">{"".join(rows)}</g>')

# ---------- Bottom wave + contact panel ----------
wy = 4700
art.append('<g id="Bottom_Panel">'
           f'<path fill="{CYAN}" d="M0,{Y(wy)} C{X(1300)},{Y(wy + 380)} {X(2900)},{Y(wy + 330)} {W},{Y(wy + 70)} V{H} H0 Z"/>'
           f'<path fill="#ffffff" d="M0,{Y(wy + 90)} C{X(1300)},{Y(wy + 460)} {X(2900)},{Y(wy + 410)} {W},{Y(wy + 160)} V{H} H0 Z"/>'
           f'<path fill="{NAVY}" d="M0,{Y(wy + 140)} C{X(1300)},{Y(wy + 500)} {X(2900)},{Y(wy + 450)} {W},{Y(wy + 210)} V{H} H0 Z"/>'
           f'<path fill="{DEEP}" d="M0,{Y(6300)} C{X(1400)},{Y(6450)} {X(2800)},{Y(6450)} {W},{Y(6300)} V{H} H0 Z" opacity="0.6"/>'
           '</g>')
contacts = [(0xf095, PHONE), (0xf0ac, 'www.truetech-sol.com'), (0xf0e0, 'info@truetech-sol.com')]
col_w = (TW - 2 * SAFE) / 3
ccap = min(78, 0.86 * col_w / max(text_width(s, 600, 1) for _, s in contacts))
cells = []
for i, (code, label) in enumerate(contacts):
    cx = SAFE + col_w * (i + 0.5)
    cells.append(f'<circle cx="{X(cx):.1f}" cy="{Y(5380)}" r="125" fill="none" stroke="#ffffff" stroke-width="14"/>')
    cells.append(f'<path fill="#ffffff" d="{icon(code, 120, X(cx), Y(5380))}"/>')
    d, _ = text(label, 600, ccap, X(cx), Y(5660), 'middle')
    cells.append(f'<path fill="#ffffff" d="{d}"/>')
    if i:
        cells.append(f'<rect x="{X(SAFE + col_w * i) - 4:.1f}" y="{Y(5290)}" width="8" height="430" fill="#ffffff" fill-opacity="0.7"/>')
art.append(f'<g id="Contact">{"".join(cells)}</g>')

# ---------- Frosted vinyl layer with handle cut-out ----------
hole = f'M{X(HX0):.0f},{Y(HY0)} H{W} V{Y(HY1)} H{X(HX0):.0f} Z'
frost = (f'<g id="FROST_VINYL"><path fill="#dfe8f1" fill-rule="evenodd" '
         f'd="M0,0 H{W} V{H} H0 Z {hole}"/></g>')

guides = ('<g id="GUIDES_do_not_print" fill="none" stroke-width="5">'
          f'<rect x="{B}" y="{B}" width="{TW}" height="{TH}" stroke="#e5007e" stroke-dasharray="30,18"/>'
          f'<rect x="{B + SAFE}" y="{B + SAFE}" width="{TW - 2 * SAFE}" height="{TH - 2 * SAFE}" stroke="#00a0e0" stroke-dasharray="12,12"/>'
          f'<rect x="{X(HX0)}" y="{Y(HY0)}" width="{W - X(HX0)}" height="{HY1 - HY0}" stroke="#e5007e" stroke-width="8"/>')
lbl, _ = text('HANDLE', 700, 60, X((HX0 + TW) / 2), Y((HY0 + HY1) / 2 - 40), 'middle')
lbl2, _ = text('KEEP CLEAR', 700, 42, X((HX0 + TW) / 2), Y((HY0 + HY1) / 2 + 60), 'middle')
guides += f'<path fill="#e5007e" d="{lbl}"/><path fill="#e5007e" d="{lbl2}"/></g>'


def svg(with_guides, with_frost=True):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W / 100}in" height="{H / 100}in" viewBox="0 0 {W} {H}">\n'
            '<title>True Tech Solutions Door Sticker 42x74in (+0.5in bleed)</title>\n'
            f'<defs>{MARK_GRADIENT}</defs>\n' + (frost if with_frost else '') + '\n<g id="PRINT">' + '\n'.join(art) + '</g>\n'
            + (guides if with_guides else '') + '</svg>\n')


out = 'print/TrueTech_DoorSticker_42x74in'
open(out + '_PRINT.svg', 'w').write(svg(False))
open(out + '_PROOF_with_guides.svg', 'w').write(svg(True))
cairosvg.svg2pdf(bytestring=svg(False).encode(), write_to=out + '_PRINT_full_colour.pdf')
cairosvg.svg2pdf(bytestring=svg(False, False).encode(), write_to=out + '_PRINT_on_frosted_vinyl.pdf')
cairosvg.svg2png(url=out + '_PROOF_with_guides.svg', write_to=out + '_preview.png', output_width=1100)
print('ok', 'service cap', round(tcap), 'contact cap', round(ccap))
