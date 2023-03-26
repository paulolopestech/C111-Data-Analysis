name = str(input('Digite o nome do aluno: '))
average = float(input('Digite a média do aluno: '))

studentData = {}

studentData['name'] = name
studentData['average'] = average

if studentData['average'] >= 60:
    studentData['status'] = 'AP'
else:
    studentData['status'] = 'RP'

print('STATUS DO ALUNO: ', studentData['status'])
print(studentData)    