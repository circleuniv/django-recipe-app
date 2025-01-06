# Generated by Django 5.0.10 on 2025-01-05 02:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=255)),
                ('codename', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=150, unique=True)),
                ('first_name', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=150)),
                ('last_name', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=150)),
                ('email', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, db_collation='Chinese_Taiwan_Stroke_CI_AS', null=True)),
                ('object_repr', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField(db_collation='Chinese_Taiwan_Stroke_CI_AS')),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=100)),
                ('model', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=255)),
                ('name', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(db_collation='Chinese_Taiwan_Stroke_CI_AS', max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(db_collation='Chinese_Taiwan_Stroke_CI_AS')),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('meal', models.CharField(max_length=1000, unique=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('meal_type', models.CharField(choices=[('starters', 'Starters'), ('salads', 'Salads'), ('main_dishes', 'Main Dishes'), ('deserts', 'Deserts')], max_length=200)),
                ('status', models.IntegerField(choices=[(0, 'Unavailable'), (1, 'Available')], default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'menu_items',
            },
        ),
    ]