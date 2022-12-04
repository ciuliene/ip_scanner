# IP Scanner

Scan your local network, discover other IP addresses and, if exists, also the DNS for each IP.

## Usage

**Note:** For better management create a virtual environment using this command:

```sh
python -m venv venv
```

And activate it running this:

```sh
source venv/bin/activate
```

### Install dependencies

To install required packages, run this command:

```sh
pip install -r requirements.txt
```

### Run the script

To start the scan, run this command:

```sh
python scan.py
```

## Behavior

At first, the script gets the local IP address. Then it begin the network scan, replacing at each iteration the last number of the IP address, from 1 to 255.

Furthermore, for each IP address, it tries to get the DNS and, if it exists, prints it.

The script will print to the stdout the result of the scan and save it in a local file called log.txt

## Extra

There is another file (scan.sh) that scans the network using shell commands. It's just an alternative script.
