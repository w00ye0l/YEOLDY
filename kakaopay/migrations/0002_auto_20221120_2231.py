# Generated by Django 3.2.13 on 2022-11-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakaopay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderlistfinal',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='order_request',
            field=models.CharField(choices=[('부재 시 경비실에 맡겨주세요', '부재 시 경비실에 맡겨주세요'), ('부재 시 택배함에 넣어주세요', '부재 시 택배함에 넣어주세요'), ('부재 시 집 앞에 놔주세요', '부재 시 집 앞에 놔주세요'), ('배송 전 연락 바랍니다', '배송 전 연락 바랍니다'), ('파손의 위험이 있는 상품입니다. 주의해 주세요.', '파손의 위험이 있는 상품입니다. 주의해 주세요.')], max_length=50),
        ),
        migrations.AlterField(
            model_name='orderlistfinal',
            name='order_request',
            field=models.CharField(choices=[('부재 시 경비실에 맡겨주세요', '부재 시 경비실에 맡겨주세요'), ('부재 시 택배함에 넣어주세요', '부재 시 택배함에 넣어주세요'), ('부재 시 집 앞에 놔주세요', '부재 시 집 앞에 놔주세요'), ('배송 전 연락 바랍니다', '배송 전 연락 바랍니다'), ('파손의 위험이 있는 상품입니다. 주의해 주세요.', '파손의 위험이 있는 상품입니다. 주의해 주세요.')], max_length=50),
        ),
    ]
