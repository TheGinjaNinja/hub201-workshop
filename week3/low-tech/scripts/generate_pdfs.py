"""
Hub201 Week 3 - PDF Generator
Produces:
  interview-script-skeleton.pdf  (A4 portrait)
  question-rewrite-cheatsheet.pdf  (A4 landscape)
Run: python3 week3/low-tech/scripts/generate_pdfs.py
"""

import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, black, white, lightgrey
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

SCRIPTS_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.abspath(os.path.join(SCRIPTS_DIR, ".."))

ORANGE = HexColor("#EA580D")
DARK = HexColor("#0F172A")
MID_GREY = HexColor("#64748B")
LIGHT_BG = HexColor("#FFF7ED")
BORDER = HexColor("#E4E4E7")
LIGHT_FILL = HexColor("#F4F4F5")

A4_W, A4_H = A4          # 595.28 x 841.89 pts
LAND_W, LAND_H = landscape(A4)  # 841.89 x 595.28 pts

MARGIN = 18 * mm
INNER_W = A4_W - 2 * MARGIN


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def draw_rule(c, x, y, width, color=ORANGE, thickness=1.5):
    c.setStrokeColor(color)
    c.setLineWidth(thickness)
    c.line(x, y, x + width, y)


def draw_rect_filled(c, x, y, w, h, fill_color, stroke_color=None,
                     stroke_w=0.5):
    c.setFillColor(fill_color)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(stroke_w)
        c.rect(x, y, w, h, fill=1, stroke=1)
    else:
        c.rect(x, y, w, h, fill=1, stroke=0)


def draw_line(c, x1, y1, x2, y2, color=BORDER, width=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1, y1, x2, y2)


def text_at(c, x, y, text, font="Helvetica", size=10, color=DARK,
            align="left"):
    c.setFont(font, size)
    c.setFillColor(color)
    if align == "center":
        c.drawCentredString(x, y, text)
    elif align == "right":
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)


def label_field(c, x, y, label, field_width, font_size=9):
    """Draw a label then a dotted underline of field_width."""
    c.setFont("Helvetica-Bold", font_size)
    c.setFillColor(MID_GREY)
    c.drawString(x, y, label)
    label_w = c.stringWidth(label, "Helvetica-Bold", font_size)
    line_x = x + label_w + 2 * mm
    draw_rule(c, line_x, y - 1, field_width - label_w - 2 * mm,
              color=BORDER, thickness=0.75)


def section_header(c, x, y, width, text, font_size=10):
    """Orange filled bar with white text."""
    bar_h = 6.5 * mm
    draw_rect_filled(c, x, y - bar_h + 1.5 * mm, width, bar_h,
                     fill_color=ORANGE)
    c.setFont("Helvetica-Bold", font_size)
    c.setFillColor(white)
    c.drawString(x + 3 * mm, y - bar_h + 3.5 * mm, text.upper())
    return y - bar_h + 1.5 * mm  # return bottom of bar


def write_blank_slot(c, x, y, width, slot_height=9 * mm,
                     show_signal_tick=True):
    """One question slot: empty box with optional signal tag row."""
    draw_rect_filled(c, x, y - slot_height, width, slot_height,
                     fill_color=white, stroke_color=BORDER, stroke_w=0.5)
    if show_signal_tick:
        # Signal target prompt at bottom of slot
        tick_y = y - slot_height + 1.8 * mm
        c.setFont("Helvetica", 7)
        c.setFillColor(MID_GREY)
        c.drawString(x + 2 * mm, tick_y,
                     "Signal:  [ ] Recency/freq  [ ] Concrete behaviour  "
                     "[ ] Time/money  [ ] Problem match  [ ] Awareness")
    return y - slot_height


# ---------------------------------------------------------------------------
# PDF 1: Interview Script Skeleton
# ---------------------------------------------------------------------------

