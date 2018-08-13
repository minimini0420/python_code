import json
# jsonResult=[{'name': '윤성우', 'age': '28', 'address': '달서구', 'past_record': '1', 'student_ID': 'ITT001'}]
jsonResult=[{'name': '윤성우', 'age': '28'}]
with open('ITT_Student.json', 'w',encoding='UTF8') as outfile:
    readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(str(readable_result))
    print("프로그램을 종료합니다.")