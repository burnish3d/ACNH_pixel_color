import pytest
from ACNH_pixel_color.ACNH_pixel_color import make_lookup

def test_make_lookup():
  d = make_lookup()
  assert d


def test_basic_lookup():
  """Hex code 9C5C30 with ID 609 should produce values 3,11,10"""
  d = make_lookup()
  assert d['609'] == [3,11,10]
