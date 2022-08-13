import sys

# print(sys.argv[0])
# print(sys.argv[1])

print(sys.argv)

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write(message)