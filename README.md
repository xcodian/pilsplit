# pilsplit
Split images into equal rows and columns. Useful for splitting spritesheets into individual sprites

### Introduction

---

* Have you ever wanted to split a spritesheet into individual sprites?

* Have you ever wanted to create awesome photo collages?

* Tired of incorect splitting and offset errors?

#### Your answer: PilSplit!

<img src="https://i.ibb.co/Bwg5GDL/pilsplit-demo1.png"></img>

Using PilSplit is simple! Just specify your spritesheet + output folder, how many rows and columns you
want to split into, and get started! The example above shows the program being used to split a spritesheet of
UNO cards into individual PNG images. All images were saved in `/home/user/UnoCards` as specified.

<img src="https://i.ibb.co/ZGhw1Dt/pilsplit-demo2.png"></img>

This is the help for the `pilsplit` command. Here is an explanation of what everything does.

- `image` - Your source image, in this case, this would be the spritesheet.

- `output_dir` - The path to the directory where all the split images should be put into. You can create new directories straight from the command.

- `rows` - How many rows do you want to split the image into?

- `cols` - How many columns do you want to split the image into?

- `-e <ext>`|`--ext <ext>`  - File extension for the output images, without `.`

- `-ns`|`--nosplash` - Disable the splash screen (`PilSplit v1.0.0 by Codian`)

- `-nc`|`--nocolor` - Disable colored output, if it's causing issues for you.

- `-v`|`--verbose` - Show more information about things. Enable if you want to see file write errors when you're splitting.

- `-y`|`--yes` - Yes to all prompts, no input required.

- `-s`|`--silent` - Silence all command output, do the job quietly.

##### Example
Split `input.png` into `2` rows and `3` columns that should be located in `out_dir` and have a
file extension of `.jpg`, don't ask for confirmation, don't show colours, don't show the splash
screen and be verbose.
```
$ pilsplit input.png out_dir/ 2 3 -e jpg -y -nc -ns -v
```
---
### Installation
PilSplit should work in basically any OS that can run python, though it was initially
intended to be used on Linux. **If you are not on linux, you can still use the program,
though you will reach some limitations.**

To get started, clone the repository and enter it:
```
$ git clone https://github.com/xxcodianxx/pilsplit
$ cd pilsplit
```

If you are on linux, you can run the included configuration script to automatically
install or remove PilSplit from your system. 

**You need to run the script as root.**
```
$ chmod +x ./configure.py
# ./configure.py
```
or, alternatively:
```
# python3 ./configure.py --install
```

*Tip: to remove PilSplit from `/usr/bin`, you can replace `--install` with `--remove`*.

---
### Depencencies
As the name suggests, PilSplit depends on `pillow` which should be taken care of by the
configuration script, but you can install it manually using `pip`.

```
# pip install pillow
```
---
### License
PilSplit is licensed under the MIT License.
```
MIT License

Copyright (c) 2020 Martin Velikov

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
```
