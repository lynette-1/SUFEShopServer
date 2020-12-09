# Generated by Django 3.1.3 on 2020-12-07 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserService', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('commodity_id', models.AutoField(primary_key=True, serialize=False)),
                ('commodity_name', models.CharField(max_length=50)),
                ('commodity_type', models.CharField(max_length=20)),
                ('commodity_picture', models.ImageField(upload_to=None)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('detail', models.TextField()),
                ('on_shelf_time', models.DateTimeField(auto_now_add=True)),
                ('if_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CommodityApplication',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('apply_time', models.DateTimeField(auto_now_add=True)),
                ('application_state', models.CharField(choices=[('TO_BE_REVIEWED', '待审核'), ('APPROVED', '审核通过'), ('REJECTED', '审核未通过')], max_length=20)),
                ('audit_time', models.DateTimeField(auto_now=True)),
                ('if_delete', models.BooleanField(default=False)),
                ('Commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommodityService.commodity')),
                ('auditor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='auditor', to='UserService.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applier', to='UserService.user')),
            ],
        ),
        migrations.CreateModel(
            name='BrowserHisory',
            fields=[
                ('browser_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('browse_time', models.DateTimeField(auto_now_add=True)),
                ('if_delete', models.BooleanField(default=False)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommodityService.commodity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserService.user')),
            ],
        ),
    ]
