"""
Role tests
"""
import pytest

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)

def test_packages(Package):
    assert Package('uwsgi').is_installed
    assert Package('uwsgi-plugin-python').is_installed
    assert Package('uwsgi-plugin-python3').is_installed
