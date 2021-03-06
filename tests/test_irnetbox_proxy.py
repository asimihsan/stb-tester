import imp
import os
import unittest


IRNetBoxProxy = imp.load_source(
    "irnetbox_proxy",
    os.path.join(os.path.dirname(__file__), "..", "irnetbox-proxy")
).IRNetBoxProxy


class ProxyTest(unittest.TestCase):

    def test_id_generation(self):
        proxy = IRNetBoxProxy("no_address")
        for i in range(65536):
            self.assertEqual(proxy.make_id(), i)
        self.assertEqual(proxy.make_id(), 0)

    def test_id_generation_skips_active_ids(self):
        proxy = IRNetBoxProxy("no_address")
        proxy.async_commands[2] = None

        self.assertEqual(proxy.make_id(), 0)
        self.assertEqual(proxy.make_id(), 1)
        self.assertEqual(proxy.make_id(), 3)

    def test_replace_sequence(self):
        proxy = IRNetBoxProxy("no_address")
        data = "YYYY"
        self.assertEqual(proxy.replace_sequence_id(data, 1), "\x00\x01YY")
        self.assertEqual(proxy.replace_sequence_id(data, 65535), "\xff\xffYY")


if __name__ == "__main__":
    unittest.main()
