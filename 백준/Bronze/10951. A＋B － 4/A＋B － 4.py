while True:
  try:    # 에러가 발생할 수 있는 가능성이 있는 문장을 작성
    a, b = map(int, input().split())
  except: # 에러 발생 시 실행시킬 문장 작성
    break
  print(a+b)