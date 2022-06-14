#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Module for creating files.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Module for creating files based on path and content.

options:
    path:
        description: Path to the file.
        required: true
        type: str
    content:
        description: Content of the file
        required: true
        type: str

author:
    - Anatoly K. (@avloton)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_own_namespace.yandex_cloud_elk.test_role:
    path: "hello world"
    content: "123"
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
path:
    description: Content of the file.
    type: str
    returned: always
    sample: 'hello world'
content:
    description: Content of the file.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule
from os.path import exists


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed = False,
        path = '',
        content = '',
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    #result['original_message'] = module.params['name']
    result['path'] = module.params['path']
    result['content'] = module.params['content']

    path = module.params['path']
    content = module.params['content']
    old_text = ''
    do_write = False
    file_exists = exists(path)

    if file_exists:
        with open(path, 'r') as f:
            old_text = f.read()
            if old_text != content:
                do_write = True

    if not file_exists or do_write:
        with open(path, 'w') as f:
            f.write(content)
        result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
