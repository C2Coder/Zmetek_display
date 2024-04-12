
# 15 frames
# 88971 bytes


buffer = []

with open("file.txt", "r") as f:
    for line in f.readlines():
        for b in line.split(","):
            buffer.append(b)

print(len(buffer))