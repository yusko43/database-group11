# Generated by Django 2.0.5 on 2018-05-12 08:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('account_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('player_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('account_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('match_date', models.DateField()),
                ('referee', models.CharField(max_length=20)),
                ('score', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('offer_type', models.BooleanField()),
                ('offer_amount', models.IntegerField(default=0)),
                ('contract_start', models.DateField()),
                ('contract_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ParticipatesIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('account_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('kit_no', models.IntegerField(default=0)),
                ('pref_foot', models.BooleanField(default=True)),
                ('prev_transfer_fee', models.IntegerField(default=0)),
                ('recovery_date', models.DateField(blank=True, null=True)),
                ('suspend_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaysIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=20)),
                ('contract_start', models.DateField()),
                ('contract_end', models.DateField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Player')),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('account_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProposeOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Offer')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Player')),
                ('president_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.President')),
            ],
        ),
        migrations.CreateModel(
            name='ProposeTrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Player')),
                ('president_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.President')),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=20)),
                ('capacity', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Match')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=20)),
                ('league_place', models.IntegerField(default=0)),
                ('budget', models.IntegerField(default=0)),
                ('establishment_date', models.DateField()),
                ('stadium_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Stadium')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('trade_id', models.IntegerField(primary_key=True, serialize=False)),
                ('trade_amount', models.IntegerField(default=0)),
                ('time_limit', models.DateField()),
                ('no_players', models.IntegerField(default=0)),
                ('deciding_president', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.President')),
            ],
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 12, 11, 54, 36, 449584)),
        ),
        migrations.AddField(
            model_name='statistics',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Team'),
        ),
        migrations.AddField(
            model_name='proposetrade',
            name='trade_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Trade'),
        ),
        migrations.AddField(
            model_name='president',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Team'),
        ),
        migrations.AddField(
            model_name='playsin',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='belong_to_team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Team'),
        ),
        migrations.AddField(
            model_name='participatesin',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Player'),
        ),
        migrations.AddField(
            model_name='offer',
            name='deciding_president',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.President'),
        ),
        migrations.AddField(
            model_name='match',
            name='guest_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_team', to='posts.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='posts.Team'),
        ),
        migrations.AddField(
            model_name='coach',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Team'),
        ),
        migrations.AddField(
            model_name='agent',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Player'),
        ),
    ]
