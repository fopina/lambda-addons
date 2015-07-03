import sys

from test.koditestcase import KodiTestCase


class TestSources(KodiTestCase):

    def test_play_alluc(self):
        sys.argv = [
            'default.py',
            '1',
            ''
        ]

        from default import resolver

        __builtins__['global_sources'] = []

        resolver().sources_movie('Ex Machina', 'Ex Machina', '2015', 'http://www.imdb.com/title/tt0470752/', 'alluc')

        self.assertGreater(len(global_sources), 0)
        for src in global_sources:
            self.assertEqual(src['provider'], 'Alluc')

    def test_play_movieshd(self):
        sys.argv = [
            'default.py',
            '1',
            ''
        ]

        from default import resolver

        __builtins__['global_sources'] = []

        resolver().sources_movie('Ex Machina', 'Ex Machina', '2015', 'http://www.imdb.com/title/tt0470752/', 'movieshd')

        self.assertGreater(len(global_sources), 0)
        for src in global_sources:
            self.assertEqual(src['provider'], 'MoviesHD')
