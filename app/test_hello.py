# testing hello.py 
def test_hello_no_args():
    import hello
    assert hello.hello() == "Hello World!"

def test_hello_with_args():
    import hello
    assert hello.hello("fire") == "Hello fire!"
