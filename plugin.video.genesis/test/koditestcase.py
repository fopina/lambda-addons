'''
original at https://github.com/powlo/weather.metoffice
'''

import unittest
from mock import patch, Mock


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
        self.module_patcher.start()
        self.addon_patcher.start()
        self.translate_patcher.start()

        self.xbmcaddon.Addon().getAddonInfo = Mock(return_value='')
        self.xbmcaddon.Addon().getSetting = Mock(return_value='false')

    def tearDown(self):
        self.module_patcher.stop()
        self.addon_patcher.stop()
        self.translate_patcher.stop()
