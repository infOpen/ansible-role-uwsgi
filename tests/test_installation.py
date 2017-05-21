"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_packages(host):
    """
    Check if packages are installed
    """

    packages = []

    if host.system_info.distribution in ('debian', 'ubuntu'):
        packages = ['uwsgi', 'uwsgi-plugin-python', 'uwsgi-plugin-python3']

    for package in packages:
        assert host.package(package).is_installed


def test_configuration_file(host):
    """
    Check configuration files properties
    """

    if host.system_info.distribution not in ('debian', 'ubuntu'):
        pytest.skip('Not apply to %s' % host.system_info.distribution)

    config_file = host.file('/etc/uwsgi/apps-available/foo.yaml')
    assert config_file.exists
    assert config_file.is_file

    config_link = host.file('/etc/uwsgi/apps-enabled/foo.yaml')
    assert config_link.exists
    assert config_link.is_symlink
    assert config_link.linked_to == '/etc/uwsgi/apps-available/foo.yaml'


def test_run_files(host):
    """
    Check run files properties
    """

    if host.system_info.distribution not in ('debian', 'ubuntu'):
        pytest.skip('Not apply to %s' % host.system_info.distribution)

    pid_file = host.file('/var/run/uwsgi/app/foo/pid')
    assert pid_file.exists
    assert pid_file.is_file
    assert pid_file.user == 'root'
    assert pid_file.group == 'root'

    socket_file = host.file('/var/run/uwsgi/app/foo/socket')
    assert socket_file.exists
    assert socket_file.is_socket
    assert socket_file.user == 'foobar'
    assert socket_file.group == 'www-data'
    assert socket_file.mode == 0o660


def test_processes(host):
    """
    Check processes
    """

    assert len(host.process.filter(user='foobar')) == 3


def test_socket(host):
    """
    Test socket properties
    """

    socket = host.socket("unix:///var/run/uwsgi/app/foo/socket")
    assert socket.is_listening


def test_service(host):
    """
    Test service started and enabled
    """

    service = ''
    if host.system_info.distribution in ('debian', 'ubuntu'):
        service = host.service('uwsgi')

    assert service.is_enabled

    # Systemctl not available with Docker images
    if 'docker' != host.backend.NAME:
        assert service.is_running


def test_app(host):
    """
    Test app is running
    """

    app_test = host.run('curl http://127.0.0.1')
    expected_output = "<body><h1 style='color:blue'>Hello World!</h1></body>"

    assert app_test.rc == 0
    assert expected_output in app_test.stdout
