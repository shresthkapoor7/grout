"""
make_gif_3x6.py

For a sprite sheet arranged as 3 rows x 6 columns = 18 frames.

Install:
    pip install pillow

Run:
    python make_gif_3x6.py

Input:
    sprite_sheet.png

Outputs:
    animation.gif
    frames/frame_001.png ...
    debug_frames/frame_001_raw.png ...
    debug_sheet_crop.png
"""

from pathlib import Path
from collections import Counter
from PIL import Image


INPUT_FILE = "sprite_sheet.png"
OUTPUT_GIF = "animation.gif"

FRAMES_DIR = "frames"
DEBUG_FRAMES_DIR = "debug_frames"

# Your current sheet layout
ROWS = 3
COLS = 6
FRAME_COUNT = 18

# Higher = slower animation
FRAME_DELAY_MS = 130

# Use 2 if you want a bigger pixel-art GIF
SCALE = 1

# If using the actual downloaded image, keep this None.
# If using a screenshot with borders, set this manually:
# SHEET_CROP_BOX = (left, top, right, bottom)
SHEET_CROP_BOX = None

# Fake checkerboard background removal.
# Start low so it does not eat the dark hoodie.
BG_TOLERANCE = 10
BG_COLOR_COUNT = 8

# Global crop padding around all frames
PADDING = 8

# If True, keeps every frame as full cell size.
# If False, crops the whole animation to shared content bounds.
KEEP_FULL_CELL_SIZE = False


def color_distance(c1: tuple[int, int, int], c2: tuple[int, int, int]) -> int:
    return sum(abs(a - b) for a, b in zip(c1, c2))


def load_sheet() -> Image.Image:
    sheet = Image.open(INPUT_FILE).convert("RGBA")

    if SHEET_CROP_BOX is not None:
        sheet = sheet.crop(SHEET_CROP_BOX)

    sheet.save("debug_sheet_crop.png")
    return sheet


def get_grid_bounds(total: int, parts: int) -> list[int]:
    """
    Uses rounded proportional boundaries instead of total // parts.
    This avoids drift when image dimensions are not perfectly divisible.
    """
    return [round(i * total / parts) for i in range(parts + 1)]


def split_grid(sheet: Image.Image) -> list[Image.Image]:
    width, height = sheet.size

    x_bounds = get_grid_bounds(width, COLS)
    y_bounds = get_grid_bounds(height, ROWS)

    Path(DEBUG_FRAMES_DIR).mkdir(exist_ok=True)

    frames = []
    idx = 0

    for row in range(ROWS):
        for col in range(COLS):
            if idx >= FRAME_COUNT:
                break

            left = x_bounds[col]
            right = x_bounds[col + 1]
            top = y_bounds[row]
            bottom = y_bounds[row + 1]

            frame = sheet.crop((left, top, right, bottom)).convert("RGBA")

            idx += 1
            frame.save(Path(DEBUG_FRAMES_DIR) / f"frame_{idx:03}_raw.png")
            frames.append(frame)

    return frames


def get_border_colors(img: Image.Image) -> list[tuple[int, int, int]]:
    pixels = img.load()
    w, h = img.size

    colors = []

    for x in range(w):
        colors.append(pixels[x, 0][:3])
        colors.append(pixels[x, h - 1][:3])

    for y in range(h):
        colors.append(pixels[0, y][:3])
        colors.append(pixels[w - 1, y][:3])

    return colors


def get_likely_background_colors(frames: list[Image.Image]) -> list[tuple[int, int, int]]:
    """
    Finds the most common border colors across all frames.
    For fake transparency checkerboards, this usually detects the two checker colors.
    """
    all_border_colors = []

    for frame in frames:
        all_border_colors.extend(get_border_colors(frame))

    counts = Counter(all_border_colors)
    return [color for color, _ in counts.most_common(BG_COLOR_COUNT)]


def remove_checkerboard_background(
    frame: Image.Image,
    bg_colors: list[tuple[int, int, int]],
) -> Image.Image:
    """
    Removes fake checkerboard background by making likely bg colors transparent.
    """
    frame = frame.convert("RGBA")
    pixels = frame.load()
    w, h = frame.size

    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            current = (r, g, b)

            if any(color_distance(current, bg) <= BG_TOLERANCE for bg in bg_colors):
                pixels[x, y] = (r, g, b, 0)

    return frame


def global_crop(frames: list[Image.Image]) -> list[Image.Image]:
    """
    Crops all frames using one shared crop box.
    This prevents jitter from per-frame cropping.
    """
    if KEEP_FULL_CELL_SIZE:
        return frames

    bboxes = []

    for frame in frames:
        bbox = frame.getchannel("A").getbbox()
        if bbox is not None:
            bboxes.append(bbox)

    if not bboxes:
        return frames

    left = min(b[0] for b in bboxes)
    top = min(b[1] for b in bboxes)
    right = max(b[2] for b in bboxes)
    bottom = max(b[3] for b in bboxes)

    left = max(0, left - PADDING)
    top = max(0, top - PADDING)
    right = min(frames[0].width, right + PADDING)
    bottom = min(frames[0].height, bottom + PADDING)

    return [frame.crop((left, top, right, bottom)) for frame in frames]


def scale_frames(frames: list[Image.Image]) -> list[Image.Image]:
    if SCALE == 1:
        return frames

    scaled = []

    for frame in frames:
        w, h = frame.size
        scaled.append(
            frame.resize((w * SCALE, h * SCALE), Image.Resampling.NEAREST)
        )

    return scaled


def save_frames(frames: list[Image.Image]) -> None:
    Path(FRAMES_DIR).mkdir(exist_ok=True)

    for i, frame in enumerate(frames, start=1):
        frame.save(Path(FRAMES_DIR) / f"frame_{i:03}.png")


def save_gif(frames: list[Image.Image]) -> None:
    frames[0].save(
        OUTPUT_GIF,
        save_all=True,
        append_images=frames[1:],
        duration=FRAME_DELAY_MS,
        loop=0,
        disposal=2,
    )


def main() -> None:
    sheet = load_sheet()
    print(f"Sheet size: {sheet.size}")

    frames = split_grid(sheet)

    bg_colors = get_likely_background_colors(frames)
    print(f"Detected background colors: {bg_colors}")

    frames = [
        remove_checkerboard_background(frame, bg_colors)
        for frame in frames
    ]

    frames = global_crop(frames)
    frames = scale_frames(frames)

    save_frames(frames)
    save_gif(frames)

    print(f"Saved GIF: {OUTPUT_GIF}")
    print(f"Saved cleaned frames to: {FRAMES_DIR}/")
    print(f"Saved raw frames to: {DEBUG_FRAMES_DIR}/")
    print("Saved cropped sheet preview: debug_sheet_crop.png")


if __name__ == "__main__":
    main()