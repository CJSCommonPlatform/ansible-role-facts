from ansiblelint import AnsibleLintRule

class ShellAltChage(AnsibleLintRule):
    id = 'MOJCPP0101'
    shortdesc = 'Use the chage module'
    description = 'You probably want to use this instead of running `chage` in a shell: https://github.com/barkingiguana/ansible-role-chage'
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['__ansible_module__'] not in ['shell', 'command']:
            return False
        if 'chage' in task['action']['__ansible_arguments__']:
            return True
        return False
