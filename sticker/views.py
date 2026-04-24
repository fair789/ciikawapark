from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from datetime import date

from .models import StickerRecord, GoalSetting


def _get_comment(progress_rate):
    if progress_rate >= 100:
        return "討伐完了ッ！！やったーーッ！！🎉"
    elif progress_rate >= 90:
        return "すごいッ！！あとちょっとだよッ！"
    elif progress_rate >= 60:
        return "折り返しッ！！ここからだよッ！"
    elif progress_rate >= 30:
        return "いい感じッ！もっとがんばるッ！"
    else:
        return "さあはじめるよッ！みんなでがんばるッ！"


def dashboard(request):
    today = date.today()

    if request.method == 'POST':
        cast_name = request.POST.get('cast_name', '').strip()
        count_str = request.POST.get('count', '')
        try:
            count = int(count_str)
            if count < 1:
                raise ValueError
        except (ValueError, TypeError):
            messages.error(request, '枚数は1以上の数字を入力してねッ！')
            return redirect('dashboard')

        StickerRecord.objects.create(
            date=today,
            count=count,
            cast_name=cast_name,
        )
        name_label = cast_name if cast_name else 'キャスト'
        messages.success(request, f'{name_label} が {count}枚 配布報告したよッ！ありがとうッ！')
        return redirect('dashboard')

    goal_obj = GoalSetting.objects.first()
    goal_total = goal_obj.target_count if goal_obj else 3000

    today_count = (
        StickerRecord.objects.filter(date=today)
        .aggregate(total=Sum('count'))['total'] or 0
    )
    cumulative_total = (
        StickerRecord.objects.filter(date__year=today.year, date__month=today.month)
        .aggregate(total=Sum('count'))['total'] or 0
    )
    progress_rate = min(int(cumulative_total / goal_total * 100), 100)

    ranking_qs = (
        StickerRecord.objects.filter(date__year=today.year, date__month=today.month)
        .exclude(cast_name='')
        .values('cast_name')
        .annotate(total=Sum('count'))
        .order_by('-total')[:5]
    )
    medals = ['🥇', '🥈', '🥉', '4位', '5位']
    ranking = [
        {'medal': medals[i], 'name': r['cast_name'], 'total': r['total']}
        for i, r in enumerate(ranking_qs)
    ]

    recent_records = StickerRecord.objects.order_by('-id')[:5]

    return render(request, 'sticker/dashboard.html', {
        'goal_total': goal_total,
        'today_count': today_count,
        'cumulative_total': cumulative_total,
        'progress_rate': progress_rate,
        'comment': _get_comment(progress_rate),
        'ranking': ranking,
        'recent_records': recent_records,
        'today': today,
    })
