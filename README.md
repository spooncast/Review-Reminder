# Review-Reminder
## 개발 동기
팀원들과 1 on 1 미팅에서 팀원들이 한가지 애로 사항을 경험하고 있음을 알게 되었습니다.

* Code Freezing 날짜는 다가오는데, 올려둔 PR이 리뷰 & 승인되지 않아 Merge를 못하고 있음
* 최종 Freezing 당일에 팀원들에게 재촉하여 리뷰 승인을 받고 Merge 함

Code Freezing 날짜 별로 급한 순서대로 필요한 PR이 먼저 리뷰되면 좋겠다는 생각이 들었습니다.

## 동작

평일 오전 8시 즈음 Github Action Workflow가 자동으로 동작합니다.

Repository 내 `open` 상태의 PR 목록을 조회하여 리뷰 승인이 필요한 PR들에 대해 `마감 기한`이 급한 순서로 슬랙 채널에 알려줍니다.

예시:
![image](https://user-images.githubusercontent.com/96655366/225930793-0fedcceb-ca1d-4f82-a034-475259bfac5b.png)

이를 바탕으로 각 팀원들은 기한이 많이 남아있는 PR들을 리뷰하느라 마감이 임박한 PR을 지나치는 일을 방지할 수 있으며, 오늘까지 리뷰 & Merge 되어야 하는 PR을 팀원들에게 매번 재촉하지 않아도 됩니다.

각 팀 Repository에 적용하기 위한 usage guide는 [이곳](https://github.com/spooncast/Review-Reminder/wiki)에서 확인 가능합니다.

## 제약 사항

Bitbucket Cloud Repository에 한하여 동작합니다.
Github 및 그외 Repository에는 해당하지 않습니다.
