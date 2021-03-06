# -*- coding: utf-8 -*-

import unittest


class TestRedisCache(unittest.TestCase):

    initstring = 'redis://localhost:6379/0'

    def setUp(self):
        from shove.cache.redisdb import RedisCache
        self.cache = RedisCache(self.initstring)

    def tearDown(self):
        self.cache = None

    def test_getitem(self):
        self.cache['test'] = 'test'
        self.assertEqual(self.cache['test'], 'test')

    def test_setitem(self):
        self.cache['test'] = 'test'
        self.assertEqual(self.cache['test'], 'test')

    def test_delitem(self):
        self.cache['test'] = 'test'
        del self.cache['test']
        self.assertEqual('test' in self.cache, False)

    def test_get(self):
        self.assertEqual(self.cache.get('min'), None)

    def test_timeout(self):
        import time
        from shove.cache.redisdb import RedisCache
        cache = RedisCache(self.initstring, timeout=1)
        cache['test'] = 'test'
        time.sleep(3)
        def tmp(): #@IgnorePep8
            return cache['test']
        self.assertRaises(KeyError, tmp)


if __name__ == '__main__':
    unittest.main()
