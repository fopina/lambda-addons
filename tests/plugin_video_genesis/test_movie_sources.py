from genesistestcase import GenesisTestCase


class TestSources(GenesisTestCase):
    longMessage = True

    def test_einthusan_mv(self):
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

    def test_furk_mv_tv(self):
        self.skipTest("needs login, private cloud")

    def get_box_movies(self):
        if not getattr(self, 'movies', None):
            import urlparse

            self.execute(
                'default.py',
                '1',
                '?action=movies&url=boxoffice'
            )
            self.movies = []

            for x in self.xbmcplugin.addDirectoryItem.call_args_list:
                pars = dict(urlparse.parse_qsl(x[1]['url'].replace('default.py?', '')))
                if pars['action'] == 'play':
                    self.movies.append(pars)

        self.assertEqual(len(self.movies), 20, msg='Failed to retrieve box office list')

    def movie_source(self, source_name):
        return 0
        self.get_box_movies()

        from resources.lib.sources import sources
        import time

        hosts = sources()

        mod = __import__('resources.lib.sources.' + source_name, fromlist=['source'])
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
                    self.assertIsNotNone(src['provider'])
                last_exception = None
                break
            except AssertionError as e:
                last_exception = e

        if last_exception is not None:
            raise last_exception

        return st


def list_all_source_modules():
    # crappy implementation to avoid patching xbmc module only to list modules
    # resources can be imported, but resources.lib.sources cannot
    import os
    import resources
    exclude = [
        'furk_mv_tv',
        'einthusan_mv',
    ]
    return [
        x[:-3]
        for x in os.listdir(resources.__path__[0] + '/lib/sources')
        if x.endswith('.py') and x.find('_mv') > -1 and x[:-3] not in exclude
    ]


def some_generator(source):
    def test(self=None):
        if self:
            self.movie_source(source)
    return test

for source in list_all_source_modules():
    test_name = 'test_%s' % source
    test = some_generator(source)
    setattr(TestSources, test_name, test)
