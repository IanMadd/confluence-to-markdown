import re


def open_file(full_file_path):
    """Open file and return file text"""
    with open(full_file_path, encoding="utf-8") as file_object:
        file_text = file_object.read()

    return file_text

def output_file(output_path, file_text):
    """Take text string and save to file"""
    with open(output_path, 'w', encoding="utf-8") as file_object:
        file_object.write(file_text)

SKIP_COURIER_INDEX_PAGE_REGEX = r"<head>\n +<title>Courier : Courier</title>"
SKIP_FILE_REGEXES = [SKIP_COURIER_INDEX_PAGE_REGEX]

def skip_file(html_file_path):
    """Remove HTML file from list of converted files if file matches certain characteristics"""
    html_text = open_file(html_file_path)
    for regex in SKIP_FILE_REGEXES:
        return re.search(regex, html_text, re.M)
