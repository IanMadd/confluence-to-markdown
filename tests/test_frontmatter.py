import pytest
from convert.munge import *

title_string_input_1 = '# <span id="title-text"> Courier : Skill Catalog </span>'
title_string_response_1 = 'Courier : Skill Catalog'
toml_menu_string_1 = '''+++
title = "Courier Skill Catalog"

[menu.courier]
title = "Skill Catalog"
identifier = "courier/Courier Skill Catalog"
parent = "courier"
weight = 10
+++

'''

title_string_input_2 = '# <span id="title-text"> Courier : Using / Configuring External Services </span>'
title_string_response_2 = 'Courier : Using / Configuring External Services'

def test_get_title_1():
    """get_title returns the proper page title"""
    assert get_title(title_string_input_1) == title_string_response_1

def test_get_title_2():
    """get_title returns the proper page title"""
    assert get_title(title_string_input_2) == title_string_response_2

def test_create_page_frontmatter():
    assert create_page_frontmatter(title_string_input_1) == toml_menu_string_1