import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTest(unittest.TestCase):
	def test_eat_healthy(self):
		"""eat should have a positive message for healthy eating"""
		self.assertEqual(
			eat("broccoli", is_healthy=True),
			"I'm eating broccoli, because my body is a temple"
		)
	def test_eat_unhealthy(self):
		"""eat should have a positive message for unhealthy eating"""
		self.assertEqual(
			eat("pizza", is_healthy=False),
			"I'm eating pizza, because YOLO!"
		)

	def test_eat_healthy_boolean(self):
		"""is_heathy must be a bool"""
		with self.assertRaises(ValueError):
			eat("pizza", is_healthy="who cares?")

	def test_short_nap(self):
		self.assertEqual(
			nap(1),
			"I'm feeling refreshed after my 1 hour nap"
		)
	def test_long_nap(self):
		self.assertEqual(
			nap(3), "Ugh I overslept. I didn't mean to nap"
		)

	def test_is_funny_tim(self):
		self.assertEqual(is_funny("tim"), "tim should not be funnny.")

	def test_is_funny_anyone_else(self):
		self.assertTrue(is_funny("blue"), "blue should be funny")
		self.assertTrue(is_funny("tammy"), "tammy should be funny")
		self.assertTrue(is_funny("sven"), "sven should be funny")

	def test_laugh(self):
		self.assertIn(laugh(), ('lol', 'haha', 'tehteh'))

if __name__ == "__main__":
	unittest.main()
