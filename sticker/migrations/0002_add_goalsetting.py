from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_count', models.PositiveIntegerField(default=3000, verbose_name='今月の目標枚数')),
            ],
            options={
                'verbose_name': '目標設定',
            },
        ),
    ]
