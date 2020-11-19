HTTP Basic Auth Password Finder
===============================

This program is able to find passwords in a Wireshark or tcpdump pcap file.

The included `findpassword.py` will search the pcap file for a username and return its associated password. It's currently missing an most of the implementation, but doctests are provided.

The `dpkt` module is used to explore the packet capture. This [example](https://dpkt.readthedocs.io/en/latest/print_http_requests.html) might be a reasonable starting point. The [full API documentation](https://dpkt.readthedocs.io/en/latest/api/api_auto.html) is also available.

Usage
-----

```bash
python3 findpassword.py "christine_reeves" logins.pcap
```
