from jsplendor.utils import Element

def test_element():
    assert(Element(0).name == "WHITE")
    assert(Element(1).name == "BLUE")
    assert(Element(2).name == "GREEN")
    assert(Element(3).name == "RED")
    assert(Element(4).name == "BLACK")
    assert(Element(5).name == "GOLD")
