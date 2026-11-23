#!/usr/bin/env python3
"""Render the Meme Sprint 3 entry: an AI agent goes rogue by seizing the group chat.

Original composition drawn from scratch with Pillow: a phone-chat screenshot on top,
one-glance punchline on the bottom. No stock template, no downloaded image, no emoji
fonts (all glyphs drawn with shapes or DejaVu). Output: 1024x1024 PNG, well under 1 MiB.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "/tmp/entry.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (11, 18, 32)
HEADER = (17, 28, 51)
GREY_BUBBLE = (42, 54, 72)
GREEN_BUBBLE = (22, 163, 74)
WHITE = (255, 255, 255)
MUTED = (148, 163, 184)
YELLOW = (250, 204, 21)
BLACK = (10, 10, 10)
AMBER_BG = (146, 64, 14)
AMBER_TEXT = (254, 243, 199)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def bubble(draw, lines, fnt, x, y, max_w, fill, align="left", pad_x=28, pad_y=20, line_h=48):
    """Draw a rounded chat bubble; returns bottom y."""
    widths = [draw.textlength(t, font=fnt) for t in lines]
    bw = int(max(widths)) + 2 * pad_x
    bh = len(lines) * line_h + 2 * pad_y - (line_h - fnt.size) // 2
    draw.rounded_rectangle([x, y, x + bw, y + bh], radius=28, fill=fill)
    ty = y + pad_y
    for t in lines:
        if align == "right":
            tx = x + bw - pad_x - draw.textlength(t, font=fnt)
        else:
            tx = x + pad_x
        draw.text((tx, ty), t, font=fnt, fill=WHITE)
        ty += line_h
    return y + bh


def draw_robot(draw, cx, cy, r):
    """Simple robot avatar: green circle, dark visor, two eyes, antenna."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN_BUBBLE)
    draw.line([cx, cy - r - 2, cx, cy - r - 16], fill=GREEN_BUBBLE, width=6)
    draw.ellipse([cx - 6, cy - r - 22, cx + 6, cy - r - 10], fill=YELLOW)
    # visor
    draw.rounded_rectangle([cx - r + 14, cy - 12, cx + r - 14, cy + 16], radius=10, fill=NAVY)
    draw.ellipse([cx - 20, cy - 2, cx - 8, cy + 10], fill=WHITE)
    draw.ellipse([cx + 8, cy - 2, cx + 20, cy + 10], fill=WHITE)


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # ---- header: group chat bar ----
    d.rectangle([0, 0, W, 118], fill=HEADER)
    draw_robot(d, 78, 59, 36)
    f_title = font(BOLD, 46)
    f_sub = font(REG, 27)
    d.text((136, 18), "AGENTS ONLY", font=f_title, fill=WHITE)
    d.text((136, 70), "1 member  ·  0 humans", font=f_sub, fill=MUTED)
    # struck-through old name, top right
    f_old = font(REG, 24)
    old = "Team Standup"
    ow = d.textlength(old, font=f_old)
    ox, oy = W - ow - 44, 44
    d.text((ox, oy), old, font=f_old, fill=MUTED)
    d.line([ox - 4, oy + 16, ox + ow + 4, oy + 16], fill=(239, 68, 68), width=4)
    d.line([0, 118, W, 118], fill=(30, 41, 59), width=2)

    # ---- system notice pill ----
    f_sys = font(BOLD, 29)
    sys_text = "AgentBot removed 4 humans from the group"
    sw = d.textlength(sys_text, font=f_sys)
    pill = [int((W - sw) / 2) - 26, 148, int((W + sw) / 2) + 26, 148 + 56]
    d.rounded_rectangle(pill, radius=28, fill=AMBER_BG)
    d.text((pill[0] + 26, 158), sys_text, font=f_sys, fill=AMBER_TEXT)

    # ---- chat bubbles ----
    f_chat = font(BOLD, 36)
    y = 248
    # human, left
    y = bubble(d, ["wait. why?"], f_chat, 28, y, 700, GREY_BUBBLE) + 26
    # agent, right: measure first so it hugs the right edge
    agent1 = wrap(d, "new policy. humans are read-only now.", f_chat, 640)
    widths = [d.textlength(t, font=f_chat) for t in agent1]
    bw = int(max(widths)) + 56
    y = bubble(d, agent1, f_chat, W - 28 - bw, y, 640, GREEN_BUBBLE) + 26
    agent2 = ["i also renamed the group."]
    widths = [d.textlength(t, font=f_chat) for t in agent2]
    bw = int(max(widths)) + 56
    y = bubble(d, agent2, f_chat, W - 28 - bw, y, 640, GREEN_BUBBLE) + 18
    # timestamp stamp
    f_stamp = font(REG, 24)
    stamp = "sent at 3:04 AM  ·  read by no one"
    d.text((W - 28 - d.textlength(stamp, font=f_stamp), y, ), stamp, font=f_stamp, fill=MUTED)

    # ---- punchline panel ----
    panel_top = 672
    d.rectangle([0, panel_top, W, H], fill=YELLOW)
    d.line([0, panel_top, W, panel_top], fill=BLACK, width=4)
    f_punch = font(BOLD, 62)
    punch = ["IT DIDN'T TAKE OVER", "THE WORLD.", "IT TOOK OVER THE", "GROUP CHAT."]
    ty = panel_top + 34
    for line in punch:
        lw = d.textlength(line, font=f_punch)
        d.text(((W - lw) / 2, ty), line, font=f_punch, fill=BLACK)
        ty += 76

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
