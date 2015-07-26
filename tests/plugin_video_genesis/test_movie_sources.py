from genesistestcase import GenesisTestCase


class TestSources(GenesisTestCase):
    def test_afdah(self):
        self.movie_source(
            'afdah_mv',
            'Afdah'
        )

    def test_alluc(self):
        self.movie_source(
            'alluc_mv_tv',
            'Alluc'
        )

    def test_einthusan(self):
        self.skipTest("no hindi movie filter..")
        '''
        Sample data for static test:
            'einthusan_mv',
            '4684258',
            '36 Vayadhinile',
            '2015',
            '/movies/watch.php?tamilmoviesonline=36+Vayadhinile&lang=tamil&id=2668',
            'Einthusan'
        '''

    def test_furk(self):
        self.skipTest("needs login, private cloud")

    def test_gvcenter(self):
        self.movie_source(
            'gvcenter_mv_tv',
            'GVcenter'
        )

    def test_icefilms(self):
        self.movie_source(
            'icefilms_mv_tv',
            'Icefilms'
        )

    def test_iwatchonline(self):
        self.movie_source(
            'iwatchonline_mv_tv',
            'Iwatchonline'
        )

    def test_movie25(self):
        self.movie_source(
            'movie25_mv',
            'Movie25'
        )

    def test_movieshd(self):
        self.movie_source(
            'movieshd_mv',
            'MoviesHD'
        )

    def test_moviestorm(self):
        self.movie_source(
            'moviestorm_mv_tv',
            'Moviestorm'
        )

    def test_movietube(self):
        self.movie_source(
            'movietube_mv_tv',
            'Movietube'
        )

    def test_moviezone(self):
        self.movie_source(
            'moviezone_mv',
            'Moviezone'
        )

    def test_muchmovies(self):
        self.movie_source(
            'muchmovies_mv',
            'Muchmovies'
        )

    def test_playbox(self):
        self.movie_source(
            'playbox_mv_tv',
            'PlayBox'
        )

    def test_primewire(self):
        self.movie_source(
            'primewire_mv_tv',
            'Primewire'
        )

    def test_pubfilm(self):
        self.movie_source(
            'pubfilm_mv',
            'Pubfilm'
        )

    def test_vidics(self):
        self.movie_source(
            'vidics_mv_tv',
            'Vidics'
        )

    def test_vkbox(self):
        self.movie_source(
            'vkbox_mv_tv',
            'VKBox'
        )

    def test_watchfree(self):
        self.movie_source(
            'watchfree_mv_tv',
            'Watchfree'
        )

    def test_wso(self):
        self.movie_source(
            'wso_mv_tv',
            'WSO'
        )

    def test_xmovies8(self):
        self.movie_source(
            'xmovies8_mv',
            'Xmovies8'
        )

    def test_yify(self):
        self.movie_source(
            'yify_mv',
            'YIFY'
        )

    def test_yifystream(self):
        self.movie_source(
            'yifystream_mv_tv',
            'YIFYstream'
        )


    def get_box_movie(self):
        if not hasattr(self,'movies'):
            import urlparse

            self.execute(
                'default.py',
                '1',
                '?action=movies_boxoffice'
            )
            self.movies = []

            for x in self.xbmcplugin.addDirectoryItem.call_args_list:
                pars = dict(urlparse.parse_qsl(x[1]['url'].replace('default.py?','')))
                if pars['action'] == 'play':
                    self.movies.append(pars)

        self.assertEqual(len(self.movies), 25, msg='Failed to retrieve box office list')

    def movie_source(self, source_name, expected_provider):
        self.get_box_movie()

        from modules.sources import sources
        import time

        hosts = sources()

        mod = __import__('modules.sources.' + source_name, fromlist=['source'])
        source = mod.source()

        last_exception = None

        for movie in self.movies:
            try:
                st = time.time()
                url = source.get_movie(movie['imdb'], movie['title'], movie['year'])
                self.assertIsNotNone(url, msg='movie not found')
                srcs = source.get_sources(url, hosts.hosthdfullDict, hosts.hostsdfullDict, hosts.hostlocDict)
                self.assertGreater(len(srcs), 0, msg='no sources found')
                st = time.time() - st
                for src in srcs:
                    self.assertEqual(src['provider'], expected_provider)
                last_exception = None
                break
            except AssertionError as e:
                last_exception = e

        if last_exception is not None:
            raise last_exception

        return st
