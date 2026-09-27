# contents of test_main.py file

import os

def test_main():
    assert True

def is_done(path):
    if not os.path.exists(path):
        return False
    with open(path) as _f:
        contents = _f.read()
    if "yes" in contents.lower():
        return True
    elif "no" in contents.lower():
        return False

class TestIsDone:

    # Both of these look in the exact same CWD (Current Working Dir) location (C:\Users\AMarto\PyTest_project)
        # with open("tmp/test_file", "w") as f: ...
        # with open("./tmp/test_file", "w") as f: ...
    # however open("/tmp/test_file", "w") as f: ... looks at the root of the current drive (C:\tmp\test_file):

    def test_yes(self):
        with open("./tmp/test_file", "w") as _f:
            _f.write("yes")
        assert is_done("./tmp/test_file") is True

    def test_no(self):
        with open("./tmp/test_file", "w") as _f:
            _f.write("no")
        assert is_done("./tmp/test_file") is False