resize
======

Very basic script to quickly resize images

Usage
-----
```
python resize.py [-h] [-p [PERCENT]] files [files ...]
```

Description
-----------
Provide either multiple files or use a wildcard (e.g. \*.jpg). Optionally provide the percentage to scale the image(s). The scaled images will be stored in the same location the input file is in. A suffix of *_WIDTHxHEIGHT.ext* is added to the scaled files.
