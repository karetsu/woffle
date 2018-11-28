#-- Imports ---------------------------------------------------------------------
from woffle.data.parse import *

#-- Tests -----------------------------------------------------------------------
def test_letters():
    assert letters('foobar') == 'foobar'
    assert letters('foo_bar') == 'foobar'

def test_spaces():
    assert spaces('  ') == ' '

def test_singletons():
    assert singletons(' x ') == ''

def test_unlines():
    assert unlines('\n\n\n\n') == ''