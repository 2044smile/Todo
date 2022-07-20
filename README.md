# TodoList

## Plan

Frontend Vue.js </br>
Backend Django  </br>

### 현재 확인사항(문제점 발견)
#### 백엔드
백엔드에서 Todo Model List를 생성하면 프론트엔드에서는 확인 불가

#### 프론트엔드
프론트엔드에서 Todo를 만들면 관련 글은 백엔드 데이터베이스(sqlite)에 저장 완료

ㄴ 프론트엔드에서 TODO를 만들면 관련 글이 프론트에서 보이지가 않음



## Todo Model

- title (CharField 64)
- description (CharField 256)
- author (Account Foreign and CharField 16)
- due_date (DateField)
- completed (BooleanField default False)

## Account Model

- email(Email Authentication) ()
- username(Default email address (nickname)@)
- is_superuser
- is_staff
- is_active(ban user is_active=False)
- date_joined
- account_emailaddress

TODO(Think): Avatar? Profile(point, activity log) Model?
