# Generated by Django 5.1.1 on 2024-10-03 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientinfo', '0002_initial'),
        ('inventory', '0004_initial'),
        ('produits', '0001_initial'),
        ('tiers', '0002_initial'),
        ('user', '0001_initial'),
        ('ventes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FicheLivraisonExterne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('adresse', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('transporteur', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('modePaiement', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('montant', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('numeroColis', models.IntegerField(default=1)),
                ('note', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoyenTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immatriculation', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('designation', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_moyenstransport', to='clientinfo.store')),
            ],
        ),
        migrations.CreateModel(
            name='CourseLivraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('note', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('dateTimeAffectation', models.DateTimeField(blank=True, null=True)),
                ('dateTimeDebut', models.DateTimeField(blank=True, null=True)),
                ('dateTimeFin', models.DateTimeField(blank=True, null=True)),
                ('typeCourse', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('transporteur', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('montant', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('fraisTransport', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('montantrecupere', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('tempsCourse', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('etat', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('bonlivraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonL_course', to='ventes.bonsortie')),
                ('chauffeur', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_courses', to='user.customuser')),
                ('moyen_transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='logistique.moyentransport')),
            ],
        ),
        migrations.CreateModel(
            name='BonTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBon', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('chauffeur', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('date_depart', models.DateTimeField()),
                ('adresse_livraison', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('frais_Livraison', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('etat_livraison', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('bonlivraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonsL_transports', to='ventes.bonsortie')),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients_bonstransport', to='tiers.client')),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_bontransport', to='clientinfo.store')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_bonstransport', to='user.customuser')),
                ('moyen_transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistique.moyentransport')),
            ],
        ),
        migrations.CreateModel(
            name='PreparationStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBon', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('datePrep', models.DateTimeField()),
                ('bonEntry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonsE_preparation', to='inventory.bonentry')),
            ],
        ),
        migrations.CreateModel(
            name='ProduitsEnBonTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('livre', models.BooleanField(default=False)),
                ('BonNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits_en_bon_transport', to='logistique.bontransport')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mes_bons_transport', to='produits.product')),
            ],
        ),
        migrations.CreateModel(
            name='ReglementTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date', models.DateField()),
                ('bon_transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reglements_bontransport', to='logistique.bontransport')),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientinfo.store')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='requeteclientinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateReq', models.DateField(blank=True, null=True)),
                ('etat', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('modePaiement', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('note', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients_requetes', to='tiers.client')),
            ],
        ),
        migrations.CreateModel(
            name='BlsEnRequeteClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modePaiement', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('etat_livraison', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('note', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('bonlivraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonsL_requests', to='ventes.bonsortie')),
                ('requete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonsL_enreq', to='logistique.requeteclientinfo')),
            ],
        ),
    ]
