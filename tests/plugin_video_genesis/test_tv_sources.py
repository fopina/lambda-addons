from .genesistestcase import GenesisTestCase


class TestSources(GenesisTestCase):
    def test_alluc(self):
        self.skipTest("alluc not working anymore?")

    def test_animeultima(self):
        self.tv_source(
            'animeultima_tv',
            '0434665',
            '74796',
            'Bleach',
            'Bleach',
            '2004',
            None,
            '1',
            '1',
            '/watch/bleach-english-subbed-dubbed-online/',
            '/bleach-episode-1/',
            'Animeultima'
        )

    def test_clickplay(self):
        self.skipTest("to be revisited")
        self.tv_source(
            'clickplay_tv',
            '0944947',
            None,
            'Game of Thrones',
            'Game of Thrones',
            '2011',
            None,
            '1',
            '1',
            '/tv-shows/game-of-thrones-17/',
            '/tv-shows/game-of-thrones-17/season-1/episode-1',
            'Animeultima'
        )

    def test_directdl(self):
        self.skipTest("does it work??")
        self.tv_source(
            'directdl_tv',
            '0944947',
            None,
            'Game of Thrones',
            'Game of Thrones',
            '2011',
            None,
            '1',
            '1',
            '/tv-shows/game-of-thrones-17/',
            '/tv-shows/game-of-thrones-17/season-1/episode-1',
            'Animeultima'
        )

    def test_furk(self):
        self.skipTest("private host, need login")
        self.tv_source(
            'furk_mv_tv',
            '0944947',
            None,
            'Game of Thrones',
            'Game of Thrones',
            '2011',
            None,
            '1',
            '1',
            '/tv-shows/game-of-thrones-17/',
            '/tv-shows/game-of-thrones-17/season-1/episode-1',
            'Animeultima'
        )

    def test_gvcenter(self):
        self.tv_source(
            'gvcenter_mv_tv',
            '0944947',
            None,
            'Game of Thrones',
            'Game of Thrones',
            '2011',
            None,
            '1',
            '1',
            '522',
            '522 S01E01',
            'GVcenter'
        )

    def test_icefilms(self):
        self.tv_source(
            'icefilms_mv_tv',
            '0944947',
            None,
            'Game of Thrones',
            'Game of Thrones',
            '2011',
            None,
            '1',
            '1',
            '/tv/series/3/2908?',
            '/ip.php?v=131216',
            'Icefilms'
        )

    def test_iwatchonline(self):
        self.skipTest("redirect loop on get sources?")
        self.tv_source(
            'iwatchonline_mv_tv',
            '0944947',
            None,
            'Game of Thrones',
            'Game of Thrones',
            '2011',
            None,
            '1',
            '1',
            '/episode/1280-game-of-thrones',
            '/episode/1280-game-of-thrones-s01e01',
            'Animeultima'
        )

    def test_moviestorm(self):
        self.skipTest("cant get sources")
        self.tv_source(
            'moviestorm_mv_tv',
            '0944947',
            None,
            'Game of Thrones',
            'Game of Thrones',
            '2011',
            None,
            '1',
            '1',
            '/view/114-watch-game-of-thrones.html',
            '/view/114-watch-game-of-thrones.html?season=1&episode=1',
            'Moviestorm'
        )

    def test_movietube(self):
        self.tv_source(
            'movietube_mv_tv',
            '',
            None,
            'The Big Bang Theory',
            'The Big Bang Theory',
            '',
            None,
            '3',
            '1',
            'The Big Bang Theory',
            'koClLk2wIYo|01',
            'Movietube'
        )

    def test_ororo(self):
        self.tv_source(
            'ororo_tv',
            '',
            None,
            'The Big Bang Theory',
            'The Big Bang Theory',
            '',
            None,
            '3',
            '1',
            'The Big Bang Theory',
            'koClLk2wIYo|01',
            'Movietube'
        )
        pass

    def test_playbox(self):
        # playbox_mv_tv.py
        pass

    def test_primewire(self):
        # primewire_mv_tv.py
        pass

    def test_vidics(self):
        # vidics_mv_tv.py
        pass

    def test_vkbox(self):
        # vkbox_mv_tv.py
        pass

    def test_watchfree(self):
        # watchfree_mv_tv.py
        pass

    def test_watchseries(self):
        # watchseries_tv.py
        pass

    def test_wso(self):
        # wso_mv_tv.py
        pass

    def test_yifystream(self):
        # yifystream_mv_tv.py
        pass

    def tv_source(self, source_name, imdb, tvdb, show, show_alt, year, episode_date, season, episode, expected_show_url, expected_episode_url, expected_provider):
        from modules.sources import sources
        from time import sleep
        hosts = sources()

        mod = __import__('modules.sources.' + source_name, fromlist=['source'])
        source = mod.source()

        # some sources fail some times, so try at least
        # 3 times before actual fail (3rd time's a charm)
        attempt = 3
        while True:
            try:
                url = source.get_show(imdb, tvdb, show, show_alt, year)
                self.assertEqual(url, expected_show_url)
                break
            except AssertionError:
                attempt -= 1
                if attempt < 1:
                    raise
                sleep(0.2)

        episode_url = source.get_episode(url, imdb, tvdb, show, episode_date, season, episode)
        self.assertEqual(episode_url, expected_episode_url)

        srcs = source.get_sources(url, hosts.hosthdfullDict, hosts.hostsdfullDict, hosts.hostlocDict)

        self.assertGreater(len(srcs), 0, msg='No sources found (some error?)')

        for src in srcs:
            self.assertEqual(src['provider'], expected_provider)
