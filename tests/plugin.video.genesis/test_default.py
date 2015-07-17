from koditestcase import KodiTestCase


class TestDefault(KodiTestCase):
    def test_movies_featured(self):
        self.execute(
            'default.py',
            '1',
            '?action=movies_featured'
        )

        self.assertGreater(len(self.xbmcplugin.addDirectoryItem.call_args_list), 0)
        for call in self.xbmcplugin.addDirectoryItem.call_args_list:
            self.assertTrue(call[1]['url'].startswith('default.py?action=play&name='))
