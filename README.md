# uwsgi

[![Build Status](https://travis-ci.org/infOpen/ansible-role-uwsgi.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-uwsgi)

Install uwsgi package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role has some testing methods.

To use locally testing methods, you need to install Docker and/or Vagrant and Python requirements:

* Create and activate a virtualenv
* Install requirements

```
pip install -r requirements_dev.txt
```

### Automatically with Travis

Tests runs automatically on Travis on push, release, pr, ... using docker testing containers

### Locally with Docker

You can use Docker to run tests on ephemeral containers.

```
make test-docker
```

### Locally with Vagrant

You can use Vagrant to run tests on virtual machines.

```
make test-vagrant
```

## Role Variables

### Default role variables

``` yaml
# Installation vars
uwsgi_install_mode: 'package'
uwsgi_package_state: 'latest'
uwsgi_packages:
  - 'uwsgi'
  - 'uwsgi-plugin-python'
  - 'uwsgi-plugin-python3'
uwsgi_service_name: 'uwsgi'

# Configuration vars
uwsgi_configuration_available_path: '/etc/uwsgi/apps-available'
uwsgi_configuration_enabled_path: '/etc/uwsgi/apps-enabled'
uwsgi_configuration_log_path: '/var/log/uwsgi'
uwsgi_configuration_run_path: '/var/run/uwsgi'
uwsgi_configuration_owner: 'root'
uwsgi_configuration_group: 'root'
uwsgi_configuration_mode: '0640'
uwsgi_apps: []
uwsgi_apps_defaults:
  uwsgi:
    autoload: true
    master: true
    workers: 2
    no-orphans: true
    pidfile: "{{ uwsgi_configuration_run_path ~ '/%(deb-confnamespace)/%(deb-confname)/pid' }}"
    socket: "{{ uwsgi_configuration_run_path ~ '/%(deb-confnamespace)/%(deb-confname)/socket' }}"
    logto: "{{ uwsgi_configuration_log_path ~ '/%(deb-confnamespace)/%(debconfname).log' }}"
    chmod-socket: 660
    log-date: true
    uid: www-data
    gid: www-data
```

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: infOpen.uwsgi }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
