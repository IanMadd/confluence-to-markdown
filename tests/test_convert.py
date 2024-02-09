import pytest
from convert.munge import *

input_string_1 = '''# <span id="title-text"> Courier : Web Application Firewall (WAF) </span>

A web application firewall is a specific form of application firewall that filters, monitors, and blocks HTTP traffic to and from a web service
'''

output_string_1 = '''A web application firewall is a specific form of application firewall that filters, monitors, and blocks HTTP traffic to and from a web service
'''

def test_convert_remove_title():
    assert remove_title(input_string_1) == output_string_1