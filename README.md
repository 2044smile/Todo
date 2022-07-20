# TodoList

## Plan

Frontend Vue.js </br>
Backend Django  </br>
할만 할 콘텐츠가 있을까?

## Todo Model

- title (CharField 64)
- description (CharField 256)
- author (Account Foreign and CharField 16)
- due_date (DateField)
- completed (BooleanField default False)

## Account Model

- email(Email Authentication)
- username(Default email address (nickname)@)
- is_superuser
- is_staff
- is_active(ban user is_active=False)
- date_joined

TODO(Think): Avatar? Profile(point, activity log) Model?
