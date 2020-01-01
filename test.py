from pathlib import Path

base_dir = Path(__file__).parent
image_dir = Path.joinpath(base_dir, 'image')


if not Path.exists(image_dir):
    Path.mkdir(image_dir)