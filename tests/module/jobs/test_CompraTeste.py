import unittest
from src.module.jobs import compra as T

class CompraTeste(unittest.TestCase):

    def test_frete_gratis(self):
        nova_compra = T.Compra()
        self.assertEqual(200,nova_compra.frete_gratis(200))
#
# if __name__ == "__main__":
#     unittest.main()
