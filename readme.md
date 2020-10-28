HTTP Basic Auth Password Finder
===============================

This program is able to find passwords in a Wireshark or tcpdump pcap file.

The included `findpassword.py` will search the pcap file for a username and return its associated password. It's currently missing an implementation, but doctests are provided.

Usage
-----

```bash
python3 findpassword.py "christine_reeves" logins.pcap
```