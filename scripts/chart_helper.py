"""
chart_helper.py - Automated, theme-aware inline SVG generator for SEM5 Study Notes.
Outputs clean, mathematically computed SVG diagrams using site CSS variables:
  --ink, --ink-muted, --surface, --surface-alt, --border, --green, etc.
Zero raster graphics, zero external libraries.
"""

import math

def render_figure(svg_content, title, caption, fig_id=""):
    id_attr = f' id="{fig_id}"' if fig_id else ''
    return f'''<figure class="diagram-card"{id_attr} role="group" aria-labelledby="{fig_id}-title">
  {svg_content}
  <figcaption id="{fig_id}-title" class="diagram-title">{title}</figcaption>
  <p class="diagram-caption" style="font-size:13px; color:var(--ink-muted); margin-top:0.4rem; text-align:center;">{caption}</p>
</figure>'''

def line_chart(points, width=700, height=320, xlabel="X Axis", ylabel="Y Axis", 
               title="Chart", aria_label="", curve_color="var(--green)", xlim=None, ylim=None):
    """
    Renders an accurate 2D mathematical curve plot with axes, ticks, and labels.
    points: list of (x, y) tuples
    """
    pad_left = 65
    pad_right = 30
    pad_top = 35
    pad_bottom = 50
    plot_w = width - pad_left - pad_right
    plot_h = height - pad_top - pad_bottom

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x = xlim[0] if xlim else min(xs)
    max_x = xlim[1] if xlim else max(xs)
    min_y = ylim[0] if ylim else min(ys)
    max_y = ylim[1] if ylim else max(ys)

    if max_x == min_x: max_x += 1
    if max_y == min_y: max_y += 1

    def to_svg(x, y):
        sx = pad_left + ((x - min_x) / (max_x - min_x)) * plot_w
        sy = pad_top + (1.0 - ((y - min_y) / (max_y - min_y))) * plot_h
        return sx, sy

    # Generate path
    path_d = []
    for i, (x, y) in enumerate(points):
        sx, sy = to_svg(x, y)
        cmd = "M" if i == 0 else "L"
        path_d.append(f"{cmd} {sx:.2f} {sy:.2f}")
    path_str = " ".join(path_d)

    # Grid lines & ticks (5 vertical, 5 horizontal)
    grid_lines = []
    tick_labels = []
    for i in range(5):
        # Y axis ticks
        y_val = min_y + (i / 4.0) * (max_y - min_y)
        _, sy = to_svg(min_x, y_val)
        y_lbl = f"{y_val:.1f}" if (isinstance(y_val, float) and abs(y_val) < 10 and y_val != int(y_val)) else f"{int(round(y_val))}"
        grid_lines.append(f'<line x1="{pad_left}" y1="{sy:.1f}" x2="{width - pad_right}" y2="{sy:.1f}" stroke="var(--border)" stroke-width="1" stroke-dasharray="3,3" />')
        tick_labels.append(f'<text x="{pad_left - 8}" y="{sy + 4:.1f}" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="end">{y_lbl}</text>')

        # X axis ticks
        x_val = min_x + (i / 4.0) * (max_x - min_x)
        sx, _ = to_svg(x_val, min_y)
        x_lbl = f"{x_val:.1f}" if (isinstance(x_val, float) and abs(x_val) < 10 and x_val != int(x_val)) else f"{int(round(x_val))}"
        grid_lines.append(f'<line x1="{sx:.1f}" y1="{pad_top}" x2="{sx:.1f}" y2="{height - pad_bottom}" stroke="var(--border)" stroke-width="1" stroke-dasharray="3,3" />')
        tick_labels.append(f'<text x="{sx:.1f}" y="{height - pad_bottom + 18}" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle">{x_lbl}</text>')

    grid_svg = "\n    ".join(grid_lines)
    ticks_svg = "\n    ".join(tick_labels)

    # Axes
    axes_svg = f'''<line x1="{pad_left}" y1="{pad_top}" x2="{pad_left}" y2="{height - pad_bottom}" stroke="var(--ink)" stroke-width="1.5" />
    <line x1="{pad_left}" y1="{height - pad_bottom}" x2="{width - pad_right}" y2="{height - pad_bottom}" stroke="var(--ink)" stroke-width="1.5" />'''

    # Axis labels
    labels_svg = f'''<text x="{width / 2}" y="{height - 12}" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle">{xlabel}</text>
    <text x="{18}" y="{height / 2}" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="700" text-anchor="middle" transform="rotate(-90 18 {height / 2})">{ylabel}</text>'''

    svg = f'''<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" role="img" aria-label="{aria_label or title}">
  <title>{title}</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />
  <g class="chart-grid">
    {grid_svg}
  </g>
  <g class="chart-axes">
    {axes_svg}
    {ticks_svg}
    {labels_svg}
  </g>
  <path d="{path_str}" fill="none" stroke="{curve_color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
</svg>'''
    return svg

