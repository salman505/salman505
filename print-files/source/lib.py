"""Helpers: outlined text (Montserrat), FontAwesome icons, traced logo mark."""
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import os

HERE = os.path.dirname(os.path.abspath(__file__))
_fonts = {}


def font(weight):
    if weight not in _fonts:
        vf = TTFont(os.path.join(HERE, 'fonts/Montserrat.ttf'))
        _fonts[weight] = instantiateVariableFont(vf, {'wght': weight})
    return _fonts[weight]


def text(s, weight, cap, x, y, anchor='start', tracking=0.0):
    """Outline `s` with baseline at y and cap height `cap` (in doc units).
    Returns (path_d, width)."""
    f = font(weight)
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    capH = f['OS/2'].sCapHeight
    k = cap / capH
    names = [cmap[ord(c)] for c in s]
    adv = [gs[n].width * k for n in names]
    track = tracking * cap
    width = sum(adv) + track * (len(s) - 1)
    x0 = {'start': x, 'middle': x - width / 2, 'end': x - width}[anchor]
    pen = SVGPathPen(gs, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.'))
    cx = x0
    for n, a in zip(names, adv):
        gs[n].draw(TransformPen(pen, (k, 0, 0, -k, cx, y)))
        cx += a + track
    return pen.getCommands(), width


def text_width(s, weight, cap, tracking=0.0):
    return text(s, weight, cap, 0, 0, tracking=tracking)[1]


_fa = None


def icon(code, size, cx, cy):
    """FontAwesome 4.7 glyph centred on (cx, cy), fitted into a size x size box."""
    global _fa
    if _fa is None:
        _fa = TTFont(os.path.join(HERE, 'odoo17/addons/web/static/src/libs/fontawesome/fonts/fontawesome-webfont.ttf'))
    gs = _fa.getGlyphSet()
    g = gs[_fa.getBestCmap()[code]]
    bp = BoundsPen(gs)
    g.draw(bp)
    xmin, ymin, xmax, ymax = bp.bounds
    k = size / max(xmax - xmin, ymax - ymin)
    ox = cx - (xmin + xmax) / 2 * k
    oy = cy + (ymin + ymax) / 2 * k
    pen = SVGPathPen(gs, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.'))
    g.draw(TransformPen(pen, (k, 0, 0, -k, ox, oy)))
    return pen.getCommands()


def mark(x, y, height):
    """Traced logo mark: returns (transform-wrapped <path> string, width)."""
    d, bb = open(os.path.join(HERE, 'mark_path.txt')).read().split('\n')
    bx, by, bw, bh = map(float, bb.split())
    k = height / bh
    w = bw * k
    g = (f'<g id="Logo_Mark" transform="translate({x:.2f},{y:.2f}) scale({k:.5f}) translate({-bx},{-by})">'
         f'<path fill="url(#markGrad)" fill-rule="evenodd" d="{d}"/></g>')
    return g, w


MARK_GRADIENT = ('<linearGradient id="markGrad" gradientUnits="objectBoundingBox" x1="0" y1="0.5" x2="1" y2="0.5">'
                 '<stop offset="0" stop-color="#0a64c8"/><stop offset="1" stop-color="#0143a3"/></linearGradient>')
