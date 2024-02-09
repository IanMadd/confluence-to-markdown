from pathlib import PurePath, Path
import os
import shutil
import re
from convert.open_files import open_file
from convert.config import *
from slugify import slugify

INTEGER_FILENAME_REGEX = r"^\d+\.html$"
HTML_TITLE_REGEX = r"<h1 id=\"title-heading\" class=\"pagetitle\">\s+<span id=\"title-text\">\s+([\w| |:|\/|\(|\)|\,|\-|;|\.]+)"


def modify_filename(input_path, output_dir):
    """Take input HTML path and return output MD path"""
    path = PurePath(input_path)
    print(path)

    input_filename = path.parts[-1]
    output_filename = input_filename

    # if the filename is a string of just numbers (12321412.html), parse the file text to generate a new file name
    if re.match(INTEGER_FILENAME_REGEX, output_filename):
        file_text = open_file(input_path)
        page_title_match = re.search(HTML_TITLE_REGEX, file_text, re.M)
        print(page_title_match)
        print(page_title_match.group(1))
        output_filename = slugify(page_title_match.group(1), max_length=60, word_boundary=True, separator="_") + '.html'

    output_filename = re.sub(r'\.html$', '.md', output_filename)
    output_filename = re.sub(r'%2[C|c]-', '_', output_filename)
    output_filename = re.sub(r'_\d+(?=\.)', '', output_filename)
    output_filename = re.sub(r'-', '_', output_filename)
    output_filename = re.sub(r'_{2,}', '_', output_filename)

    output_filename = output_filename.lower()

    output_path = os.path.join(output_dir, output_filename)

    return output_path, input_filename, output_filename

def verify_dir(input_path):
    """Verify output directories exist"""
    dir_name = os.path.dirname(input_path)
    return os.path.isdir(dir_name)

def make_dir(input_path):
    """Create dir if it doesn't exist"""
    dir_name = os.path.dirname(input_path)
    os.makedirs(dir_name)

def clean(output_dir_path):
    """Delete contents of output dir"""
    if os.path.isdir(output_dir_path):
        shutil.rmtree(output_dir_path)
    os.makedirs(output_dir_path)
