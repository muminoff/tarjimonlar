from django.test import TestCase
from core.models import Company


class CompanyTestCase(TestCase):

    def setUp(self):
        self.company = Company.objects.create(name="My company")

    def test_company_name(self):
        return self.assertEqual("My company", self.company.name)
