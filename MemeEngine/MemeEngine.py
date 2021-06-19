"""MemeEngine Create Meme image."""

from PIL import Image, ImageFont, ImageDraw
import os


class MemeEngine:
    """Create Meme Image."""

    def __init__(self, output_dir):
        """Create Directory."""
        self.output_dir = output_dir
        try:
            os.mkdir(output_dir)
        except OSError as error:
            print(error)
            pass

    def make_meme(self, img_path, body, author, width=500) -> str:
        """Create Meme Image from Path, body, and Author."""
        img = Image.open(img_path)
        # Set image size
        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
        # Get font
        fnt = ImageFont.truetype("arial.ttf", 20)
        # Get drawing context
        d = ImageDraw.Draw(img)
        # Create text
        text = f'"{body}" - \n {author}'
        # Draw multiline text
        d.multiline_text(
            (10, 10),
            text,
            font=fnt,
            fill=(255, 255, 255),
            stroke_width=1,
            stroke_fill=(0, 0, 0),
        )
        # Create out_path
        out_path = self.output_dir + '/img' + '.jpg'
        img.save(out_path)
        return out_path
