# uwsgi

[![Build Status](https://travis-ci.org/infOpen/ansible-role-uwsgi.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-uwsgi)

Install uwsgi package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# Installation vars
uwsgi_install_mode: 'package'
uwsgi_packages: "{{ _uwsgi_packages }}"
uwsgi_service_name: 'uwsgi'

# Configuration vars
uwsgi_configuration_available_path: "{{ _uwsgi_configuration_available_path }}"
uwsgi_configuration_enabled_path: "{{ _uwsgi_configuration_enabled_path }}"
uwsgi_configuration_log_path: "{{ _uwsgi_configuration_log_path }}"
uwsgi_configuration_run_path: "{{ _uwsgi_configuration_run_path }}"
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

### Debian family variables

``` yaml
# Package management
_uwsgi_packages:
  - name: 'uwsgi'
  - name: 'uwsgi-plugin-python'
  - name: 'uwsgi-plugin-python3'

# Configuration management
_uwsgi_configuration_available_path: '/etc/uwsgi/apps-available'
_uwsgi_configuration_enabled_path: '/etc/uwsgi/apps-enabled'
_uwsgi_configuration_log_path: '/var/log/uwsgi'
_uwsgi_configuration_run_path: '/var/run/uwsgi'
_uwsgi_apps_defaults:
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

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.uwsgi }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
