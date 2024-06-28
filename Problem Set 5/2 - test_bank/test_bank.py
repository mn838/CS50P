from bank import value
import pytest

def test_1( ) -> None:
    assert value( 'Hello' ) == 0

def test_2( ) -> None:
    assert value( 'Hello, Newman' ) == 0

def test_3( ) -> None:
    assert value( 'How you doing?' ) == 20

def test_4( ) -> None:
    assert value( 'What\'s happening?' ) == 100