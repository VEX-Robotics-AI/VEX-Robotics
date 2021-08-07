"""
https://bit.ly/S4V_CS201_Stack
https://www.robotmesh.com/studio/60f24c87c4b0580fb15d4e5e
"""


cau = ["Dao", "Trong", "Su", "Ton"]

stack = []
print(stack)

for chu in cau:
    stack.append(chu)   # them mot phan tu vao cuoi danh sach/ cuoi stack
print('---------')
print(stack)

print('---------')
for i in range(len(stack)):
    chu = stack.pop()
    print(chu)

print('---------')
print(stack)
