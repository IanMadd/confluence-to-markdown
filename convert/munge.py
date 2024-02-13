import re
import json
import toml
from convert.config import *
from convert.open_files import *

COURIER_COURIER_PAGE_TITLE_REGEX = r"Courier : Courier "
COURIER_PAGE_TITLE_REGEX = r"Courier : "
COURIER_PAGE_TITLE_REGEX_REPLACE = "Courier "
COURIER_MENU_TITLE_REGEX = r"Courier "
HTML_LINK_REGEX = r'<a href="([\w|\-|%|\.|\:|\/|\+|_|;|!|$|?|&|=]+)" [\w| |\-|\"|=|]+>([\w| |\-|%|\.|\:|\/|\+|_|;|!|$|?|&|=]+)<\/a>'
NBSP_CHARACTER_REGEX = r" "
WIKI_PAGE_NUMBER_REGEX = r"/wiki/spaces/Courier/pages/(\d+)"

def remove_title(page_text):
    """Delete page title HTML span from top of page"""
    result = re.sub(TITLE_REGEX, '', page_text, 1, re.M).lstrip()
    return result

def get_title(page_text):
    """Return page title from MD page text"""
    match_object = re.search(TITLE_REGEX, page_text, re.M)
    if match_object is None:
        print(page_text[:200])
        raise TypeError
    # print(match_object.group(1))
    return match_object.group(1).strip()

def fix_page_title(title_text):
    """Take page title and edit text"""
    title_text = re.sub(COURIER_COURIER_PAGE_TITLE_REGEX, COURIER_PAGE_TITLE_REGEX_REPLACE, title_text, 1)
    title_text = re.sub(COURIER_PAGE_TITLE_REGEX, COURIER_PAGE_TITLE_REGEX_REPLACE, title_text, 1)
    return title_text

def fix_menu_title(title_text):
    """Take page title and format menu title"""
    menu_title = re.sub(COURIER_MENU_TITLE_REGEX, "", title_text, 1)
    return menu_title

def create_page_frontmatter(page_text):
    """Generate TOML frontmatter for each page"""
    page_title = get_title(page_text)
    page_title = fix_page_title(page_title)
    menu_title = fix_menu_title(page_title)
    frontmatter_dict = {}
    frontmatter_dict['title'] = page_title
    menu_identifier = 'courier/' + str(page_title)
    menu_properties = {'title': menu_title, 'identifier': menu_identifier, 'parent': 'courier', 'weight': 10}
    menu = {'courier': menu_properties}
    frontmatter_dict['menu'] = menu
    frontmatter = '+++\n'
    frontmatter += toml.dumps(frontmatter_dict)
    frontmatter += '+++\n\n'
    return frontmatter

def fix_image_links(page_text):
    """Take MD page text and fix image links"""
    image_regex = r"<img src=\"attachments/\w+/((\w|\/|)+\.[\w]+)[\w|\?|\=|\"| |\-|\/|\.|\:]+>"
    icon_regex = r"<img src=\"images/icons[\/|\w\.|\"| |\=]+>"
    md_image_regex = r"\[[\w|\-]+\.\w+\]\(attachments/\d+\/(\d+\.\w+)\) \([\w|\/]+\)"

    page_text = re.sub(image_regex, "![](/images/courier/\\g<1>)\n", page_text, 0)
    page_text = re.sub(icon_regex, "", page_text, 0)
    page_text = re.sub(md_image_regex, "![](/images/courier/\\g<1>)", page_text, 0)

    return page_text

def fix_links(page_text):
    """Take MD Page text and fix relative links to other pages"""
    converted_files = json.loads(open_file('convert_filenames.json'))
    while(html_link_match := re.search(HTML_LINK_REGEX, page_text, re.M)):
        start = html_link_match.start(0)
        print(start)
        print(html_link_match)
        end = html_link_match.end(0)
        print(end)
        link_text = html_link_match.group(2)
        # print(html_link_match.groups())
        html_link_url = html_link_match.group(1)
        print(html_link_url)
        if html_link_url in converted_files:
            new_link_url = "/courier/" + converted_files[html_link_url]
        elif '/wiki/spaces/Courier/' in html_link_url:
            page_number_match = re.search(WIKI_PAGE_NUMBER_REGEX, html_link_url)
            print('page number: ')
            print(page_number_match.group(1))
            page_number = page_number_match.group(1)
            md_page = ''
            for key, value in converted_files.items():
                if page_number in key:
                    print('found match')
                    md_page = value
                    print('string: ' + page_number)
                    print('match: ' + key)
                    print(md_page)
            new_link_url = "/courier/" + md_page
        else:
            new_link_url = html_link_url
        new_link_url = re.sub(r'\.html', '/', new_link_url)
        new_link_url = re.sub(r'\.md', '/', new_link_url)
        new_url_text = "[" + link_text + "](" + new_link_url + ")"
        page_text = page_text[0:start] + new_url_text + page_text[end:]

    return page_text

