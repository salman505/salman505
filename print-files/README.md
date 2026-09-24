# True Tech Solutions – door plate and door sticker (print files)

All artwork is **100% vector**: no embedded images, and all text is converted to outlines,
so no fonts are needed. Files open in CorelDRAW (File → Import the `.svg`, or open the `.pdf`).

| File | Use |
|---|---|
| `TrueTech_DoorPlate_30x16in_PRINT.pdf` / `.svg` | **Door plate**: send to printer. 30 × 16 in trim + 0.25 in bleed (30.5 × 16.5 in page). |
| `TrueTech_DoorSticker_42x74in_PRINT_on_frosted_vinyl.pdf` | **Door sticker** (recommended): colour artwork only, printed on frosted/etched vinyl. |
| `TrueTech_DoorSticker_42x74in_PRINT_full_colour.pdf` | Door sticker alternative: includes a light "frost" tint for printing on clear or white vinyl. |
| `TrueTech_DoorSticker_42x74in_PRINT.svg` | Editable door sticker. Layers: `FROST_VINYL` (background with handle cut-out) and `PRINT` (artwork). |
| `*_PROOF_with_guides.svg`, `*_preview.png` | For checking only. Pink dashed line = trim, blue dotted line = safe area, pink box = handle keep-out. **Do not print.** |

## Notes for the printer

- Door sticker: 42 × 74 in trim + 0.5 in bleed (43 × 75 in page). Leave the handle area
  (right edge, 29–47 in from the top of the glass) **unprinted and cut out** around the handle fixings.
  **Measure the actual door and handle before printing**, then move the keep-out box if needed
  (`HX0, HX1, HY0, HY1` in `source/door.py`, or move it by hand in CorelDRAW).
- Colours (RGB → specify CMYK/Pantone with the printer): Navy `#0143A3`, Cyan `#05A5FD`, Deep navy `#012D74`.
- Font used (outlined): Montserrat (SIL Open Font License). Icons: Font Awesome 4.7 (SIL OFL).

## Before sending to print, please confirm

1. **Phone number:** +92 51 6109291 is used (as in your designs). The website lists +92 51 8747430.
   To change it: `python source/nameplate.py "+92 51 8747430"` and `python source/door.py "+92 51 8747430"`.
2. **ISO badge:** the group `ISO_Badge_REPLACE_WITH_OFFICIAL_MARK` is a simple text badge. Replace it with
   the official mark from your certification body if you have it.
3. **Logo:** the logo mark was traced to vector from your artwork. If you have the original logo file,
   swap it in for the best possible match.
