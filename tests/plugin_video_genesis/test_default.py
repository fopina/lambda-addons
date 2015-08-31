from .genesistestcase import GenesisTestCase


class TestDefault(GenesisTestCase):
    def test_movies_featured(self):
        self.execute(
            'default.py',
            '1',
            '?action=movies&url=featured'
        )

        self.assertGreater(len(self.xbmcplugin.addDirectoryItem.call_args_list), 1)
        for call in self.xbmcplugin.addDirectoryItem.call_args_list[:-1]:
            self.assertIn('default.py?action=play&name=', call[1]['url'])

    def test_movies_box_office(self):
        self.execute(
            'default.py',
            '1',
            '?action=movies&url=boxoffice'
        )

        self.assertGreater(len(self.xbmcplugin.addDirectoryItem.call_args_list), 1)
        for call in self.xbmcplugin.addDirectoryItem.call_args_list[:-1]:
            self.assertTrue(call[1]['url'].startswith('default.py?action=play&name='))
