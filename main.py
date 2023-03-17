import os
import re
from datetime import datetime
from datetime import date
import sys
from repo.bitbucket_repo import getPullRequest, getPullRequests
from repo.slack_repo import sendSlackMessage


def is_unapproved_pr(prDetails):
    min_approval_count = int(os.environ.get('MINIMUM_APPROVAL_COUNT'))
    approval_count = 0
    participants = prDetails['participants']
    for participant in participants:
        if participant['approved'] == True:
            approval_count += 1
            if approval_count >= min_approval_count:
                return False

    return True


def get_remain_day(text):
    regex = r"Due date: (\d{4}-\d{2}-\d{2})"
    match = re.search(regex, text)
    if match:
        due_date_str = match.group(1)
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        return abs(date.today() - due_date.date()).days
    else:
        return sys.maxsize


def get_slack_message(pr):
    remain_day_text = ""
    if pr['remain_day'] <= 0:
        remain_day_text = "당장 리뷰해주세요!"
    elif pr['remain_day'] == sys.maxsize:
        remain_day_text = ""
    else:
        remain_day_text = str(pr['remain_day']) + "일 내에 리뷰해주세요"
    return f" - <{pr['links']['html']['href']}|{pr['title']}>\t{remain_day_text}"

pr_list = getPullRequests()
unapproved_pr_list = []

for pr in pr_list:
    prDetails = getPullRequest(pr['id'])

    if is_unapproved_pr(prDetails):
        remain_day = get_remain_day(prDetails['description'])
        prDetails['remain_day'] = remain_day
        unapproved_pr_list.append(prDetails)

sorted_pr_list = sorted(unapproved_pr_list, key=lambda x: x['remain_day'])
message = '\n'.join([get_slack_message(pr) for pr in sorted_pr_list])
sendSlackMessage("코드 리뷰가 필요한 PR 목록\n" + message)
