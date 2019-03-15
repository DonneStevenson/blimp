'''Tests plimp package'''
import pytest
from blimp import blimp

def test_multi_cv(capsys):
    '''Correct numbers print out'''
    blimp.multi_cv(7,5)
    captured = capsys.readouterr()
    assert captured.out == "Will do a 7 fold validation 5 times\n"
    
    