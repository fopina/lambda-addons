import sys

from test.koditestcase import KodiTestCase


class TestDefault(KodiTestCase):
    def test_movies_featured(self):
        sys.argv = [
            'default.py',
            '1',
            '?action=movies_featured'
        ]
        import default

        self.assertGreater(len(self.xbmcplugin.addDirectoryItem.call_args_list), 0)
        for call in self.xbmcplugin.addDirectoryItem.call_args_list:
            self.assertTrue(call[1]['url'].startswith('default.py?action=play&name='))

    def test_play(self):
        all_sources = ['afdah', 'alluc', 'einthusan', 'furk', 'gvcenter', 'icefilms', 'iwatchonline', 'mintmovies',
                       'movie25', 'movieshd', 'moviestorm', 'movietube', 'moviezone', 'muchmovies', 'noobroom',
                       'onlinemovies', 'primewire', 'sweflix', 'vidics', 'vkbox', 'watchfree', 'wso', 'yify',
                       'yifystream']

        src = ''

        def getSetting(x):
            if x == 'sources_timeout_beta': return 10
            if x == 'autoplay': return 'false'
            if x == src: return 'true'
            return 'false'

        self.xbmc.getInfoLabel = lambda x: 'default.py'

        self.xbmcaddon.Addon().getSetting = getSetting

        sys.argv = [
            'default.py',
            '1',
            ''
        ]
        import default
        from time import time

        sys.argv = [
            'default.py',
            '1',
            '?action=play&name=Ex+Machina+%282015%29&title=Ex+Machina&year=2015&imdb=0470752&url=http%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0470752%2F&t=20150619095007045928'
        ]

        url_list = []
        for isrc in all_sources:
            st = time()
            src = isrc
            self.xbmcgui.Dialog().select.call_args_list = []
            default.main()
            print('%s: %0.2fs - %d results' % (src, time()-st, len(self.xbmcgui.Dialog().select.call_args_list)))
            if len(self.xbmcgui.Dialog().select.call_args_list) > 0:
                url_list += self.xbmcgui.Dialog().select.call_args_list[0][0][1]

        self.assertGreater(len(url_list), 0)