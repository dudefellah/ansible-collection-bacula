dudefellah.bacula.bacula_daemon
=========

This is a generic Bacula installation and configuration role meant to allow you
to setup your Bacula installs from Ansible. It's called "`bacula_daemon`" as a
sort of generic term to refer to Bacula's director, storage and file daemons.

The default config refers to the standard File Daemon config availble in Debian
Bullseye's `bacula-fd` package. This should be reasonably close to the most
common use of this role, but you can easily customize it to deploy the other
daemons and install configurations appropriate to those daemons.

The primary factors determining what gets installed, what configurations are
created, and how those configurations get tested are the settings built for:

* `bacula_daemon_base_config_file` - Your resources get imported as separate
  configs under `bacula_daemon_config_root.path`, and they'll be all included
  into the config file referred to by `bacula_daemon_base_config_file`.
  This should normally be your `bacula-dir.conf`, `bacula-sd.conf`, or
  `bacula-fd.conf`. You can set this as a relative (to
  `bacula_daemon_config_root.path`) value, or absolute.

* `bacula_daemon_config_root` - If you're installing multiple daemons on a
   single host, you'll probably want to set the `path` value in this dict to
   something unique for your daemon so that you can avoid overlap of
   auto-generated filenames. If you're explicitly setting the filenames for
   each resource, this is less important.

   Just be aware that if you set `bacula_daemon_config_root.path`, the relative
   path for `bacula_daemon_base_config_file` will be under this path. If you're
   trying to separate your split-up config files from your base file, you might
   want to make this value absolute.

   Eg.

```
# Place the root config at /etc/bacula/bacula-dir.conf so that the default
# service configuration finds it.
bacula_daemon_base_config_file: /etc/bacula/bacula-dir.conf
# Split up the resources under /etc/bacula/director/...
bacula_daemon_config_root:
  path: /etc/bacula/director
  ... etc
```

* `bacula_daemon_default_template_validate` - This tells Ansible how to validate
  your templates. Typically you'll want one of `bacula-dir -t %s`,
  'bacula-sd -t %s', or `bacula-df -t %s`. This can also be set per resource in
  `bacula_daemon_resources`, with the `template_validate` keyword inside the
  `bacula_daemon_resource_definition` entry, but probably makes most sense to
  live in `bacula_daemon_default_template_validate` since you're unlikely to
  want to use validate with a different daemon binary.

  An additional thing to be aware of here is that validation for the separate
  resources defined under `bacula_daemon_resources` can't happen on a one-by-one
  basis, since the validation happens in a temp directory. This role tries to
  test a single, complete test file with template validation before writing out
  the individual resources. In principle, if one large file of resources passes
  Bacula's syntax checks, then the separate resources should also pass the test.
  Testing the single file first helps us avoid writing out configurations that
  might be broken, so it makes cleanup easier (or not required).

* `bacula_daemon_resources` - You're want to set this no matter what install
  you're doing. Just note that the resource file definitions don't "know" the
  difference between different resource types (Directors vs FileSets vs Messages
  etc.), so it can't check to see if you used a proper config keyword or not.
  Instead, the template does some simple mapping of variable names and types
  into resource file definitions. If you have appropriate template verification
  configured, you should be able to save yourself from typos and misallocated
  resources before you cause yourself any trouble.

Further documentation on all available values in this role can be found in the
annotations available in [defaults/main.yml](defaults/main.yml).

Requirements
------------

None.

Role Variables
--------------

In addition to the description above, you can look at the variable annotations
in [defaults/main.yml](defaults/main.yml).

Dependencies
------------

This role is a part of the [dudefellah.bacula](github.com/dudefellah/ansible-collection-bacula)
collection and uses some custom filters, so that collection should be installed
in connection with this role. You should look at the collection documentation
to see if there are any additional requirements or dependencies.

Example Playbook
----------------

See the [github.com/dudefellah/ansible-collection-bacula/playbooks](github.com/dudefellah/ansible-collection-bacula/playbooks)
directory for some example playbooks.

License
-------

GPLv2+

Author Information
------------------

Dan - github.com/dudefellah
