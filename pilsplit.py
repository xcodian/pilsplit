#!/usr/bin/python3
# author: Codian (github -> xxcodianxx)

'''
MIT License

Copyright (c) 2020 Codian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

__VERSION__ = '1.0.0'

class color:
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'
    reset = '\u001b[0m'

try:
    import sys, os
    import argparse
    from PIL import Image
except ImportError:
    print(f'{color.reset}[{color.red}!{color.reset}] {color.red}Could not load PIL module. {color.reset}Please install {color.red}pillow{color.reset} with the command {color.red}pip install pillow{color.reset}.')
    exit(-1)

parser = argparse.ArgumentParser(description='Split an image file into equal segments. Uses the Pillow image library.', prog='pilsplit')
parser.add_argument('image', action='store', help='the input image')
parser.add_argument('output_dir', action='store', help='directory to output the split images into')
parser.add_argument('rows', action='store', help='amount of rows')
parser.add_argument('cols', action='store', help='amount of columns')
parser.add_argument('-e', '--ext', action='store', metavar='E', help='file extension of the file without `.` - leave blank for original')
parser.add_argument('-ns', '--nosplash', action='store_true', help='disable the splash screen')
parser.add_argument('-nc', '--nocolor', action='store_true', help='disable colored output')
parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose command output')
parser.add_argument('-y', '--yes', action='store_true', help='yes to all prompts')
parser.add_argument('-s', '--silent', action='store_true', help='silence all command output, even errors')

args = parser.parse_args()
verbose = args.verbose

if args.silent:
    def print(x):
        pass

if verbose:
    if args.nocolor:
        print('+no colored output')
    if args.nosplash:
        print('+skip splash screen')
    if args.yes:
        print('+skip confirmation')


if args.nocolor:
    class color:
        black = ''
        red = ''
        green = ''
        yellow = ''
        blue = ''
        magenta = ''
        cyan = ''
        white = ''
        reset = ''

SPLASH = f'''{color.blue}PilSplit {color.green}v{__VERSION__} {color.reset}by {color.magenta}Codian{color.reset}'''

if not args.nosplash:
    print(SPLASH)

inp_file = args.image
out_dir = args.output_dir

if not os.path.isfile(inp_file):
    print(f'{color.reset}[{color.red}!{color.reset}] {color.reset}Input file {color.red}{inp_file}{color.reset} does not exist.')
    exit(-1)
elif not os.access(inp_file, os.R_OK):
    print(f'{color.reset}[{color.red}!{color.reset}] {color.reset}No read access to input file: {color.red}{inp_file}{color.reset}')
    exit(-1)
else:
    try:
        inp_im = Image.open(inp_file)
    except Exception as e:
        e = str(e)
        print(f'{color.reset}[{color.red}!{color.reset}] {color.reset}Input image: {color.red}{inp_file}{color.reset} -> {color.yellow}{e}{color.reset}')
        exit(-1)
    else:
        Image.Image.format_description
        print(f'{color.reset}[{color.blue}+{color.reset}] {color.reset}Loaded input image: {color.blue}{inp_file}{color.reset} -> {color.green}{inp_im.format} / {inp_im.size[0]}x{inp_im.size[1]} {color.reset}')

if not os.path.isdir(out_dir):
    print(f'{color.reset}[{color.red}!{color.reset}] {color.reset}Output directory {color.red}{out_dir}{color.reset} does not exist.')

    if not args.yes:
        while True:
            x = input(f'-> {color.yellow}Create directory?{color.reset} (y/n): {color.blue}').strip().lower()
            sys.stdout.write(color.reset)
            if x == 'y':
                break
            elif x == 'n':
                print(f'-> {color.red}Aborting!{color.reset} (the output directory must exist)')
                exit(-1)
            else:
                print(f'-> Answer with {color.green}y{color.reset} for Yes or {color.red}n{color.reset} for no')
    else:
        print('[confirmation skipped]')
    try:
        os.mkdir(out_dir)
    except Exception as e:
        print(
            f'{color.reset}[{color.red}!{color.reset}] {color.reset}Error creating {color.red}{out_dir}{color.reset} -> {color.yellow}{e}{color.reset}')
        exit(-1)
    else:
        print(f'{color.reset}[{color.blue}+{color.reset}] {color.reset}Successfully created output directory.')

elif not os.access(out_dir, os.W_OK):
    print(f'{color.reset}[{color.red}!{color.reset}] {color.reset}No write access to output directory: {color.red}{out_dir}{color.reset}')
    exit(-1)
out_dir = os.path.abspath(out_dir)
print(f'{color.reset}[{color.blue}+{color.reset}] {color.reset}Output directory: {color.blue}{out_dir}{color.reset} -> {color.green}{len(os.listdir(out_dir)):,} items{color.reset}')

try:
    r = int(args.rows)
except:
    print(f"{color.reset}[{color.red}!{color.reset}] A {color.red}number{color.reset} is required for row count")
    exit(-1)

try:
    c = int(args.cols)
except:
    print(f"{color.reset}[{color.red}!{color.reset}] A {color.red}number{color.reset} is required for column count")
    exit(-1)

if r < 1:
    print(f"{color.reset}[{color.red}!{color.reset}] You can't split to less than {color.red}1{color.reset} row")
    exit(-1)
if c < 1:
    print(f"{color.reset}[{color.red}!{color.reset}] You can't split to less than {color.red}1{color.reset} column")
    exit(-1)

w, h = inp_im.size

cw = w / c
ch = h / r

print(f'{color.reset}[{color.blue}+{color.reset}] {color.blue}{r}{color.reset} rows, {color.blue}{c}{color.reset} columns -> {color.green}{cw}px{color.reset} x {color.green}{ch}px{color.reset} each')

orig = inp_file.split('.')[-1]
if args.ext == None:
    if orig == inp_file:
        ext = 'png'
    else:
        ext = orig
else:
    ext = args.ext
print(f'{color.reset}[{color.blue}+{color.reset}] File extension for split images: {color.blue}example.{ext}{color.reset}\n')

if not args.yes:
    while True:
        x = input(f'-> {color.yellow}Proceed?{color.reset} (y/n): {color.blue}').strip().lower()
        sys.stdout.write(color.reset)
        if x == 'y':
            break
        elif x == 'n':
            print(f'-> {color.red}Aborting!{color.reset} (user cancelled operation)')
            exit(-1)
        else:
            print(f'-> Answer with {color.green}y{color.reset} for Yes or {color.red}n{color.reset} for no')
else:
    print('[confirmation skipped]')

print(f'\nWriting files...')
ok = 0
for x in range(0, c):
    for y in range(0, r):
        short = f'{y}_{x}.{ext}'
        fname = os.path.join(out_dir, short)

        ov_x = x*cw
        ov_y = y*ch
        cell = inp_im.crop([ov_x, ov_y, ov_x+cw, ov_y+ch])
        try:
            cell.save(fname)
        except Exception as e:
            if verbose:
                print(f'{color.reset}[{color.red}!{color.reset}] {color.reset}Error writing {color.red}{short}{color.reset}: {e}')
        else:
            if verbose:
                print(f'{color.reset}[{color.blue}+{color.reset}] {color.reset}Written {color.blue}{fname}{color.reset}')
            ok += 1

print(f'Written {color.green}{ok:,}{color.reset}/{color.green}{r*c:,}{color.reset} files to {color.green}{out_dir}{color.reset}')

if ok != r*c and not verbose:
    print(f'{color.reset}[{color.yellow}?{color.reset}] Errors? Append {color.yellow}-v{color.reset} to the command to enable {color.yellow}verbose output{color.reset}.')

print('Thank you and goodbye.')
