# 🚀 GitHub 공유를 위한 설정 가이드

## 사용자가 준비해야 할 것

### 1. 필수 프로그램 설치
```bash
# Python 3.8 이상 필요
python --version

# 필요한 패키지 설치
pip install pandas matplotlib openpyxl jupyter notebook
```

### 2. 엑셀 파일 준비
- 파일명: 아무거나 OK (코드에서 수정 가능)
- 필수 컬럼:
  - 고객명 (주문자명)
  - 주문수량
  - 총매출액 또는 결제금액
  - 주문일자
  - 상품명
  - 주소

### 3. 사용 방법

#### 방법 1: Jupyter Notebook (추천)
```bash
# 노트북 실행
jupyter notebook

# notebook.ipynb 파일 열기
# 첫 번째 셀에서 파일명과 컬럼명 수정
```

#### 방법 2: Google Colab (설치 없이 사용)
1. Google Colab 접속: https://colab.research.google.com
2. GitHub URL 입력: `github.com/[your-username]/[repo-name]`
3. notebook.ipynb 열기
4. 엑셀 파일 업로드
5. 실행

## 코드 수정 필요 부분

### 파일명 변경 (첫 번째 셀)
```python
# 기존
df_morning = pd.read_excel('erp_order_form.xlsx', sheet_name='오전')

# 수정 (본인 파일명으로)
df = pd.read_excel('your_file.xlsx')  # 시트가 1개면
```

### 컬럼명 변경
```python
# 본인 엑셀의 컬럼명으로 수정
customer_col = 'Customer Name'  # 고객명 컬럼
quantity_col = 'Quantity'       # 수량 컬럼
amount_col = 'Total Amount'     # 금액 컬럼
date_col = 'Order Date'         # 날짜 컬럼
product_col = 'Product'         # 제품명 컬럼
```

## 라이선스
MIT License - 자유롭게 사용 가능