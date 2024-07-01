from plates import is_valid
import pytest

def test_1( ) -> None:
    assert is_valid( "CS50" ) == True

def test_2( ) -> None:
    assert is_valid( "CS05" ) == False

def test_3( ) -> None:
    assert is_valid( "CS50P" ) == False

def test_4( ) -> None:
    assert is_valid( "PI3.14" ) == False

def test_5( ) -> None:
    assert is_valid( "H" ) == False

def test_6( ) -> None:
    assert is_valid( "OUTATIME" ) == False
