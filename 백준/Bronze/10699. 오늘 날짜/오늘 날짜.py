from datetime import datetime, timedelta

# 현재 UTC 시간 가져오기
utc_now = datetime.utcnow()

# UTC+9 (KST)로 변환
kst_now = utc_now + timedelta(hours=9)

# YYYY-MM-DD 형식으로 출력
print(kst_now.strftime('%Y-%m-%d'))
