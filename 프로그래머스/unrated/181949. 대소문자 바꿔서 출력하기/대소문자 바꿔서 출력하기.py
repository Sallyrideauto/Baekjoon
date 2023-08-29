# https://velog.io/@seoul788/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4python-%EB%8C%80%EC%86%8C%EB%AC%B8%EC%9E%90-%EB%B0%94%EA%BF%94%EC%84%9C-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0

str = input()

for i in str:
    if i.isupper() == True:
        print(i.lower(), end = '')
    else:
        print(i.upper(), end = '')