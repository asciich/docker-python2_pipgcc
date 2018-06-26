import pytest

@pytest.fixture(scope='module')
def container_image():
    return 'asciich/python2_pipgcc'

class TestAsciichPython2Pipgcc(object):

    def test_git_installed(self, docker_container):
        assert docker_container.exists('git')

    def test_gcc_installed(self, docker_container):
        assert docker_container.exists('gcc')