def timing_diagram(events, width=720, height=360, title="Timing Diagram", sender_label="Sender", receiver_label="Receiver"):
    """
    Renders protocol packet exchange timing diagram (e.g. Stop-and-Wait, Go-Back-N).
    events: list of dicts:
      {
        'type': 'packet' | 'ack' | 'loss' | 'timeout',
        't_start': float (0..1),
        't_end': float (0..1),
        'label': str,
        'lost': bool (optional)
      }
    """
    x_sender = 120
    x_receiver = width - 120
    y_top = 50
    y_bottom = height - 40

    timeline_h = y_bottom - y_top

    lines = []
    # Axes / Time lines
    lines.append(f'<line x1="{x_sender}" y1="{y_top}" x2="{x_sender}" y2="{y_bottom}" stroke="var(--ink)" stroke-width="2" />')
    lines.append(f'<line x1="{x_receiver}" y1="{y_top}" x2="{x_receiver}" y2="{y_bottom}" stroke="var(--ink)" stroke-width="2" />')
    lines.append(f'<polygon points="{x_sender-4},{y_bottom} {x_sender+4},{y_bottom} {x_sender},{y_bottom+8}" fill="var(--ink)" />')
    lines.append(f'<polygon points="{x_receiver-4},{y_bottom} {x_receiver+4},{y_bottom} {x_receiver},{y_bottom+8}" fill="var(--ink)" />')

    # Headers
    lines.append(f'<text x="{x_sender}" y="{y_top - 18}" fill="var(--ink)" font-family="var(--font-display)" font-size="14" font-weight="700" text-anchor="middle">{sender_label}</text>')
    lines.append(f'<text x="{x_receiver}" y="{y_top - 18}" fill="var(--ink)" font-family="var(--font-display)" font-size="14" font-weight="700" text-anchor="middle">{receiver_label}</text>')
    lines.append(f'<text x="{30}" y="{height/2}" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="11" text-anchor="middle" transform="rotate(-90 30 {height/2})">Time t ▾</text>')

    for ev in events:
        y1 = y_top + ev['t_start'] * timeline_h
        y2 = y_top + ev['t_end'] * timeline_h
        etype = ev.get('type', 'packet')
        lbl = ev.get('label', '')

        if etype == 'packet':
            # Sender to receiver arrow
            color = "var(--green)"
            lines.append(f'<line x1="{x_sender}" y1="{y1}" x2="{x_receiver}" y2="{y2}" stroke="{color}" stroke-width="2" />')
            # Arrow head
            lines.append(f'<polygon points="{x_receiver-8},{y2-4} {x_receiver},{y2} {x_receiver-8},{y2+4}" fill="{color}" />')
            # Mid label
            mx = (x_sender + x_receiver) / 2
            my = (y1 + y2) / 2 - 8
            lines.append(f'<text x="{mx}" y="{my}" fill="var(--ink)" font-family="var(--font-mono)" font-size="11" font-weight="600" text-anchor="middle">{lbl}</text>')

        elif etype == 'ack':
            # Receiver to sender arrow
            color = "#1E4E79" # Blue tint
            lines.append(f'<line x1="{x_receiver}" y1="{y1}" x2="{x_sender}" y2="{y2}" stroke="{color}" stroke-width="1.8" stroke-dasharray="4,2" />')
            lines.append(f'<polygon points="{x_sender+8},{y2-4} {x_sender},{y2} {x_sender+8},{y2+4}" fill="{color}" />')
            mx = (x_sender + x_receiver) / 2
            my = (y1 + y2) / 2 - 8
            lines.append(f'<text x="{mx}" y="{my}" fill="{color}" font-family="var(--font-mono)" font-size="11" font-weight="600" text-anchor="middle">{lbl}</text>')

        elif etype == 'loss':
            # Packet lost midway
            color = "#B91C1C" # Red
            mx = (x_sender + x_receiver) * 0.65
            my = y1 + (y2 - y1) * 0.65
            lines.append(f'<line x1="{x_sender}" y1="{y1}" x2="{mx}" y2="{my}" stroke="{color}" stroke-width="2" />')
            lines.append(f'<text x="{mx + 8}" y="{my + 4}" fill="{color}" font-family="var(--font-display)" font-size="14" font-weight="bold">✕ [Lost]</text>')
            lines.append(f'<text x="{(x_sender+mx)/2}" y="{(y1+my)/2 - 8}" fill="{color}" font-family="var(--font-mono)" font-size="11" text-anchor="middle">{lbl}</text>')

        elif etype == 'timeout':
            color = "#D97706" # Amber
            lines.append(f'<rect x="{x_sender - 12}" y="{y1}" width="24" height="{y2 - y1}" fill="var(--surface-alt)" stroke="{color}" stroke-width="1.5" rx="3" />')
            lines.append(f'<text x="{x_sender - 18}" y="{(y1+y2)/2 + 4}" fill="{color}" font-family="var(--font-mono)" font-size="10" font-weight="bold" text-anchor="end">{lbl}</text>')

    content = "\n    ".join(lines)
    return f'''<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" role="img" aria-label="{title}">
  <title>{title}</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />
  {content}
</svg>'''

