dudefellah.bacula.bacula_director
=========

This role mostly does what [dudefellah.bacula.bacula_daemon](github.com/dudefellah/ansible-collection-bacula/roles/bacula_daemon)
does, with a few extra bits added in. Mostly these are related to the
configuration and initialization of the catalog database. You can read more
about that below. Otherwise, this role does what it implies: installs the
bacula director, creates and tests configuration files and starts the daemon.

Requirements
------------

Make sure you have the ability to `setfacl` if you intend on using some of
the extra init scripts to prepare the catalog database. Normally, this should
aready live on your system, but some minimal images (eg. a Vagrant box or Docker
image) might be missing the binary. On Debian and RedHat systems + variants, you
can install the `acl` package (if you add it to the `bacula_director_packages`
list, it'll be installed when this role is run).

Additionally, you may need to install a Python package to allow testing of your
catalog database from Ansible. For Postgres, that package is `python3-psycopg2`.
You can add this to the role's package list, or separately install it (possibly
through `pip3`?).

Role Variables
--------------

The role variables follow a very similar format to those in the
[dudefellah.bacula.bacula_daemon](github.com/dudefellah/ansible-collection-bacula/roles/bacula_daemon)
role. Names in this role that start with `bacula_director_` map to names in that
role that start with `bacula_daemon_`. For more information on thse values,
please refer to the [defaults/main.yml](github.com/dudefellah/ansible-collection-bacula/roles/bacula_daemon/defaults/main.yml)
file which has annotations for all of the available values.

In addition to those values, a few extras have been added to this role. You can
find documentation for those in this role's
[defaults/main.yml](defaults/main.yml) file.

Dependencies
------------

For testing the catalog database, either the
[community.mysql](https://galaxy.ansible.com/community/mysql) or
[community.postgresql](https://galaxy.ansible.com/community/postgresql)
collections should be installed.

Example Playbook
----------------

See the playbooks for [this collection](github.com/dudefellah/ansible-collection-bacula/playbooks)
for some examples on the use of this, and other related roles.

If you're installing the Bacula Director onto a Debian or Debian-variant system, 
you should be aware that those packages try to automatically prepare the
database, so you might want to take advantage of this by prepopulating some
`debconf` values (with
[ansible.builtin.debconf](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/debconf_module.html))
before using this role. An example of this can be found in the
[playbooks](github.com/dudefellah/ansible-collection-bacula/playbooks/debian-example.yml).

License
-------

GPLv2+

Author Information
------------------

Dan - github.com/dudefellah
