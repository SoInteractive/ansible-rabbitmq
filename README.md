<p><img src="https://upload.wikimedia.org/wikipedia/en/9/99/RabbitMQLogo.png" alt="rabbitmq logo" title="rabbitmq" align="right" height="60" /></p>

Ansible Role: RabbitMQ
======================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/rabbitmq/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Frabbitmq/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18295.svg)](https://galaxy.ansible.com/SoInteractive/rabbitmq/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Provision RabbitMQ cluster

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.rabbitmq
```

Role Variables
--------------

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
