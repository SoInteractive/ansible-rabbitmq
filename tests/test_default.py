from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/etc/rabbitmq",
        "/var/lib/rabbitmq",
        "/var/log/rabbitmq"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/rabbitmq/rabbitmq-env.conf",
        "/etc/rabbitmq/rabbitmq.config",
        "/var/lib/rabbitmq/.erlang.cookie",
        "/etc/systemd/system/rabbitmq_exporter.service"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "rabbitmq-server",
        "rabbitmq_exporter"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled


# def test_socket(Socket, Interface):
#     ip = Interface("eth0").addresses[0]
#     print(ip)
#     present = [
#         "tcp://" + ip + ":5672",
#         "tcp://0.0.0.0:15672",
#         "tcp://0.0.0.0:4369"
#     ]
#     for socket in present:
#         s = Socket(socket)
#         assert s.is_listening
