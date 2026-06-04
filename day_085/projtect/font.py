import os, sys
from PIL import ImageFont


def get_font(size):
    paths = {
        "win32":  ["C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arial.ttf"],
        "darwin": ["/Library/Fonts/Arial Bold.ttf", "/System/Library/Fonts/Helvetica.ttc"],
    }.get(sys.platform, [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ])
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()