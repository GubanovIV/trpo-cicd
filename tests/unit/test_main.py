from app.main import greet, xor

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