def delay_breakdown_bar(components, width=700, height=220, title="Packet Delay Component Breakdown"):
    """
    Renders stacked delay breakdown: Transmission, Propagation, Queuing, Processing
    components: list of dicts: {'name': str, 'value': float, 'unit': str, 'color': str, 'desc': str}
    """
    total = sum(c['value'] for c in components)
    pad_x = 40
    bar_y = 65
    bar_h = 42
    bar_w = width - 2 * pad_x

    elements = []
    # Title
    elements.append(f'<text x="{width/2}" y="32" fill="var(--ink)" font-family="var(--font-display)" font-size="14" font-weight="700" text-anchor="middle">{title}</text>')

    curr_x = pad_x
    legend_items = []
    for i, c in enumerate(components):
        pct = c['value'] / total
        w = pct * bar_w
        color = c['color']
        elements.append(f'<rect x="{curr_x:.1f}" y="{bar_y}" width="{w:.1f}" height="{bar_h}" fill="{color}" stroke="var(--border)" stroke-width="1" />')
        if w > 45:
            elements.append(f'<text x="{curr_x + w/2:.1f}" y="{bar_y + bar_h/2 + 5}" fill="#FFFFFF" font-family="var(--font-mono)" font-size="11" font-weight="700" text-anchor="middle">{c["value"]}{c["unit"]}</text>')
        
        # Legend item
        leg_y = 135 + (i // 2) * 32
        leg_x = pad_x + (i % 2) * (bar_w / 2 + 10)
        legend_items.append(f'''<g transform="translate({leg_x},{leg_y})">
  <rect width="14" height="14" fill="{color}" rx="3" />
  <text x="22" y="11" fill="var(--ink)" font-family="var(--font-display)" font-size="12" font-weight="600">{c["name"]}: <tspan fill="var(--ink-muted)" font-family="var(--font-mono)" font-weight="normal">{c["value"]} {c["unit"]} ({pct*100:.1f}%) – {c["desc"]}</tspan></text>
</g>''')
        curr_x += w

    content = "\n  ".join(elements + legend_items)
    return f'''<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" role="img" aria-label="{title}">
  <title>{title}</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />
  {content}
</svg>'''

def packet_header_grid(fields, width=720, height=180, title="IPv4 Header Format (20 Bytes Base)"):
    """
    Renders 32-bit width packet header layout with exact bit partitions.
    fields: list of rows, each row has list of (label, bit_width, color, subtext)
    Total bits per row = 32
    """
    pad_x = 35
    row_h = 32
    start_y = 50
    total_w = width - 2 * pad_x

    lines = []
    # Title & Bit ruler
    lines.append(f'<text x="{width/2}" y="28" fill="var(--ink)" font-family="var(--font-display)" font-size="14" font-weight="700" text-anchor="middle">{title}</text>')
    
    # 0, 4, 8, 16, 19, 31 bit ruler
    ruler_y = 44
    for b in [0, 4, 8, 16, 19, 24, 31]:
        bx = pad_x + (b / 32.0) * total_w
        lines.append(f'<text x="{bx}" y="{ruler_y}" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="10" text-anchor="middle">bit {b}</text>')

    for r_idx, row in enumerate(fields):
        y = start_y + r_idx * (row_h + 4)
        curr_x = pad_x
        for label, bits, color, sub in row:
            w = (bits / 32.0) * total_w
            lines.append(f'<rect x="{curr_x:.1f}" y="{y}" width="{w:.1f}" height="{row_h}" fill="{color}" stroke="var(--border)" stroke-width="1.2" rx="2" />')
            lines.append(f'<text x="{curr_x + w/2:.1f}" y="{y + 15}" fill="var(--ink)" font-family="var(--font-display)" font-size="11" font-weight="700" text-anchor="middle">{label}</text>')
            lines.append(f'<text x="{curr_x + w/2:.1f}" y="{y + 26}" fill="var(--ink-muted)" font-family="var(--font-mono)" font-size="9" text-anchor="middle">{sub or f"{bits} bits"}</text>')
            curr_x += w

    content = "\n  ".join(lines)
    return f'''<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" role="img" aria-label="{title}">
  <title>{title}</title>
  <rect width="100%" height="100%" fill="var(--surface)" rx="12" />
  {content}
</svg>'''