def build_interview_script():
    path = os.path.join(OUTPUT_DIR, "interview-script-skeleton.pdf")
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("Hub201 Week 3 - Interview Script Skeleton")

    # --- Page 1 ---
    y = A4_H - MARGIN

    # Header block
    draw_rect_filled(c, MARGIN, y - 8 * mm, INNER_W, 8 * mm,
                     fill_color=ORANGE)
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(white)
    c.drawString(MARGIN + 3 * mm, y - 6 * mm,
                 "HUB201 WEEK 3  |  INTERVIEW SCRIPT SKELETON")
    y -= 8 * mm

    y -= 4 * mm

    # Meta fields grid (2 per row)
    meta_fields = [
        ("Date:", 45 * mm),
        ("Interviewer name:", 45 * mm),
        ("Interviewee name:", 45 * mm),
        ("Role:", 45 * mm),
        ("Company:", 45 * mm),
        ("Hypothesis being tested:", 45 * mm),
    ]
    col_w = INNER_W / 2
    for i, (lbl, fw) in enumerate(meta_fields):
        col = i % 2
        row = i // 2
        fx = MARGIN + col * col_w
        fy = y - row * 9 * mm - 4 * mm
        label_field(c, fx, fy, lbl, col_w - 4 * mm, font_size=9)

    y -= (len(meta_fields) // 2) * 9 * mm + 8 * mm

    draw_rule(c, MARGIN, y, INNER_W, color=BORDER, thickness=0.5)
    y -= 3 * mm

    # --- INTRO ---
    bottom = section_header(c, MARGIN, y, INNER_W,
                            "Intro (warm up - context and permission)")
    y = bottom - 2 * mm

    intro_note = ("Start: thank them, state your name and purpose, confirm "
                  "recording consent. No pitching.")
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColor(MID_GREY)
    c.drawString(MARGIN + 2 * mm, y - 2 * mm, intro_note)
    y -= 7 * mm

    for _ in range(3):
        y = write_blank_slot(c, MARGIN, y, INNER_W, slot_height=11 * mm,
                             show_signal_tick=True)
        y -= 2 * mm

    y -= 2 * mm

    # --- INDUSTRY ---
    bottom = section_header(c, MARGIN, y, INNER_W,
                            "Industry (context and landscape)")
    y = bottom - 2 * mm
    for _ in range(3):
        y = write_blank_slot(c, MARGIN, y, INNER_W, slot_height=11 * mm,
                             show_signal_tick=True)
        y -= 2 * mm

    y -= 2 * mm

    # --- BUSINESS ---
    bottom = section_header(c, MARGIN, y, INNER_W,
                            "Business (their role and priorities)")
    y = bottom - 2 * mm
    for _ in range(4):
        y = write_blank_slot(c, MARGIN, y, INNER_W, slot_height=11 * mm,
                             show_signal_tick=True)
        y -= 2 * mm

    # Check if we need a second page
    if y < 60 * mm:
        c.showPage()
        y = A4_H - MARGIN

    y -= 2 * mm

    # --- PERSONAL ---
    bottom = section_header(c, MARGIN, y, INNER_W,
                            "Personal (decisions and past behaviour)")
    y = bottom - 2 * mm
    for _ in range(4):
        y = write_blank_slot(c, MARGIN, y, INNER_W, slot_height=11 * mm,
                             show_signal_tick=True)
        y -= 2 * mm

    y -= 2 * mm

    # --- OUTRO ---
    bottom = section_header(c, MARGIN, y, INNER_W,
                            "Outro (close and referral)")
    y = bottom - 2 * mm

    # Magic wand question pre-printed
    draw_rect_filled(c, MARGIN, y - 11 * mm, INNER_W, 11 * mm,
                     fill_color=LIGHT_BG, stroke_color=ORANGE, stroke_w=0.75)
    c.setFont("Helvetica-Bold", 8.5)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN + 2 * mm, y - 4 * mm, "Magic wand question (pre-set):")
    c.setFont("Helvetica-Oblique", 8.5)
    c.setFillColor(DARK)
    c.drawString(MARGIN + 2 * mm, y - 8.5 * mm,
                 "If you could wave a magic wand and fix one thing about how "
                 "you handle this today, what would it be?")
    y -= 13 * mm

    y = write_blank_slot(c, MARGIN, y, INNER_W, slot_height=11 * mm,
                         show_signal_tick=False)
    y -= 2 * mm

    # --- FOOTER ---
    if y < 35 * mm:
        c.showPage()
        y = A4_H - MARGIN

    y -= 4 * mm
    draw_rule(c, MARGIN, y, INNER_W, color=ORANGE, thickness=1.0)
    y -= 3 * mm

    footer_lbl = "AFTER THE INTERVIEW"
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, y - 2 * mm, footer_lbl)
    y -= 7 * mm

    after_fields = [
        "Main impressions:",
        "Strongest piece of evidence:",
        "Biggest surprise:",
        "Next action:",
    ]
    fw = (INNER_W - 2 * mm) / 2
    for i, lbl in enumerate(after_fields):
        col = i % 2
        row = i // 2
        fx = MARGIN + col * (fw + 2 * mm)
        fy = y - row * 11 * mm
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(MID_GREY)
        c.drawString(fx, fy, lbl)
        draw_rule(c, fx, fy - 5 * mm, fw - 2 * mm, color=BORDER,
                  thickness=0.5)
        draw_rule(c, fx, fy - 9.5 * mm, fw - 2 * mm, color=BORDER,
                  thickness=0.5)

    # Page footer
    c.setFont("Helvetica", 7)
    c.setFillColor(MID_GREY)
    c.drawCentredString(A4_W / 2, 8 * mm,
                        "Hub201 Week 3 - Interview Script Skeleton  |  "
                        "gingerninjaventures.com")

    c.save()
    print(f"Saved: {path}  ({os.path.getsize(path):,} bytes)")


