from PIL import Image, ImageDraw

from .font import get_font
from .positions import POSITIONS


def add_watermark(image: Image.Image, text: str, size: int,
                  color: str, opacity: int, position: str) -> Image.Image:
    img = image.convert("RGBA")
    W, H = img.size

    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw  = ImageDraw.Draw(layer)
    font  = get_font(size)

    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    fill = (r, g, b, int(opacity * 2.55))

    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]

    if position == "Tile":
        step_x, step_y = tw + 60, th + 40
        for y in range(0, H + step_y, step_y):
            for x in range(0, W + step_x, step_x):
                draw.text((x, y), text, font=font, fill=fill)
    else:
        rx, ry, anchor = POSITIONS[position]
        draw.text((W * rx, H * ry), text, font=font, fill=fill, anchor=anchor)

    return Image.alpha_composite(img, layer).convert("RGB")