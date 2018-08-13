import re

def check_match(p,file_name):
    m = p.match(file_name)
    if m :
        print(m)

file_name_condidates = ['foo.bar','autoexec.bat','sendmail.cf']

p = re.compile(".*[.].*$")

print("첫번쨰 정규식 테스트: .*[.].*$")
for file_name in file_name_condidates:
    check_match(p,file_name)

# step2] 확장자가 bat 파일 제외
p = re.compile(".*[.][^b].*$")
print("\n두번째 정규식 테스트: //*[.][^b].*$")
for file_name in file_name_condidates:
    check_match(p,file_name)

# step3] 확장자가 bat 파일 제외 두번째 시도
p = re.compile(".*[.]([^b]..|.[^a].|..[^t])")
print("\n세번째 정규식 테스트: .*[.]([^b]..|.[^a].|..[^t])")
for file_name in file_name_condidates:
    check_match(p,file_name)

# step4] 확장자가 bat 파일 제외 세번째 시도
p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)")
print("\n네번째 정규식 테스트 :.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)")
for file_name in file_name_condidates:
    check_match(p,file_name)