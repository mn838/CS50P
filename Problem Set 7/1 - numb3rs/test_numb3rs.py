import pytest
from numb3rs import validate

def test_true( ) -> None:
    assert validate( '127.0.0.1' ) == True

def test_false( ) -> None:
    assert validate( '127.0.0.1000' ) == False

def test_range( ) -> None:
    assert validate( '20.260.15.35' ) == False
