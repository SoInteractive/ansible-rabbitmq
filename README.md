<p><img src="https://upload.wikimedia.org/wikipedia/en/9/99/RabbitMQLogo.png" alt="rabbitmq logo" title="rabbitmq" align="right" height="60" /></p>

Ansible Role: RabbitMQ
======================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-rabbitmq.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-rabbitmq) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.rabbitmq-blue.svg)](https://galaxy.ansible.com/SoInteractive/rabbitmq/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-rabbitmq.svg)](https://github.com/SoInteractive/ansible-rabbitmq/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Provision RabbitMQ cluster

# :warning: IMPORTANT NOTICE

THIS PROJECT IS ABANDONED. WE DO NOT ACCEPT ANY NEW ISSUES AND/OR PULL REQUESTS.

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

TODO
----

- tests, tests, tests
