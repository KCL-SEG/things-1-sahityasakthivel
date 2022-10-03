from django.test import TestCase

# Create your tests here.
class UnitTestCase(TestCase):
    def test(self):
        a = Thing(name = "pen", description = "writing",quantity = 2);
        try:
             a.full_clean()
        except (ValidationError):
            self.fail("FAiled")
