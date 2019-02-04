"""
    SoftLayer.tests.CLI.modules.summary_tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :license: MIT, see LICENSE for more details.
"""
from SoftLayer import testing

import json
import mock
import io
import shlex

from prompt_toolkit.shortcuts import prompt
from SoftLayer.shell import core

class ShellTests(testing.TestCase):
    #def test_shell(self):
     #   result = self.run_command(['shell'])
      #  self.assertIsInstance(result.exception, io.UnsupportedOperation)

    @mock.patch('prompt_toolkit.shortcuts.prompt')
    def test_shell_quit(self, prompt):
        prompt.return_value = "quit"
        result = self.run_command(['shell'])
        self.assertEqual(result.exit_code, 0)

    #@mock.patch('SoftLayer.CLI.core.main')
    #@mock.patch('prompt_toolkit.shortcuts.prompt')
    #def test_shell_ValueError_And_ShellExit(self, main, prompt):
     #   main.side_effect = [ValueError, core.ShellExit]
      #  prompt.return_value = ["vs list", "quit"]
       # result = self.run_command(['shell'])
        #self.assertEqual(result.exit_code, 1)

    #@mock.patch('SoftLayer.CLI.core.main')
    #@mock.patch('prompt_toolkit.shortcuts.prompt')
    #def test_shell_SysExit(self, main, prompt):
     #   main.side_effect = [SystemExit, core.ShellExit]
      #  prompt.return_value = ["vs list", "quit"]
       # result = self.run_command(['shell'])
        #self.assertEqual(result.exit_code, 0)

    #@mock.patch('SoftLayer.CLI.core.main')
    #@mock.patch('prompt_toolkit.shortcuts.prompt')
    #def test_shell_EOF(self, main, prompt):
     #   main.side_effect = EOFError
      #  prompt.return_value = "vs list"
       # result = self.run_command(['shell'])
        #self.assertEqual(result.exit_code, 1)
