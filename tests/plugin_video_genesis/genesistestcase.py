from ..koditestcase import KodiTestCase
from mock import patch


class MockThread(object):
    def __init__(self):
        pass

    def start(self):
        self.run()

    def join(self):
        pass

    def is_alive(self):
        return False


class GenesisTestCase(KodiTestCase):
    def setUp(self):
        super(GenesisTestCase, self).setUp()
        self.thread_patcher = patch('threading.Thread', MockThread)
        self.thread_patcher.start()

    def tearDown(self):
        super(GenesisTestCase, self).tearDown()
        self.thread_patcher.stop()
