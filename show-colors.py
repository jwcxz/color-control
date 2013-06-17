#!/usr/bin/env python

COLOR_CODES = ['black', 'red', 'green', 'brown', 'blue', 'magenta', 'cyan', 'white', None, 'default'];
COLORS = [ c for c in COLOR_CODES if c != None ];

ESC_O = "\033[";
ESC_S = ";";
ESC_C = "m";

CLEAR = "%s%d%s" %( ESC_O, 0, ESC_C );

FG = "3";
BG = "4";
NORMAL = "22";
BOLD = "1";

def cnum(c):
    if c in COLORS:
        return str(COLOR_CODES.index(c));
    else:
        return "";

def cname(c):
    if c != 8 and c < len(COLOR_CODES):
        return COLOR_CODES[c];
    else:
        return -1;

def mkcolor(fg, bg, attr=""):
    if attr != "": attr = attr + ESC_S;

    x = [ ESC_O, attr, 
            FG, cnum(fg), ESC_S, 
            BG, cnum(bg), ESC_C ];

    return "".join(x);



# display a grid of all possible combinations, with both bold and regular
if __name__ == "__main__":
    outstr = CLEAR;
    for fg in COLORS:
        for bg in COLORS:
            t = [ mkcolor(fg, bg, NORMAL), " .:#",
                    mkcolor(fg, bg, BOLD), "#:. ",
                    CLEAR, "  " ];

            outstr += "".join(t);

        outstr += "%s\n" % CLEAR
        
    print outstr
