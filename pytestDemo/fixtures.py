import pytest

@pytest.fixture(params=[12,22,13],ids=["twelve","twenty two", "thirteen"])
def setup(request):
    p=request.param+10
    return p
    def teardown():
        print("This is the end of the world")
    request.add.finalizer(teardown)

def test_001(setup):
    print(setup)