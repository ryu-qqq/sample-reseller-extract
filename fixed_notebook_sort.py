# 동점자 처리를 위한 개선된 정렬 방식

# 기존 방식 (동점일 때 순서 불명확)
top_resellers = final_results.nlargest(10, '리셀러점수')

# 개선된 방식 (동점일 때 총매출액 → 주문횟수 → 이름순)
top_resellers = final_results.sort_values(
    ['리셀러점수', '총매출액', '주문횟수', '주문자명'],
    ascending=[False, False, False, True]
).head(10)

print("개선된 정렬 방식:")
print("1. 리셀러점수 (높은 순)")
print("2. 총매출액 (높은 순)")
print("3. 주문횟수 (높은 순)")
print("4. 고객명 (가나다순)")