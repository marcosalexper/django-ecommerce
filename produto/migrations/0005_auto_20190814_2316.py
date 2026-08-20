from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_auto_20190814_0700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
    ]