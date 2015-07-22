# no test_ prefix in the filename so it is skipped by untargetted test run

import test_movie_sources
import timeit
import functools


class SourceSpeedTest(test_movie_sources.TestSources):
    @classmethod
    def setUpClass(cls):
        cls.times = []
        cls.errors = []

    @classmethod
    def tearDownClass(cls):
        cls.times.sort()

        print
        print 'Timings:'
        for t, name in cls.times:
            print '\t%s: %0.2f' % (name, t)

        print
        print 'Errors:'
        for x in cls.errors:
            print '\t%s: %s' % x

    def movie_source(self, source_name, imdb, title, year, expected_url, expected_provider, attempts=3):
        try:
            t = timeit.timeit(functools.partial(super(SourceSpeedTest, self).movie_source, source_name, imdb, title, year, expected_url, expected_provider, attempts=1), number=1)
            SourceSpeedTest.times.append((t, source_name))
        except AssertionError as e:
            SourceSpeedTest.errors.append((source_name, e.message))

if __name__ == '__main__':
    import nose
    import sys
    sys.argv.append('-s')
    nose.runmodule()
