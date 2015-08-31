# no test_ prefix in the filename so it is skipped by untargetted test run
import test_movie_sources


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

    def movie_source(self, source_name):
        print
        print source_name,
        try:
            t = super(SourceSpeedTest, self).movie_source(source_name)
            SourceSpeedTest.times.append((t, source_name))
            print t,
        except AssertionError as e:
            SourceSpeedTest.errors.append((source_name, e.message))
        print

if __name__ == '__main__':
    import nose
    import sys
    sys.argv.append('-s')
    nose.runmodule()
