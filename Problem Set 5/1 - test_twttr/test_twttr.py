from twttr import shorten
import pytest

def test_1( ) -> None:
    assert shorten( 'Twitter' ) == 'Twttr'

def test_2( ) -> None:
    assert shorten( 'What\'s your name?' ) == 'Wht\'s yr nm?'

def test_3( ) -> None:
    assert shorten( 'CS50' ) == 'CS50'

def test_4( ) -> None:
    assert shorten( 'WhAt\'s your name?' ) == 'Wht\'s yr nm?'
