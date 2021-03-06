#!/usr/bin/env python

import argparse, re

CPFX = ['black', 'red', 'green', 'brown', 'blue', 'magenta', 'cyan', 'white'];

C_NORMAL = [ "%s_normal" % c for c in CPFX ];
C_BRIGHT = [ "%s_bright" % c for c in CPFX ];
DEFS = ['foreground', 'background' ];

COLORS = C_NORMAL + C_BRIGHT + DEFS;


rect_re = re.compile("(<rect ([^/]*) />)");
color_re = re.compile("fill:#(.{6,6})");
id_re = re.compile("id=\"(\w+)\"");


def get_value(reobj, line):
    r = reobj.search(line);
    if r:
        return r.groups()[0];
    else:
        return None;


def get_color(line):
    return get_value(color_re, line);

def get_id(line):
    return get_value(id_re, line);


def extract_colors(data):
    # join lines
    data = data.replace('\n', '');

    out = {};

    # find rectangle attributes, classify by color
    rects = rect_re.findall(data);
    for _, rect in rects:
        r_id = get_id(rect);
        r_color = get_color(rect);

        if r_id in COLORS:
            out[r_id] = r_color;

    return out


def gen_xdefaults(colors):
    mapping = C_NORMAL + C_BRIGHT;

    lines = [];

    for c in colors:
        if c in mapping:
            l = "*color%d: #%s" % (mapping.index(c), colors[c]);
            lines.append((mapping.index(c) + 2, l));
        elif c in DEFS:
            l = "*%s: #%s" % (c, colors[c]);
            lines.append((DEFS.index(c), l));

    lines.sort();

    out = "";
    for _, l in lines:
        out += "%s\n" % l;

    return out[:-1];

def gen_linuxterm(colors):
    mapping = C_NORMAL + C_BRIGHT;

    lines = [];

    for c in colors:
        if c in mapping:
            l = "echo -en \"\\e]P%X%s\"  # %s" % (mapping.index(c), colors[c], c);
            lines.append((mapping.index(c), l));

    lines.sort();

    out = "";
    for _, l in lines:
        out += "%s\n" % l;

    return out[:-1];




if __name__ == "__main__":
    p = argparse.ArgumentParser(description='Generate color palettes from an SVG file');

    p.add_argument('-t', '--type', dest='type', action='store', type=str,
            default='xdefaults', 
            help='Type of config to generate (xdefaults [default] or linuxterm)');


    p.add_argument('file', action='store', type=str, nargs=1,
            help='Input SVG file');

    args = p.parse_args();

    # TODO: replace with argparse
    f = open(args.file[0]);
    data = f.read();
    f.close();

    colors = extract_colors(data);

    if args.type == 'xdefaults':
        print gen_xdefaults(colors);
    elif args.type == 'linuxterm':
        print gen_linuxterm(colors);

