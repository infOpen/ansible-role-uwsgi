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


def test_configuration_file(File):
    config_file = File('/etc/uwsgi/apps-available/foo.yaml')
    assert config_file.exists
    assert config_file.is_file

    config_link = File('/etc/uwsgi/apps-enabled/foo.yaml')
    assert config_link.exists
    assert config_link.is_symlink
    assert config_link.linked_to == '/etc/uwsgi/apps-available/foo.yaml'


def test_run_files(File):
    pid_file = File('/var/run/uwsgi/app/foo/pid')
    assert pid_file.exists
    assert pid_file.is_file
    assert pid_file.user == 'root'
    assert pid_file.group == 'root'

    socket_file = File('/var/run/uwsgi/app/foo/socket')
    assert socket_file.exists
    assert socket_file.is_socket
    assert socket_file.user == 'foobar'
    assert socket_file.group == 'www-data'
    assert socket_file.mode == 0o660


def test_processes(Process):
    assert len(Process.filter(user='foobar')) == 3


def test_socket(Socket):
    socket = Socket("unix:///var/run/uwsgi/app/foo/socket")
    assert socket.is_listening


def test_service(Service):
    service = Service('uwsgi')
    assert service.is_enabled
    assert service.is_running


def test_app(Command):
    command = Command('curl http://127.0.0.1')
    assert command.rc == 0
    assert command.stdout == "<html><body><h1 style='color:blue'>Hello World!</h1></body></html>"
