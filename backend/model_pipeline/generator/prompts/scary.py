import datetime
from PIL import Image
from model_pipeline.generator.design.image_manager import Image_Manager


class Scary():
    name = "Scary"
    description = "scary"

    def __init__(self):
        self.instruction = """
###
Message:React Navtive scares me more than any other library I've ever used.
Meme:{"subject":"React Native"}
###
Message:I can't imagine having to run a marathon
Meme:{"subject":"marathons"}
###
"""

    def create(self, meme_text):
        with Image.open(f"app/static/meme_pics/{self.name.lower()}.jpg").convert(
            "RGBA"
        ) as base:

            overlay_image = Image_Manager.add_text(
                base=base,
                text=meme_text["subject"],
                position=(425, 950),
                font_size=40,
                wrapped_width=15,
            )
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f"{date}.jpg"
                file_location = f"../generated_images/{image_name}"
                out.save(file_location)
                return image_name