def remove_divs(page_text):
    """Remove divs"""
    print('removing divs\n')
    div_regex = r'( {0,})<div [ |\w|\=|\"|\-|\#|\:|\;]+>[\n| ]{0,}'
    plain_div_regex = r"( {0,})<div>[\n| ]{0,}"
    no_spaces_next_line_regex = r"</div>\n{0,}(?=[-|\w])"
    spaces_next_line_regex = r"( {0,})</div>\n{0,}(?!\n{0,}-)"

    page_text = re.sub(div_regex, "\\g<1>", page_text, count=0)
    page_text = re.sub(plain_div_regex, "\\g<1>", page_text, count=0)
    page_text = re.sub(no_spaces_next_line_regex, "", page_text, count=0)
    page_text = re.sub(spaces_next_line_regex, "\\g<1>", page_text, count=0)

    return page_text

def remove_spans(page_text):
    """Remove HTML spans"""
    page_text = re.sub(r"<span [\w|\-|\"| |\=]+>", "", page_text, 0)
    page_text = re.sub(r"</span>\n{0,1}", "", page_text, 0)

    return page_text

def sentence_case_text(text):
    """Return text in sentence case format"""
    pass

def delete_nbsp_character(page_text):
    """Delete invisible characters returned in the HTML output"""
    page_text = re.sub(NBSP_CHARACTER_REGEX, '', page_text)

    return page_text

def fix_invalid_escape_sequence(page_text):
    """Replace invalid escapes"""
    page_text = re.sub(r"\>", ">", page_text)
    page_text = re.sub(r"\<", "<", page_text)
    page_text = re.sub(r"\[", "[", page_text)
    page_text = re.sub(r"\]", "]", page_text)
    page_text = re.sub(r"\#", "#", page_text)

    return page_text

def process_code_blocks(text):
    """Convert indented code_blocks to backtick code blocks"""
    find_indent_code_regex = r"^ {4}[\w|\s]"
    regular_line_regex = r"^[\n|\r|\w|#]"
    backticks_regex = r"^```\s{0,1}\w{0,}"
    backtick_code_block = False

    text_list = text.splitlines(True)

    editing_code_block = False
    loop_break = 0

    for index,line in enumerate(text_list):
        loop_break += 1
        assert loop_break < 2000, f"text_list number when processing code blocks exceeds: {loop_break}"

        ## If a line has a fenced code_block markers, ie "```", and the script has already matched a fenced code_block,
        ## then set backtick_code_block to False.
        ## That is to say the script has already started processing a fenced code_block on a previous line and has found the end
        ## of the fenced code_block.
        if re.search(backticks_regex, line) and backtick_code_block is True:
            backtick_code_block = False

        ## If it finds backticks code fencing and it hasn't found backtick code fencing on a previous line
        ## set backtick_code_block to True so the code_block isn't processed in the next step.
        if re.search(backticks_regex, line) and backtick_code_block is False:
            backtick_code_block = True


        if (found_indent_block := re.search(find_indent_code_regex, line)) is not None and backtick_code_block is False:
            if editing_code_block is False:
                number_of_indent_spaces = str(len(line) - len(line.lstrip(' ')))
                unindent_code_regex = r"^ {" + number_of_indent_spaces + "}"
                text_list[index] = "```\n" + re.sub(unindent_code_regex, "", line)
                editing_code_block = True
            else:
                text_list[index] = re.sub(unindent_code_regex, "", line)

        elif not found_indent_block and editing_code_block is True:
            if re.search(regular_line_regex, line):
                # print(line)
                text_list[index] = "```\n" + text_list[index]
                editing_code_block = False

    output = "".join(text_list)
    # print(output)
    return output