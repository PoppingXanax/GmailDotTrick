# GmailDotTrick
Generate Gmail dot-aliases with this Python script. Easily create email variations for improved organization and filtering.


# Gmail Dot Alias Generator

This Python script generates dot aliases for Gmail addresses, allowing you to create multiple email aliases with different dot positions in the local part. It supports both "@gmail.com" and "@googlemail.com" domains and ensures that there are no consecutive dots in the generated aliases. 

Examples at the end of the README

## Features

- Generate dot aliases for Gmail addresses.
- Supports both "@gmail.com" and "@googlemail.com" domains.
- Ensures no consecutive dots in the generated aliases.

## Usage

1. Run the script.
2. Enter a Gmail address (without the "@ domain").
3. The script will generate dot aliases for both "@gmail.com" and "@googlemail.com" domains.
4. Copy and use the generated dot aliases as needed.

**Note:** If the input Gmail address does not have the "@gmail.com" or "@googlemail.com" suffix, the script will automatically add "@gmail.com" as the default domain.

## Example

```
Example: Generate dot-aliases for a Gmail address
Enter a Gmail address (without @ domain): exmaple123
exmaple123@gmail.com (for @gmail.com):
exmaple123@gmail.com
e.xmaple123@gmail.com
ex.maple123@gmail.com
exm.aple123@gmail.com
exma.ple123@gmail.com
exmap.le123@gmail.com
exmapl.e123@gmail.com
exmaple.123@gmail.com
exmaple1.23@gmail.com
exmaple12.3@gmail.com
e.xm.aple123@gmail.com
e.xma.ple123@gmail.com
e.xmap.le123@gmail.com
e.xmapl.e123@gmail.com
e.xmaple.123@gmail.com
e.xmaple1.23@gmail.com
e.xmaple12.3@gmail.com
ex.ma.ple123@gmail.com
ex.map.le123@gmail.com
ex.mapl.e123@gmail.com
ex.maple.123@gmail.com
ex.maple1.23@gmail.com
ex.maple12.3@gmail.com
exm.ap.le123@gmail.com
exm.apl.e123@gmail.com
exm.aple.123@gmail.com
exm.aple1.23@gmail.com
exm.aple12.3@gmail.com
exma.pl.e123@gmail.com
exma.ple.123@gmail.com
exma.ple1.23@gmail.com
exma.ple12.3@gmail.com
exmap.le.123@gmail.com
exmap.le1.23@gmail.com
exmap.le12.3@gmail.com
exmapl.e1.23@gmail.com
exmapl.e12.3@gmail.com
exmaple.12.3@gmail.com
e.xm.ap.le123@gmail.com
e.xm.apl.e123@gmail.com
e.xm.aple.123@gmail.com
e.xm.aple1.23@gmail.com
e.xm.aple12.3@gmail.com
e.xma.pl.e123@gmail.com
e.xma.ple.123@gmail.com
e.xma.ple1.23@gmail.com
e.xma.ple12.3@gmail.com
e.xmap.le.123@gmail.com
e.xmap.le1.23@gmail.com
e.xmap.le12.3@gmail.com
e.xmapl.e1.23@gmail.com
e.xmapl.e12.3@gmail.com
e.xmaple.12.3@gmail.com
ex.ma.pl.e123@gmail.com
ex.ma.ple.123@gmail.com
ex.ma.ple1.23@gmail.com
ex.ma.ple12.3@gmail.com
ex.map.le.123@gmail.com
ex.map.le1.23@gmail.com
ex.map.le12.3@gmail.com
ex.mapl.e1.23@gmail.com
ex.mapl.e12.3@gmail.com
ex.maple.12.3@gmail.com
exm.ap.le.123@gmail.com
exm.ap.le1.23@gmail.com
exm.ap.le12.3@gmail.com
exm.apl.e1.23@gmail.com
exm.apl.e12.3@gmail.com
exm.aple.12.3@gmail.com
exma.pl.e1.23@gmail.com
exma.pl.e12.3@gmail.com
exma.ple.12.3@gmail.com
exmap.le.12.3@gmail.com
e.xm.ap.le.123@gmail.com
e.xm.ap.le1.23@gmail.com
e.xm.ap.le12.3@gmail.com
e.xm.apl.e1.23@gmail.com
e.xm.apl.e12.3@gmail.com
e.xm.aple.12.3@gmail.com
e.xma.pl.e1.23@gmail.com
e.xma.pl.e12.3@gmail.com
e.xma.ple.12.3@gmail.com
e.xmap.le.12.3@gmail.com
ex.ma.pl.e1.23@gmail.com
ex.ma.pl.e12.3@gmail.com
ex.ma.ple.12.3@gmail.com
ex.map.le.12.3@gmail.com
exm.ap.le.12.3@gmail.com
e.xm.ap.le.12.3@gmail.com
-----
exmaple123@googlemail.com (for @googlemail.com):
exmaple123@googlemail.com
e.xmaple123@googlemail.com
ex.maple123@googlemail.com
exm.aple123@googlemail.com
exma.ple123@googlemail.com
exmap.le123@googlemail.com
exmapl.e123@googlemail.com
exmaple.123@googlemail.com
exmaple1.23@googlemail.com
exmaple12.3@googlemail.com
e.xm.aple123@googlemail.com
e.xma.ple123@googlemail.com
e.xmap.le123@googlemail.com
e.xmapl.e123@googlemail.com
e.xmaple.123@googlemail.com
e.xmaple1.23@googlemail.com
e.xmaple12.3@googlemail.com
ex.ma.ple123@googlemail.com
ex.map.le123@googlemail.com
ex.mapl.e123@googlemail.com
ex.maple.123@googlemail.com
ex.maple1.23@googlemail.com
ex.maple12.3@googlemail.com
exm.ap.le123@googlemail.com
exm.apl.e123@googlemail.com
exm.aple.123@googlemail.com
exm.aple1.23@googlemail.com
exm.aple12.3@googlemail.com
exma.pl.e123@googlemail.com
exma.ple.123@googlemail.com
exma.ple1.23@googlemail.com
exma.ple12.3@googlemail.com
exmap.le.123@googlemail.com
exmap.le1.23@googlemail.com
exmap.le12.3@googlemail.com
exmapl.e1.23@googlemail.com
exmapl.e12.3@googlemail.com
exmaple.12.3@googlemail.com
e.xm.ap.le123@googlemail.com
e.xm.apl.e123@googlemail.com
e.xm.aple.123@googlemail.com
e.xm.aple1.23@googlemail.com
e.xm.aple12.3@googlemail.com
e.xma.pl.e123@googlemail.com
e.xma.ple.123@googlemail.com
e.xma.ple1.23@googlemail.com
e.xma.ple12.3@googlemail.com
e.xmap.le.123@googlemail.com
e.xmap.le1.23@googlemail.com
e.xmap.le12.3@googlemail.com
e.xmapl.e1.23@googlemail.com
e.xmapl.e12.3@googlemail.com
e.xmaple.12.3@googlemail.com
ex.ma.pl.e123@googlemail.com
ex.ma.ple.123@googlemail.com
ex.ma.ple1.23@googlemail.com
ex.ma.ple12.3@googlemail.com
ex.map.le.123@googlemail.com
ex.map.le1.23@googlemail.com
ex.map.le12.3@googlemail.com
ex.mapl.e1.23@googlemail.com
ex.mapl.e12.3@googlemail.com
ex.maple.12.3@googlemail.com
exm.ap.le.123@googlemail.com
exm.ap.le1.23@googlemail.com
exm.ap.le12.3@googlemail.com
exm.apl.e1.23@googlemail.com
exm.apl.e12.3@googlemail.com
exm.aple.12.3@googlemail.com
exma.pl.e1.23@googlemail.com
exma.pl.e12.3@googlemail.com
exma.ple.12.3@googlemail.com
exmap.le.12.3@googlemail.com
e.xm.ap.le.123@googlemail.com
e.xm.ap.le1.23@googlemail.com
e.xm.ap.le12.3@googlemail.com
e.xm.apl.e1.23@googlemail.com
e.xm.apl.e12.3@googlemail.com
e.xm.aple.12.3@googlemail.com
e.xma.pl.e1.23@googlemail.com
e.xma.pl.e12.3@googlemail.com
e.xma.ple.12.3@googlemail.com
e.xmap.le.12.3@googlemail.com
ex.ma.pl.e1.23@googlemail.com
ex.ma.pl.e12.3@googlemail.com
ex.ma.ple.12.3@googlemail.com
ex.map.le.12.3@googlemail.com
exm.ap.le.12.3@googlemail.com
e.xm.ap.le.12.3@googlemail.com
```
