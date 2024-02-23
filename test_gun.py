from unittest import TestCase
import gun


class TestGun(TestCase):
    # def setUp(self):
    #     self.gun_chamber = []
    #
    # def tearDown(self):
    #     self.gun_chamber = []

    def test_fire(self):

        revolver = gun.Gun("revolver")
        bullet = gun.Bullet("revolver")

        revolver.gun_chamber = []

        revolver.load(bullet)
        revolver.load(bullet)
        revolver.load(bullet)

        revolver.fire(bullet)
        self.assertEqual(2, revolver.check_ammunition())

    def test_load(self):
        revolver = gun.Gun("revolver")
        bullet = gun.Bullet("revolver")

        revolver.gun_chamber = []

        revolver.load(bullet)

        self.assertEqual(1, revolver.check_ammunition())

    def test_check_ammunition(self):
        revolver = gun.Gun("revolver")
        bullet = gun.Bullet("revolver")

        revolver.gun_chamber = []

        revolver.load(bullet)
        revolver.load(bullet)

        self.assertEqual(2, revolver.check_ammunition())

    # def test_different_gun_bullet_cannot_be_added(self):
    #     revolver = gun.Gun("revolver")
    #     bullet = gun.Bullet("revolver")
    #
    #     revolver.gun_chamber = []
    #
    #     revolver.load(bullet)
