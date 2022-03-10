# Ansible Collection - dudefellah.bacula

This collection was built to create a common interface for deploying Bacula
setups.

# Roles

* [roles/bacula_daemon](roles/bacula_daemon) - A generic Bacula installer and
  configurator role. This role has defaults specific to the File Daemon (the
  client, essentially) but is meant to be used in a Bacula Daemon agnostic way.
* [roles/bacula_director](roles/bacula_director) - A Bacula Director role. This
  role mainly uses the `bacula_daemon` role to perform its tasks. Unlike the
  other `bacula_storage_daemon` and `bacula_file_daemon` roles, this roles does
  do a little bit of extra work related to running initializations for the
  catalog database, if it's needed.
* [roles/bacula_storage_daemon](roles/bacula_storage_daemon) - A Bacula Storage
  Daemon role. This just calls the `bacula_daemon` role with appropriate
  defaults and is meant as a convenience.
* [roles/bacula_file_daemon](roles/bacula_file_daemon) - A File Daemon role.
  This just calls the `bacula_daemon` role with appropriate defaults and is
  meant as a convenience.

# Filters

* [plugins/filter/filter_bacula_quote.py](plugins/filter/filter_bacula_quote.py) - Quotes config values in a Bacula-y way.

# Playbooks

The playbooks under the [playbooks/](playbooks/) directory are primarily
usedful as examples. You may incorporate them into your existing
infrastructure, but they generally only just import the appropriate roles,
so they don't save you too much time.

# Author(s)

Dan - github.com/dudefellah
