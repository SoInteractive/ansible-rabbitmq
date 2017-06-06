Install and manage RabbitMQ cluster
===================================

All variables are in `defaults/main.yml`

Rabbitmq exporter metrics
========================

If rabbitmq_metrics is true install rabbitmq_exporter using binary release. Handlers for restart/reload events.

Requirements
============
All needed packages will be installed with this role. 

Role Variables
==============
```
rabbitmq_hosts_group: rabbitmq

rabbitmq_metrics: true
rabbitmq_exporter_version: 0.20.0
```
