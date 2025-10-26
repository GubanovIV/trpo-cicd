from app.main import greet

def test_greet_output(capsys):
    greet()
    captured = capsys.readouterr()
    assert captured.out == "Hello world\n"
    assert captured.err == ""
