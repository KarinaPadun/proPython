from django.test import TestCase

class IndexViewTests(TestCase):

    def test_index_view_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

class DetailViewTests(TestCase):

    def test_detail_view_returns_200(self):
        obj = Model.objects.create(...)
        response = self.client.get(f'/detail/{obj.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_uses_correct_template(self):
        obj = Model.objects.create(...)
        response = self.client.get(f'/detail/{obj.pk}/')
        self.assertTemplateUsed(response, 'detail.html')

    def test_detail_view_shows_correct_object(self):
        obj = Model.objects.create(...)
        response = self.client.get(f'/detail/{obj.pk}/')
        self.assertContains(response, obj.name)

class CreateViewTests(TestCase):

    def test_create_view_returns_200_on_GET(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_create_view_uses_correct_template_on_GET(self):
        response = self.client.get('/create/')
        self.assertTemplateUsed(response, 'create.html')

    def test_create_view_redirects_on_valid_POST(self):
        data = {'name': 'Test Name'}
        response = self.client.post('/create/', data)
        self.assertRedirects(response, '/home/')

    def test_create_view_shows_errors_on_invalid_POST(self):
        data = {}
        response = self.client.post('/create/', data)
        self.assertContains(response, 'This field is required.')

class EditViewTests(TestCase):

    def test_edit_view_returns_200_on_GET(self):
        obj = Model.objects.create(...)
        response = self.client.get(f'/edit/{obj.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_edit_view_uses_correct_template_on_GET(self):
        obj = Model.objects.create(...)
        response = self.client.get(f'/edit/{obj.pk}/')
        self.assertTemplateUsed(response, 'edit.html')

    def test_edit_view_redirects_on_valid_POST(self):
        obj = Model.objects.create(...)
        data = {'name': 'Updated Name'}
        response = self.client.post(f'/edit/{obj.pk}/', data)
        self.assertRedirects(response, '/home/')

