import pytest
from ACNH_pixel_color import ACNH_pixel_color

def test_make_lookup():
  d = ACNH_pixel_color.make_lookup()
  assert(d)


def test_basic_lookup():
  """Hex code 9C5C30 with ID 609 should produce values 3,11,10"""
  d = ACNH_pixel_color.make_lookup()
  assert(d['609'] == "3 11 10")
