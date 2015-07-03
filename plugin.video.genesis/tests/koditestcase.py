'''
original at https://github.com/powlo/weather.metoffice
'''

import unittest
from mock import patch, Mock
import runpy
import sys


class MockThread(object):
    def __init__(self):
        pass

    def start(self):
        self.run()

    def join(self):
        pass

    def is_alive(self):
        return False


class KodiTestCase(unittest.TestCase):
    def setUp(self):
        # Mock up any calls to modules that cannot be imported
        self.xbmc = Mock()
        self.xbmcgui = Mock()
        self.xbmcplugin = Mock()
        self.xbmcaddon = Mock()
        self.xbmcaddon.Addon = Mock()
        self.xbmcvfs = Mock()

        modules = {
            'xbmc': self.xbmc,
            'xbmcgui': self.xbmcgui,
            'xbmcaddon': self.xbmcaddon,
            'xbmcplugin': self.xbmcplugin,
            'xbmcvfs': self.xbmcvfs,
        }

        self.module_patcher = patch.dict('sys.modules', modules)
        self.addon_patcher = patch('xbmcaddon.Addon')
        self.translate_patcher = patch('xbmc.translatePath')
        self.thread_patcher = patch('threading.Thread', MockThread)
        self.module_patcher.start()
        self.addon_patcher.start()
        self.translate_patcher.start()
        self.thread_patcher.start()

        self.xbmcaddon.Addon().getAddonInfo = Mock(return_value='')
        self.xbmcaddon.Addon().getSetting = Mock(return_value='false')
        self.plugin_default = 'default'

    def tearDown(self):
        self.module_patcher.stop()
        self.addon_patcher.stop()
        self.translate_patcher.stop()
        self.thread_patcher.stop()

    def execute(self, *args):
        tmp_argv = sys.argv
        sys.argv = args
        runpy.run_module(self.plugin_default)
        sys.argv = tmp_argv
