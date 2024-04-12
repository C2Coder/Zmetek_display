import sys
from PIL import Image, ImageSequence

raw_data: bytes
out = []

in_file = sys.argv[1]
out_file = sys.argv[2]
gif_name = sys.argv[3]


def resize(frames):
    for frame in frames:
        f = frame.copy()
        # Determine the dimensions of the resized image
        width, height = f.size
        min_dim = min(width, height)
        new_size = (240, 240)

        # Calculate the crop region
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
        right = (width + min_dim) // 2
        bottom = (height + min_dim) // 2
        crop_region = (left, top, right, bottom)
        f = f.crop(crop_region)
        f = f.resize(new_size)
        yield f


im = Image.open(in_file)
frames = ImageSequence.Iterator(im)

frames = resize(frames)

om = next(frames)
om.info = im.info
om.save(f"edited_{in_file}", save_all=True, append_images=list(frames))

with open(f"edited_{in_file}", "rb") as f:
    raw_data = f.read()


for i, b in enumerate(raw_data):
    out.append(hex(b))


with open(out_file, "w") as f:
    f.write(f"const uint8_t {gif_name}[] PROGMEM = {{ \n")

    for i in range(0, len(out), 8):

        # Join 8 strings with a space separator
        line = ', '.join(out[i:i+8]).strip(", ") + ",\n"
        # Write the line to the file
        f.write(line)

    f.write("};")
