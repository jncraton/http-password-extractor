import sys
import base64
import dpkt

def extract_credentials(auth_header):
    """ Extracts credentials from an http auth header

    >>> extract_credentials('Basic aXNhYmVsX2h1dGNoaW5zb246RlNMV0tFbXc=')
    ('isabel_hutchinson', 'FSLWKEmw')
    """

def get_basic_auth_credentials(filename):
    """ Implements a generator to yeild basic auth credentials from capture file

    >>> next(get_basic_auth_credentials('logins.pcap'))
    ('matthew_cooley', 'revsZxFY')

    >>> list(get_basic_auth_credentials('logins.pcap'))[3]
    ('barbara_miller', 'taLxQHuM')

    >>> list(get_basic_auth_credentials('logins.pcap'))[-1]
    ('isabel_hutchinson', 'FSLWKEmw')
    """

def find_password(user, filename='logins.pcap'):
    """
    Finds a password for a given user in the supplied capture file

    >>> find_password('matthew_cooley')
    'revsZxFY'

    >>> find_password('christine_reeves')
    'PYvkSngJ'
    
    >>> find_password('boba_fett')
    
    """

if __name__ == '__main__':
    print (find_password(sys.argv[1]. sys.argv[2]))
