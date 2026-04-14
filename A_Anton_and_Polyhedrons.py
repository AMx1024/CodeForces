faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

t = int(input())
sum = 0

for _ in range(t):
    shape = input()
    sum += faces[shape]

print(sum)