from PIL import Image, ImageDraw
import math, os

OUT = "icons"
os.makedirs(OUT, exist_ok=True)

BG = (15, 17, 21, 255)      # #0f1115
ACCENT = (217, 164, 65, 255)  # #d9a441
ACCENT_DIM = (122, 92, 38, 255)
TEXT = (242, 236, 225, 255)

def draw_glyph(size, padding_frac, bg_full=False):
    """Draw a simple singing-bowl / bell glyph with concentric sound rings."""
    img = Image.new("RGBA", (size, size), BG if bg_full else (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if not bg_full:
        # rounded-square backdrop for non-maskable icons
        pad = int(size * 0.0)
        draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * 0.22), fill=BG)

    cx, cy = size / 2, size / 2
    pad = size * padding_frac

    # Bowl: a filled ellipse (bottom half) representing a singing bowl
    bowl_w = size - 2 * pad
    bowl_h = bowl_w * 0.42
    bowl_top = cy + size * 0.02
    draw.ellipse(
        [cx - bowl_w / 2, bowl_top - bowl_h / 2, cx + bowl_w / 2, bowl_top + bowl_h / 2],
        fill=ACCENT,
    )
    # slight rim highlight
    rim_h = bowl_h * 0.5
    draw.ellipse(
        [cx - bowl_w / 2, bowl_top - rim_h / 2, cx + bowl_w / 2, bowl_top + rim_h / 2],
        outline=(35, 26, 10, 255),
        width=max(1, int(size * 0.006)),
    )

    # Concentric sound-wave arcs above the bowl
    ring_colors = [ACCENT, ACCENT_DIM]
    base_r = bowl_w * 0.28
    for i in range(3):
        r = base_r + i * (size * 0.085)
        bbox = [cx - r, bowl_top - r * 0.75, cx + r, bowl_top + r * 0.75]
        width = max(2, int(size * (0.028 - i * 0.006)))
        color = ring_colors[0] if i == 0 else ring_colors[1]
        draw.arc(bbox, start=200, end=340, fill=color, width=width)

    return img

def save(img, path):
    img.save(path, "PNG")
    print("wrote", path, img.size)

# Standard (any-purpose) icons: safe padding, rounded-square backdrop baked in
for size, name in [(192, "icon-192.png"), (512, "icon-512.png"), (180, "icon-180.png")]:
    img = draw_glyph(size, padding_frac=0.16, bg_full=False)
    save(img, os.path.join(OUT, name))

# Maskable icons: full-bleed background, glyph kept within the safe zone (~40% radius)
for size, name in [(192, "icon-192-maskable.png"), (512, "icon-512-maskable.png")]:
    img = draw_glyph(size, padding_frac=0.26, bg_full=True)
    save(img, os.path.join(OUT, name))
