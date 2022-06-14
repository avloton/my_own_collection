Role Name
=========

Role for use module `my_own_module`.

Role Variables
--------------
 
path - path to the file.

content - content of the file.

Example Playbook
----------------

```yaml
---
- name: Test new module
  hosts: localhost
  collections:
    - "my_own_namespace.yandex_cloud_elk"
  tasks:
    - import_role:
        name: test_role
```
