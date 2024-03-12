"""
Brute-force diffing svgs
"""
opacity_1 = '0.3'
opacity_2 = '0.3'
color_1 = '#FF4C51'
color_2 = '#8D78FF'


def kdiff_svg(fname_1, fname_2, fout):
    """
    Eeschema-SVG format from kicad has 11 lines of header and its </svg> tag is on the last line
    so no parsing is needed, just some array indexing. Might be fragile
    """
    with open(fname_1, 'r') as f:
        lines1 = f.readlines()
    with open(fname_2, 'r') as f:
        lines2 = f.readlines()
    result_svg_lines = []
    svg_header_len = 11
    result_svg_lines.extend(lines1[:svg_header_len])

    result_svg_lines.extend([replace1(line) for line in lines1[svg_header_len:-1]])
    result_svg_lines.extend([replace2(line) for line in lines2[svg_header_len:]])
    with open(fout, 'w') as f:
        f.writelines(result_svg_lines)


def replace_with_color(line, color, opacity):
    """Only works if the export is black and white"""
    line = line.replace('#000000', color)
    line = line.replace('stroke-opacity:1', 'stroke-opacity:' + opacity)
    line = line.replace('fill-opacity:1.0', 'fill-opacity:' + opacity)
    return line


def replace1(line):
    return replace_with_color(line, color_1, opacity_1)


def replace2(line):
    return replace_with_color(line, color_2, opacity_2)
