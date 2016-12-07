# Copyright (c) 2013-2014 Will Thames <will@thames.id.au>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from ansiblelint import AnsibleLintRule
import re

class SymbolicFilePermissionsRule(AnsibleLintRule):
    id = 'MOJCPP0201'
    shortdesc = 'Use symbolic file permissions'
    description = 'Symbolic file permissions more clearly express what ' + \
        'we want the file permissions to be. ' + \
        'http://docs.ansible.com/ansible/file_module.html'
    tags = ['formatting']

    _modules = ['assemble', 'copy', 'file', 'ini_file', 'lineinfile',
                'replace', 'synchronize', 'template', 'unarchive']

    variable_regex = re.compile(r'\{\{')
    valid_mode_regex = re.compile(r'(?:[agou]{1,4}=[rstwxX]{1,6})(,(?:[agou]{1,4}=[rstwxX]{1,6})){0,3}')

    def matchtask(self, file, task):
        if task["action"]["__ansible_module__"] in self._modules:
            mode = task['action'].get('mode', None)
            if isinstance(mode, basestring):
                # We can't tell what the value is, if it's got a variable in it
                if self.variable_regex.match(mode):
                    return False
                return not self.valid_mode_regex.match(mode)
            return mode != None
