# Facts

## Variables

`facts_template_directory`: set to a directory containing Jinja2 templates that should be added to the local facts directory. Default: don't add any facts.

`facts_fact_path`: the directory that Ansible is using to store local facts scripts. Default: `/etc/ansible/facts.d`

`facts_reload`: after adding facts this role will reload all local facts. You may not want that to happen immediately. If you want to manage this yourself, set `facts_reload` to something falsey.

## Handlers

`reload ansible_local facts`: run this when you want to relaod all `ansible_local` facts. this is run automatically whenever a fact is added to the facts directory by this role, unless `facts_reload` is falsey.
