from app.main import greet, xor
import os

def test_greet_output(capsys):
    greet()
    captured = capsys.readouterr()
    assert captured.out == "Hello world\n"
    assert captured.err == ""

def test_dev_func():
    ans = {(0, 0): 0,
           (0, 1): 1,
           (1, 0): 1,
           (1, 1): 0,}
    for k,v in ans.items():
        assert xor(*k) == v

def test_config():
    file_to_check = "../../app/release_config.yaml"
    assert not os.path.exists(file_to_check), f"File '{file_to_check}' was not found."
