HTTP Basic Auth Password Finder
===============================

This program is able to find passwords in a Wireshark or tcpdump pcap file. Passwords are extracted from HTTP `Authorization` headers.

The included `findpassword.py` will search the pcap file for a username and return its associated password. It's currently missing some of the implementation, but doctests are provided.

The `dpkt` module is used to explore the packet capture. This [example](https://dpkt.readthedocs.io/en/latest/print_http_requests.html) might help you understand how this module works. The [full API documentation](https://dpkt.readthedocs.io/en/latest/api/index.html) is also available.

It may be a good idea to open the included `logins.pcap` file in Wireshark to better understand your task.

Usage
-----

Once complete, you should be able to call the program to return a password for any user present in the pcap file as follows:

```bash
python3 findpassword.py "christine_reeves" logins.pcap
```

```
PYvkSngJ
```
