import logging
import subprocess
from netifaces import interfaces, ifaddresses, AF_INET
import os

log_file = "log.txt"

logging.basicConfig(
    handlers=[logging.StreamHandler()]
)

fp_logger = logging.getLogger("log")
fp_logger.setLevel(logging.DEBUG)


def main(start_ip="10.100.82.1"):
    if os.path.exists(log_file):
        os.remove(log_file)

    fp_logger.addHandler(logging.FileHandler(filename=log_file))

    for i in range(1, 255):
        ip = start_ip.split(".")
        ip[3] = str(i)
        ip = ".".join(ip)
        ping = ['ping', ip, "-c", "1", "-t", "1"]

        print("{0}:".format(i), end="\t")

        response = subprocess.run(
            ping, stdout=subprocess.PIPE).stdout.decode("utf-8")

        if "1 packets received" in response:
            ns_response = subprocess.run(
                ["nslookup", ip], stdout=subprocess.PIPE).stdout.decode("utf-8")
            ns = ""
            try:
                ns = f'{ns_response.strip()}'.split("name = ")[1]
            except:
                pass
            print("{0}\t{1}".format(ip, ns))
            fp_logger.info("${0}\t{1}".format(ip, ns))
        else:
            print("")

    pass


def get_ip():
    address = None
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(
            ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
        if not "No IP addr" in addresses and not "127.0.0.1" in addresses:
            address = addresses[0]

    return address


if __name__ == "__main__":
    start_ip = get_ip()
    fp_logger.info("Local IP: {}".format(start_ip))
    main(start_ip=start_ip)
