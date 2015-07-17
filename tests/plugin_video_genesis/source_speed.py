# no test_ prefix in the filename so it is skipped by untargetted test run
from .genesistestcase import GenesisTestCase


class SourceSpeedTest(GenesisTestCase):
    def test_play(self):
        '''
        plugin.video.genesis/modules/sources$ ls *.py | grep "mv" | sed -e "s/\.py$//g" | sed -e 's/_mv$//g' | sed -e 's/_mv_tv$//g'
        '''
        all_sources = [
            'afdah', 'alluc', 'einthusan', 'furk', 'gvcenter', 'icefilms', 'iwatchonline', 'movie25',
            'movieshd', 'moviestorm', 'movietube', 'moviezone', 'muchmovies', 'onlinemovies', 'playbox',
            'primewire', 'sweflix', 'vidics', 'vkbox', 'watchfree', 'wso', 'xmovies8', 'yify', 'yifystream'
        ]

        src = ''

        def getSetting(x):
            if x == 'sources_timeout_beta':
                return 10
            if x == 'autoplay':
                return 'false'
            if x == src:
                return 'true'
            return 'false'

        self.xbmc.getInfoLabel = lambda x: 'default.py'

        self.xbmcaddon.Addon().getSetting = getSetting

        from time import time

        url_list = []
        for isrc in all_sources:
            st = time()
            src = isrc
            self.xbmcgui.Dialog().select.call_args_list = []
            self.execute(
                'default.py',
                '1',
                '?action=play&name=Ex+Machina+%282015%29&title=Ex+Machina&year=2015&imdb=0470752&url=http%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0470752%2F&t=20150619095007045928'
            )
            print('%s: %0.2fs - %d results' % (src, time() - st, len(self.xbmcgui.Dialog().select.call_args_list)))
            if len(self.xbmcgui.Dialog().select.call_args_list) > 0:
                url_list += self.xbmcgui.Dialog().select.call_args_list[0][0][1]

        self.assertGreater(len(url_list), 0)

if __name__ == '__main__':
    import nose
    import sys
    sys.argv.append('-s')
    nose.runmodule()
