# 🚀 내부 배포 가이드 (관리자용)

## 1. GitHub 업로드 및 공유

### GitHub 저장소 생성
```bash
# 1. GitHub에서 새 저장소 생성
# Repository name: reseller-analyzer
# Private 선택 (내부용)

# 2. 로컬에서 푸시
git init
git add .
git commit -m "리셀러 분석 시스템 v1.0"
git remote add origin https://github.com/[your-username]/reseller-analyzer.git
git push -u origin main
```

### 팀 멤버 초대
1. Settings → Manage access → Invite a collaborator
2. 팀 멤버 이메일 입력

---

## 2. Google Colab 직접 링크 생성

### 방법 A: GitHub 연동
```
https://colab.research.google.com/github/[your-username]/reseller-analyzer/blob/main/reseller_analyzer_colab.ipynb
```

### 방법 B: Google Drive 공유
1. Google Drive에 notebook 업로드
2. 우클릭 → 연결 앱 → Google Colaboratory
3. 공유 → 링크 받기 → "링크가 있는 모든 사용자"
4. 생성된 링크 팀에 공유

---

## 3. 원클릭 실행 버튼 만들기

### README.md에 추가
```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/[your-username]/reseller-analyzer/blob/main/reseller_analyzer_colab.ipynb)
```

### 내부 위키/노션에 추가
```html
<a href="https://colab.research.google.com/github/[your-username]/reseller-analyzer/blob/main/reseller_analyzer_colab.ipynb" target="_blank">
  <button style="background-color: #FF6F00; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer;">
    🚀 리셀러 분석 시작하기
  </button>
</a>
```

---

## 4. 자동화 옵션 (고급)

### Google Apps Script 연동
```javascript
function analyzeResellers() {
  // Google Sheets에서 직접 실행
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var data = sheet.getDataRange().getValues();

  // Colab API 호출 (설정 필요)
  var response = UrlFetchApp.fetch('YOUR_COLAB_API_ENDPOINT', {
    'method': 'post',
    'payload': JSON.stringify(data)
  });

  // 결과 시트에 추가
  var result = JSON.parse(response.getContentText());
  // ... 결과 처리
}
```

### 정기 실행 설정
1. Google Sheets → 확장프로그램 → Apps Script
2. 트리거 추가 → 시간 기반 → 매주/매월
3. 자동 리포트 이메일 발송

---

## 5. 버전 관리

### 업데이트 절차
1. `reseller_analyzer_colab.ipynb` 수정
2. 버전 번호 업데이트 (첫 셀에 명시)
3. GitHub push
4. 팀 공지

### 버전 히스토리
```
v1.0 (2025.01) - 초기 버전
  - 5가지 지표 기반 리셀러 점수
  - 엑셀 리포트 생성
  - Google Colab 지원
```

---

## 6. 보안 고려사항

### 데이터 보호
- Colab 세션은 90분 후 자동 삭제
- 업로드 파일은 세션 종료시 삭제
- 결과 파일만 로컬 다운로드

### 접근 제어
- GitHub Private 저장소 사용
- Google Drive 공유 링크는 조직 내부만
- 정기적 접근 권한 검토

---

## 7. 사용자 교육

### 초기 교육 (5분)
1. Colab 링크 북마크
2. 파일 업로드 방법
3. 결과 해석 방법

### 문서 제공
- `colab_usage_guide.md` - 사용자용
- `README.md` - 일반 설명
- 이 문서 - 관리자용

---

## 8. 문제 해결

### 자주 발생하는 문제
1. **파일 업로드 안됨**: 브라우저 팝업 차단 해제
2. **실행 중단**: 런타임 재시작 후 재실행
3. **한글 깨짐**: UTF-8 인코딩 확인

### 지원 체계
1. 1차: 사용 가이드 참조
2. 2차: 팀 채널 문의
3. 3차: 관리자 직접 지원

---

**담당자**: [이름]
**최종 업데이트**: 2025년 1월
**다음 검토**: 2025년 4월