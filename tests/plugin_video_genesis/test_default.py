from .genesistestcase import GenesisTestCase


class TestDefault(GenesisTestCase):
    def test_movies_featured(self):
        self.execute(
            'default.py',
            '1',
            '?action=movies_featured'
        )

        self.assertGreater(len(self.xbmcplugin.addDirectoryItem.call_args_list), 0)
        for call in self.xbmcplugin.addDirectoryItem.call_args_list:
            self.assertTrue(call[1]['url'].startswith('default.py?action=play&name='))

    def test_movies_box_office(self):
        self.execute(
            'default.py',
            '1',
            '?action=movies_boxoffice'
        )

        self.assertGreater(len(self.xbmcplugin.addDirectoryItem.call_args_list), 0)
        for call in self.xbmcplugin.addDirectoryItem.call_args_list:
            try:
                self.assertTrue(call[1]['url'].startswith('default.py?action=play&name='))
            except AssertionError:
                self.assertTrue(call[1]['url'].startswith('default.py?action=movies&url=http%3A%2F%2Fwww.imdb.com%2Fsearch%2Ftitle%3Fcount%'))

