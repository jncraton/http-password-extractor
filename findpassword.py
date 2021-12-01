import sys
import base64
import dpkt


def extract_credentials(auth_header):
    """ Extracts credentials from an http auth header

    It may be helpful to review the HTTP Authorization header:
    
    https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side

    >>> extract_credentials('Basic aXNhYmVsX2h1dGNoaW5zb246RlNMV0tFbXc=')
    ('isabel_hutchinson', 'FSLWKEmw')
    """

    # Add code to split base64 string and decode into username and password
    # The base64 module should be used to handle the decoding

    return (user, password)


def get_basic_auth_credentials(filename):
    """ Implements a generator to yeild basic auth credentials from capture file

    This generator will open a pcap file, process the included packets, and
    yield any HTTP basic auth credentials that it finds. The credentials will
    be represented as (user, password) tuples.

    >>> next(get_basic_auth_credentials('logins.pcap'))
    ('matthew_cooley', 'revsZxFY')

    >>> list(get_basic_auth_credentials('logins.pcap'))[3]
    ('barbara_miller', 'taLxQHuM')

    >>> list(get_basic_auth_credentials('logins.pcap'))[-1]
    ('isabel_hutchinson', 'FSLWKEmw')
    """
    with open("logins.pcap", "rb") as fp:
        pcap = dpkt.pcap.Reader(fp)
        for _, buf in pcap:
            # Read the Ethernet frame
            eth = dpkt.ethernet.Ethernet(buf)

            # Read the IP portion of the packet as the payload of the Ethernet frame
            ip = eth.<expression for packet data payload>

            # Read the TCP portion of the packet as the payload of the IP packet
            tcp = ip.<expression for packet data payload>

            if isinstance(tcp, dpkt.tcp.TCP):
                try:
                    http = dpkt.http.Request(tcp.data)
                    yield extract_credentials(http.headers["authorization"])
                except dpkt.dpkt.UnpackError:
                    pass


def find_password(user, filename="logins.pcap"):
    """
    Finds a password for a given user in the supplied capture file

    >>> find_password('matthew_cooley')
    'revsZxFY'

    >>> find_password('christine_reeves')
    'PYvkSngJ'
    
    >>> find_password('boba_fett')
    
    """

    # Add code to iterate over get_basic_auth_credentials generator and return a 
    # matching password for the supplied username


if __name__ == "__main__":
    print(find_password(sys.argv[1], sys.argv[2]))
