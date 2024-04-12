import sys
import PIL

raw_data:bytes
out = []

in_file = sys.argv[1]
out_file = sys.argv[2]
gif_name = sys.argv[3]


with open(in_file, "rb") as f:
    raw_data=f.read()


for i, b in enumerate(raw_data):
    out.append(hex(b))


with open(out_file, "w") as f:
    f.write(f"const uint8_t {gif_name}[] PROGMEM = {{ \n")

    for i in range(0, len(out), 8):

        # Join 8 strings with a space separator
        line = ', '.join(out[i:i+8]).strip(", ")+ ",\n"
        # Write the line to the file
        f.write(line)

    f.write("};")