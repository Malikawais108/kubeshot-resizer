import unittest
from app.main import app
from io import BytesIO
from PIL import Image

class TestKubeshotResizerAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_resize_endpoint_with_valid_image(self):
        # Create a dummy image in memory
        img = Image.new('RGB', (500, 500), color='blue')
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        # Send POST request to /resize
        response = self.client.post(
            '/resize',
            content_type='multipart/form-data',
            data={'image': (img_bytes, 'test.png')}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'image/png')

    def test_resize_endpoint_without_image(self):
        response = self.client.post('/resize', data={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()

