from image_app.models import Image


def image_by_url(url: str) -> Image:
    return Image.objects.filter(url=url).first()
