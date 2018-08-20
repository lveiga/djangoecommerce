from django.test import TestCase, Client


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get('/core')
        self.assertEquals(response.status_code, 200)

    def test_status_used(self):
        response = self.client.get('/core')
        self.assertTemplateUsed(response, 'index.html')