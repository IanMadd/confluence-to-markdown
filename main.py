import os
import re
import shutil
import json
import pandoc
import convert
from pandoc.types import *
from pathlib import Path


def convert_html_to_md(input_dir, output_dir):
    """Convert HTML files to MD files"""

    # Clean output_dir
    convert.path.clean(output_dir)

    # store HTML files in a list
    list_html_files = []
    converted_filenames = {}

    for (sub_dir, dirs, files) in os.walk(input_dir):
        for file in files:
            if '.html' in file:
                file_path = os.path.join(sub_dir, file)
                list_html_files.append(file_path)

    remove_html_files_list = []

    for index, html_file in enumerate(list_html_files):
        if convert.open_files.skip_file(html_file):
            print('Skip HTML file: ' + html_file)
            remove_html_files_list.append(html_file)

    list_html_files = [file for file in list_html_files if file not in remove_html_files_list]

    for file_path in list_html_files:

        doc_object = convert.convert.read(file_path, 'html')

        doc_object = convert.convert.pandoc_object_processing(doc_object)

        ##########
        ### Create Markdown
        ##########
        ### markdown formats:
        ### markdown_phpextra - garbage
        ### markdown_github - possible
        ### markdown_mmd - possible - headings are bad
        ### markdown_strict - ok - doesn't handle code blocks as well as others
        ### commonmark - better
        ### gfm - better
        ### commonmark_x - nope
        ##########

        markdown_text = pandoc.write(doc_object, format='commonmark', options=["--strip-comments", "--wrap=none"])

        ##########
        ### Generate Markdown File
        ##########

        output_path, input_filename, output_filename = convert.path.modify_filename(file_path, output_dir)
        converted_filenames[input_filename] = output_filename

        if convert.path.verify_dir(output_path) is False:
            convert.path.make_dir(output_path)

        convert.open_files.output_file(output_path, markdown_text)

    # save file conversion names

    with open("convert_filenames.json", "w", encoding="utf-8") as outfile:
        json.dump(converted_filenames, outfile, indent=4)

def move_image_files(input_dir, output_dir):
    """copy images to output directory"""

    # Clean output_dir
    convert.path.clean(output_dir)

    # Create list of image files
    list_image_files = []

    for (sub_dir, dirs, files) in os.walk(input_dir):
        # print('\n\n')
        # print('Root dir: ' + sub_dir)
        for file in files:
            if '.png' in file or '.svg' in file:
                file_path = os.path.join(sub_dir, file)
                list_image_files.append(file_path)

    for image_path in list_image_files:
        head, tail = os.path.split(image_path)
        new_image_path = output_dir + tail
        print(new_image_path)
        shutil.copyfile(image_path, new_image_path)

def munge_md_text(input_dir, output_dir):
    """Modify text of MD files

    This should:
    - add frontmatter
    - format page title
    - fix relative links
    - fix image links
    - clean up div and span tags
    """

    # Clean output_dir
    convert.path.clean(output_dir)

    for file in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file)
        output_file_path = os.path.join(output_dir, file)
        file_text = convert.open_files.open_file(file_path)
        
        print("\n\nProcessing page: " + file)

        ## Munge Markdown Files
        frontmatter_text = convert.munge.create_page_frontmatter(file_text)
        file_text = convert.munge.remove_title(file_text)

        ## Add page frontmatter
        file_text = frontmatter_text + file_text

        ## Remove NBSP characters
        file_text = convert.munge.delete_nbsp_character(file_text)

        ## Fix invalid escape characters
        file_text = convert.munge.fix_invalid_escape_sequence(file_text)

        ## Fix links
        file_text = convert.munge.fix_links(file_text)

        ## Output file
        convert.open_files.output_file(output_file_path, file_text)


ROOT_DIR = "input"
TEMP_DIR = 'temp'
OUTPUT_DIR = "output"
CONTENT_DIR = "/content/courier/"
TEMP_CONTENT_DIR = TEMP_DIR + CONTENT_DIR
OUTPUT_CONTENT_DIR = OUTPUT_DIR + CONTENT_DIR
OUTPUT_IMAGE_DIR = OUTPUT_DIR + '/static/images/courier/'

ignore_files = ['.DS_Store']


# convert_html_to_md(ROOT_DIR, TEMP_CONTENT_DIR)
# move_image_files(ROOT_DIR, OUTPUT_IMAGE_DIR)
munge_md_text(TEMP_CONTENT_DIR, OUTPUT_CONTENT_DIR)
