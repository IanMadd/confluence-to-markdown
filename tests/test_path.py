import pytest
from convert.path import *

file_path1 = "output/courier/something/something.md"

def test_verify_dir():
    """Test that nonexistent path doesn't exist"""
    assert verify_dir(file_path1) is False

