# Ansible Collection - my_own_namespace.yandex_cloud_elk

Collection with module for creating files based on path and content.

Use case:

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
