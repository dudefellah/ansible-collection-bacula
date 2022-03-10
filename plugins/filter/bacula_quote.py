from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.utils.display import Display
from ansible.module_utils._text import to_text

import json

import re

import socket

display = Display()

def _is_ip_str(data):
    try:
        socket.inet_aton(data)
    except socket.error:
        return False

    return True

def _is_run_str(data, keyword):
    if (keyword is not None) and (keyword.lower() == 'run'):
        return True

    return False

def _is_file_str(data, keyword):
    if (keyword is not None) and (keyword.lower() == 'file'):
        return True

    return False

def _is_quoted_str(data, keyword, resource_type=None):
    return keyword.lower() not in ['run', 'file', 'mail', 'operator', 'console', 'append', 'maximum_volume_bytes', 'director', 'device']

def bacula_quote(data, keyword):
    """Filter to convert the inputted YAML definitions and output them as
    Bacula config-type strings."""

    if data is None:
        return u''

    if isinstance(data, bool):
        if data:
            return "yes"
        return "no"

    elif (
            isinstance(data, str)
    ):
        if (
                not _is_ip_str(data)
                and (_is_quoted_str(data, keyword))
        ):
            return json.dumps(to_text(data))

    return f"{data}"


class FilterModule(object):
    """Jinja2 filters for translating Ansible (eg. YAML) resources into Bacula
    resources."""

    #def __init__(self):
    #    super().__init__()

    def filters(self):
        return {
            'bacula_quote': bacula_quote
        }
