Color Control
=============

Here are a few utilities for dealing with terminal colors.  I started writing
them because I was bored on a plane flight.  I wanted a way to easily design
color palettes and since I didn't have access to the internet, I couldn't get
to the [4bit designer], which is also a great tool.


## Extracting colors from an SVG graphic palette.

`extract-colors` reads colors data from an SVG file and produces lines for your
~/.Xdefaults or Linux terminal color configuration escape codes.

It's not very smart... It doesn't use proper XML parsing at all, just some
regular expressions that are fairly robust.  See the provided `example.svg`
file for a base to work from.

To generate lines for your `~/.Xdefaults`, try:

```
$ extract-colors -t xdefaults example.svg
```

This will output the appropriate lines.

If you use TTYs directly and would like to generate escape codes for
configuring the color palette there, try:

```
$ extract-colors -t linuxterm example.svg
```

You can then throw those anywhere you want, e.g. in your
`~/.{bash,zsh,whatever}rc`.  I recommend something like this:

```shell
if [ "$TERM" = "linux" ]; then
    # borrowed from http://code.google.com/p/fbterm/
	# output of extract-colors here
	clear # for background artifacting
fi
```


## Showing the current terminal scheme.

`show-colors` is yet another utility to display your available palette.
It's pretty self explanatory.  Just run it.



[4bit designer]:http://ciembor.github.io/4bit/
