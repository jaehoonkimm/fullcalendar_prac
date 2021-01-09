from django.shortcuts import render
from .models import CalendarEvent
import datetime
from django.utils import timezone


def home(request):
    events = CalendarEvent.objects.all()
    events_todo = []
    events_subject = []

    for i in events:
        # django의 datetime은 2019-01-01 00:00:00.000000. 날짜는 index 0-9까지만 필요!
        today_date = str(timezone.localtime())[0:10].replace("-", "")
        today = int(today_date)

        start_date = str(i.start)[0:10].replace("-", "")
        start_day = int(start_date)

        end_date = str(i.end)[0:10].replace("-", "")
        end_day = int(end_date)

        # 오늘 일정 갯수를 지정하는 조건문
        if today >= start_day:
            if today <= end_day:
                if i.groupId == "todo":
                    events_todo.append(str(i.title))
                elif i.groupId == "subject":
                    events_subject.append(str(i.title))
        # 일정이 존재하는지 안하는지를 배열의 길이로 확인 할 거예요!
        length_todo = len(events_todo)
        length_subject = len(events_subject)
        # main에 문구를 출력하기 위한 변수
        message_todo = ""
        message_subject = ""

        for i in range(length_todo):
            if i == 0:
                message_todo += str(events_todo[i])
            elif i > 0:
                message_todo += str("," + events_todo[i])
        for i in range(length_subject):
            if i == 0:
                message_subject += str(events_subject[i])
            elif i > 0:
                message_subject += str("," + events_subject[i])
    return render(
        request,
        "main.html",
        {
            "events": events,
            "message_todo": message_todo,
            "message_subject": message_subject,
            "length_todo": length_todo,
            "length_subject": length_subject,
        },
    )