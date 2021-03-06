# Generated by Django 2.2.17 on 2021-03-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0118_remove_problem_is_polygon_problem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problemdata',
            old_name='custom_cpp_checker',
            new_name='custom_checker',
        ),
        migrations.RemoveField(
            model_name='problemdata',
            name='custom_py_checker',
        ),
        migrations.AlterField(
            model_name='problemdata',
            name='checker',
            field=models.CharField(blank=True, choices=[('standard', 'Standard'), ('floats', 'Floats'), ('floatsabs', 'Floats (absolute)'), ('floatsrel', 'Floats (relative)'), ('identical', 'Byte identical'), ('linecount', 'Line-by-line'), ('bridged', 'Custom checker')], max_length=10, verbose_name='checker'),
        ),
        migrations.AlterField(
            model_name='problemtestcase',
            name='checker',
            field=models.CharField(blank=True, choices=[('standard', 'Standard'), ('floats', 'Floats'), ('floatsabs', 'Floats (absolute)'), ('floatsrel', 'Floats (relative)'), ('identical', 'Byte identical'), ('linecount', 'Line-by-line'), ('bridged', 'Custom checker')], max_length=10, verbose_name='checker'),
        ),
    ]
