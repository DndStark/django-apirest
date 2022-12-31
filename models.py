# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    campaign_name = models.CharField(max_length=45)
    campaign_description = models.CharField(max_length=45, blank=True, null=True)
    campaign_start_date = models.DateField()
    campaign_finish_date = models.DateField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    location = models.ForeignKey('Location', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=45)
    category_description = models.CharField(max_length=100, blank=True, null=True)
    category_logo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Condition(models.Model):
    condition_id = models.AutoField(primary_key=True)
    condition_name = models.CharField(max_length=45)
    condition_description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'condition'


class ConditionList(models.Model):
    condition_list_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    condition = models.ForeignKey(Condition, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'condition_list'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Donation(models.Model):
    donation_id = models.PositiveIntegerField(primary_key=True)
    donation_name = models.CharField(max_length=45)
    donation_description = models.CharField(max_length=45, blank=True, null=True)
    donation_photo = models.CharField(max_length=150)
    user = models.ForeignKey('User', models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    detail = models.ForeignKey('DonationDetail', models.DO_NOTHING)
    campaign = models.ForeignKey(Campaign, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'donation'


class DonationDetail(models.Model):
    donation_detail_id = models.AutoField(primary_key=True)
    detail_expiration_state = models.CharField(max_length=45)
    detail_expiration_date = models.DateField(blank=True, null=True)
    detail_amount = models.SmallIntegerField()
    detail_observation = models.CharField(max_length=300, blank=True, null=True)
    detail_solidarity_points = models.IntegerField()
    detail_register_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'donation_detail'


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_detail = models.CharField(max_length=100, blank=True, null=True)
    location_latitude = models.CharField(max_length=45)
    location_longitude = models.CharField(max_length=45)
    location_reference = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'location'


class Person(models.Model):
    person_id = models.PositiveIntegerField(primary_key=True)
    person_name = models.CharField(max_length=45, blank=True, null=True)
    person_document = models.CharField(unique=True, max_length=11, blank=True, null=True)
    person_address = models.CharField(max_length=45, blank=True, null=True)
    person_photo = models.CharField(max_length=45, blank=True, null=True)
    person_phone = models.CharField(unique=True, max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class Transport(models.Model):
    transport_id = models.AutoField(primary_key=True)
    transport_date = models.DateField(blank=True, null=True)
    transport_type = models.CharField(db_column='transport\x1f_type', max_length=1)  # Field renamed to remove unsuitable characters.
    transport_origin = models.ForeignKey(Location, models.DO_NOTHING, db_column='transport_origin')
    transport_destiny = models.ForeignKey(Location, models.DO_NOTHING, db_column='transport_destiny')
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'transport'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=45)
    user_password = models.CharField(max_length=45)
    user_state = models.CharField(max_length=1, blank=True, null=True)
    person = models.ForeignKey(Person, models.DO_NOTHING)
    user_type = models.ForeignKey('UserType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user'


class UserType(models.Model):
    user_type_id = models.AutoField(primary_key=True)
    user_type_name = models.CharField(max_length=45)
    user_type_description = models.CharField(max_length=100, blank=True, null=True)
    user_type_state = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user_type'
