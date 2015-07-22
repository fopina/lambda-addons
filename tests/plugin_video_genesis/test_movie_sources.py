from .genesistestcase import GenesisTestCase


class TestSources(GenesisTestCase):
    def test_afdah(self):
        self.movie_source(
            'afdah_mv',
            '0470752',
            'Ex Machina',
            '2015',
            '/watch?v=Ex_Machina_2015',
            'Afdah'
        )

    def test_alluc(self):
        self.movie_source(
            'alluc_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            'Ex Machina 2015',
            'Alluc'
        )

    def test_einthusan(self):
        self.movie_source(
            'einthusan_mv',
            '4684258',
            '36 Vayadhinile',
            '2015',
            '/movies/watch.php?tamilmoviesonline=36+Vayadhinile&lang=tamil&id=2668',
            'Einthusan'
        )

    def test_furk(self):
        self.skipTest("needs login, private cloud")

    def test_gvcenter(self):
        self.movie_source(
            'gvcenter_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '1458',
            'GVcenter'
        )

    def test_icefilms(self):
        self.movie_source(
            'icefilms_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '/ip.php?v=210959&',
            'Icefilms'
        )

    def test_iwatchonline(self):
        self.movie_source(
            'iwatchonline_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '/movie/48651-ex-machina',
            'Iwatchonline'
        )

    def test_movie25(self):
        self.movie_source(
            'movie25_mv',
            '0470752',
            'Ex Machina',
            '2015',
            '/ex-machina-2015-57654.html',
            'Movie25'
        )

    def test_movieshd(self):
        self.movie_source(
            'movieshd_mv',
            '0470752',
            'Ex Machina',
            '2015',
            '/watch-online/ex-machina-2015.html',
            'MoviesHD'
        )

    def test_moviestorm(self):
        self.movie_source(
            'moviestorm_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '/view/11232-watch-ex-machina.html',
            'Moviestorm'
        )

    def test_movietube(self):
        self.movie_source(
            'movietube_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '0_KqHOgMi4g',
            'Movietube'
        )

    def test_moviezone(self):
        self.movie_source(
            'moviezone_mv',
            '0470752',
            'Ex Machina',
            '2015',
            '/ex-machina-2015/',
            'Moviezone'
        )

    def test_muchmovies(self):
        self.movie_source(
            'muchmovies_mv',
            '0470752',
            'Ex Machina',
            '2015',
            '/movies/ex-machina-2015',
            'Muchmovies'
        )

    def test_playbox(self):
        self.movie_source(
            'playbox_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '44578',
            'PlayBox'
        )

    def test_primewire(self):
        self.movie_source(
            'primewire_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '/watch-518174-Ex-Machina-online-free',
            'Primewire'
        )

    def test_pubfilm(self):
        self.movie_source(
            'pubfilm_mv',
            '0470752',
            'Ex Machina',
            '2015',
            '/2015/05/ex-machina-2015-full-hd.html',
            'Pubfilm'
        )

    def test_sweflix(self):
        self.movie_source(
            'sweflix_mv',
            '0470752',
            'Ex Machina',
            '2015',
            '2480',
            'Sweflix'
        )

    def test_vidics(self):
        self.movie_source(
            'vidics_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '/Film/Ex_Machina',
            'Vidics'
        )

    def test_vkbox(self):
        self.movie_source(
            'vkbox_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '/api/serials/get_movie_data/?id=4681',
            'VKBox'
        )

    def test_watchfree(self):
        self.movie_source(
            'watchfree_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '/watch-7e81e-Ex-Machina',
            'Watchfree'
        )

    def test_wso(self):
        self.movie_source(
            'wso_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '/ex-machina-2015/',
            'WSO'
        )

    def test_xmovies8(self):
        self.movie_source(
            'xmovies8_mv',
            '0470752',
            'Ex Machina',
            '2015',
            '/movie/ex-machina-2015-2/?vq=0',
            'Xmovies8'
        )

    def test_yify(self):
        self.movie_source(
            'yify_mv',
            '0470752',
            'Ex Machina',
            '2015',
            '/watch-ex-machina-online-free-yify/',
            'YIFY'
        )

    def test_yifystream(self):
        self.movie_source(
            'yifystream_mv_tv',
            '0470752',
            'Ex Machina',
            '2015',
            '/ex-machina-2015',
            'YIFYstream'
        )

    def movie_source(self, source_name, imdb, title, year, expected_url, expected_provider, attempts=3):
        from modules.sources import sources
        from time import sleep
        hosts = sources()

        mod = __import__('modules.sources.' + source_name, fromlist=['source'])
        source = mod.source()

        # some sources fail some times, so try at least _attempts_
        # default is 3, as third time's a charm
        while True:
            try:
                url = source.get_movie(imdb, title, year)
                self.assertEqual(url, expected_url)
                break
            except AssertionError:
                attempts -= 1
                if attempts < 1:
                    raise
                sleep(0.2)

        srcs = source.get_sources(url, hosts.hosthdfullDict, hosts.hostsdfullDict, hosts.hostlocDict)

        self.assertGreater(len(srcs), 0, msg='No sources found (some error?)')

        for src in srcs:
            self.assertEqual(src['provider'], expected_provider)