# ---------------------------------------------------------------------------
# PDF 2: Question Rewrite Cheatsheet
# ---------------------------------------------------------------------------

def build_cheatsheet():
    path = os.path.join(OUTPUT_DIR, "question-rewrite-cheatsheet.pdf")
    c = canvas.Canvas(path, pagesize=landscape(A4))
    c.setTitle("Hub201 Week 3 - Question Rewrite Cheatsheet")

    margin = 15 * mm
    inner_w = LAND_W - 2 * margin
    y = LAND_H - margin

    # Header bar
    draw_rect_filled(c, margin, y - 14 * mm, inner_w, 14 * mm,
                     fill_color=ORANGE)
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(white)
    c.drawString(margin + 4 * mm, y - 7 * mm, "The Open Question Rule")
    c.setFont("Helvetica", 10)
    c.drawString(margin + 4 * mm, y - 12 * mm,
                 "Use why, what, how.  Never: do, would, could, should.")
    y -= 14 * mm + 4 * mm

    # Column headers
    col_w = (inner_w - 8 * mm) / 2
    col_left_x = margin
    col_right_x = margin + col_w + 8 * mm

    def col_header(cx, text, bg_color):
        draw_rect_filled(c, cx, y - 7 * mm, col_w, 7 * mm,
                         fill_color=bg_color)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(white)
        c.drawString(cx + 3 * mm, y - 5 * mm, text)

    col_header(col_left_x, "Closed or leading  (avoid)",
               HexColor("#DC2626"))
    col_header(col_right_x, "Open behavioural  (use)",
               HexColor("#16A34A"))
    y -= 7 * mm + 2 * mm

    # Centre divider
    draw_line(c, LAND_W / 2, margin + 28 * mm, LAND_W / 2, y + 2 * mm,
              color=BORDER, width=0.75)

    pairs = [
        (
            "Would you use this?",
            "When did you last solve this, and how?"
        ),
        (
            "Do you think this is a problem?",
            "Walk me through the last time this came up for you."
        ),
        (
            "Could you see yourself paying?",
            "What did you spend on similar tools in the last 12 months?"
        ),
        (
            "Should we include feature X?",
            "Show me how you handle this today."
        ),
        (
            "Is this interesting?",
            "What are you spending most of your time on this quarter?"
        ),
        (
            "Is budget tight?",
            "Who signed off your last software purchase? Walk me through that."
        ),
        (
            "Does this matter to you?",
            "When did you last try to solve this? What happened?"
        ),
    ]

    row_h = 8.5 * mm
    for i, (bad, good) in enumerate(pairs):
        row_y = y - i * row_h
        fill = LIGHT_FILL if i % 2 == 0 else white

        # Left cell
        draw_rect_filled(c, col_left_x, row_y - row_h + 0.5 * mm,
                         col_w, row_h - 0.5 * mm,
                         fill_color=fill, stroke_color=BORDER, stroke_w=0.3)
        c.setFont("Helvetica", 9)
        c.setFillColor(DARK)
        c.drawString(col_left_x + 2.5 * mm, row_y - row_h + 3 * mm, bad)

        # Right cell
        draw_rect_filled(c, col_right_x, row_y - row_h + 0.5 * mm,
                         col_w, row_h - 0.5 * mm,
                         fill_color=fill, stroke_color=BORDER, stroke_w=0.3)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(DARK)
        c.drawString(col_right_x + 2.5 * mm, row_y - row_h + 3 * mm, good)

    y -= len(pairs) * row_h + 5 * mm

    # Five Signals footer bar
    signals_h = 26 * mm
    bar_y = margin
    draw_rect_filled(c, margin, bar_y, inner_w, signals_h,
                     fill_color=HexColor("#0F172A"))

    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(ORANGE)
    c.drawString(margin + 4 * mm, bar_y + signals_h - 5.5 * mm,
                 "THE FIVE SIGNALS YOU ARE LISTENING FOR")

    signals = [
        ("Recency and frequency",
         "When did this last happen? How often?"),
        ("Concrete behaviour",
         "What exactly did they do, not plan to do?"),
        ("Time and money spent",
         "How much have they invested in solving it already?"),
        ("Problem-area match",
         "Is the pain in the domain you are targeting?"),
        ("Awareness level",
         "Do they know they have this problem, or call it something else?"),
    ]

    sig_col_w = inner_w / len(signals)
    for i, (sig_title, sig_desc) in enumerate(signals):
        sx = margin + i * sig_col_w
        # Vertical divider
        if i > 0:
            draw_line(c, sx, bar_y + 1 * mm, sx,
                      bar_y + signals_h - 7 * mm,
                      color=HexColor("#374151"), width=0.5)

        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(ORANGE)
        c.drawString(sx + 3 * mm, bar_y + signals_h - 11 * mm, sig_title)

        c.setFont("Helvetica", 7.5)
        c.setFillColor(HexColor("#D1D5DB"))

        # Wrap long description manually
        words = sig_desc.split()
        line = ""
        lines = []
        for w in words:
            test = (line + " " + w).strip()
            if c.stringWidth(test, "Helvetica", 7.5) < sig_col_w - 6 * mm:
                line = test
            else:
                lines.append(line)
                line = w
        if line:
            lines.append(line)

        for j, ln in enumerate(lines[:3]):
            c.drawString(sx + 3 * mm,
                         bar_y + signals_h - 15.5 * mm - j * 4.5 * mm, ln)

    # Page footer
    c.setFont("Helvetica", 7)
    c.setFillColor(MID_GREY)
    c.drawCentredString(
        LAND_W / 2, bar_y - 5 * mm,
        "Hub201 Week 3 - Question Rewrite Cheatsheet  |  "
        "gingerninjaventures.com"
    )

    c.save()
    print(f"Saved: {path}  ({os.path.getsize(path):,} bytes)")


if __name__ == "__main__":
    build_interview_script()
    build_cheatsheet()
