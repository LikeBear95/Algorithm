answer = 0
count = 0
points = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0,
          'D+': 1.5, 'D0': 1.0, 'F': 0.0, }
for i in range(20):
    lecture, point, grade = map(str, input().split())
    if grade == 'P':
        pass
    else:
        answer += float(point) * points[grade]
        count += float(point)

print(answer/count)
