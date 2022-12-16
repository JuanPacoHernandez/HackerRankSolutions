
def angryProfessor(k, a):
    students_arrived_on_time = 0
    for i in a:
        if i <= 0:
            students_arrived_on_time += 1
    if students_arrived_on_time >= k:
        print('NO')
        return
    else:
        print('YES')
        return
k = 3
a=[-1,-3,4,2]
angryProfessor(k,a)
k = 2
a=[0,-1,2,1]
angryProfessor(k,a)


