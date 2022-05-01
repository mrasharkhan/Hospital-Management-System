# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime,date


class Administrator(models.Model):
    a_id = models.CharField(db_column='A_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    a_password = models.CharField(db_column='A_password', max_length=45)  # Field name made lowercase.
    a_cnic = models.CharField(db_column='A_cnic', max_length=14)  # Field name made lowercase.
    a_name = models.CharField(db_column='A_name', max_length=45)  # Field name made lowercase.
    a_salary = models.IntegerField(db_column='A_salary')  # Field name made lowercase.
    a_age = models.IntegerField(db_column='A_age')  # Field name made lowercase.
    a_sex = models.CharField(db_column='A_sex', max_length=10)  # Field name made lowercase.
    a_address = models.CharField(db_column='A_address', max_length=45)  # Field name made lowercase.
    a_email = models.CharField(db_column='A_email', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrator'

    def __str__(self):
        return self.a_id
    
    empAuth_objects= models.Manager()


class AdmissionDetails(models.Model):
    data_admitted = models.DateTimeField()
    date_discharge = models.DateTimeField()
    p = models.OneToOneField('Patient', models.DO_NOTHING, db_column='P_Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admission_details'


class Appointment(models.Model):
    a_date = models.CharField(db_column='A_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    a_time = models.CharField(db_column='A_Time', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p = models.ForeignKey('Patient', models.DO_NOTHING, db_column='P_Id')  # Field name made lowercase.
    d = models.ForeignKey('Doctor', models.DO_NOTHING, db_column='D_Id')  # Field name made lowercase.
    p_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'appointment'
    
    empAuth_objects= models.Manager()


class Department(models.Model):
    dept_id = models.CharField(db_column='Dept_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    dept_name = models.CharField(db_column='Dept_name', max_length=45)  # Field name made lowercase.
    d = models.ForeignKey('Doctor', models.DO_NOTHING, db_column='D_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'
    def __str__(self):
        return self.dept_id
    
    empAuth_objects= models.Manager()


class Doctor(models.Model):
    d_id = models.CharField(db_column='D_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    d_password = models.CharField(db_column='D_password', max_length=45)  # Field name made lowercase.
    d_cnic = models.CharField(db_column='D_cnic', max_length=14)  # Field name made lowercase.
    d_address = models.CharField(db_column='D_address', max_length=45)  # Field name made lowercase.
    d_name = models.CharField(db_column='D_name', max_length=45)  # Field name made lowercase.
    d_salary = models.IntegerField(db_column='D_salary')  # Field name made lowercase.
    d_age = models.IntegerField(db_column='D_age')  # Field name made lowercase.
    d_sex = models.CharField(db_column='D_sex', max_length=5)  # Field name made lowercase.
    d_senioritylevel = models.CharField(db_column='D_senioritylevel', max_length=10)  # Field name made lowercase.
    d_email = models.CharField(db_column='D_email', max_length=45)  # Field name made lowercase.
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctor'
    
    def __str__(self):
        return self.d_id
    
    empAuth_objects= models.Manager()


class LabTechnician(models.Model):
    l_id = models.CharField(db_column='L_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    l_password = models.CharField(db_column='L_password', max_length=45)  # Field name made lowercase.
    l_cnic = models.CharField(db_column='L_cnic', max_length=14)  # Field name made lowercase.
    l_address = models.CharField(db_column='L_address', max_length=100)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_name', max_length=45)  # Field name made lowercase.
    l_salary = models.IntegerField(db_column='L_salary')  # Field name made lowercase.
    l_age = models.IntegerField(db_column='L_age')  # Field name made lowercase.
    l_sex = models.CharField(db_column='L_sex', max_length=10)  # Field name made lowercase.
    l_senioritylevel = models.CharField(db_column='L_senioritylevel', max_length=45)  # Field name made lowercase.
    l_email = models.CharField(db_column='L_email', max_length=45)  # Field name made lowercase.
    lab = models.ForeignKey('Laboratories', models.DO_NOTHING, db_column='Lab_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lab_technician'
    def __str__(self):
        return self.l_id
    
    empAuth_objects= models.Manager()


class Laboratories(models.Model):
    lab_id = models.CharField(db_column='Lab_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    lab_name = models.CharField(db_column='Lab_name', max_length=45)  # Field name made lowercase.
    l = models.ForeignKey(LabTechnician, models.DO_NOTHING, db_column='L_Id', blank=True, null=True)  # Field name made lowercase.
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'laboratories'
    def __str__(self):
        return self.lab_id
    empAuth_objects= models.Manager()


class Nurses(models.Model):
    n_cnic = models.CharField(db_column='N_cnic', primary_key=True, max_length=14)  # Field name made lowercase.
    n_name = models.CharField(db_column='N_name', max_length=45)  # Field name made lowercase.
    n_sex = models.CharField(db_column='N_sex', max_length=10, blank=True, null=True)  # Field name made lowercase.
    n_age = models.IntegerField(db_column='N_age')  # Field name made lowercase.
    n_salary = models.IntegerField(db_column='N_salary')  # Field name made lowercase.
    n_address = models.CharField(db_column='N_address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    n_senioritylevel = models.CharField(db_column='N_senioritylevel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nurses'


class Patient(models.Model):
    p_id = models.CharField(db_column='P_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    p_password = models.CharField(db_column='P_password', max_length=45)  # Field name made lowercase.
    p_cnic = models.CharField(db_column='P_cnic', max_length=14)  # Field name made lowercase.
    p_age = models.CharField(db_column='P_age', max_length=45)  # Field name made lowercase.
    p_address = models.CharField(db_column='P_address', max_length=45)  # Field name made lowercase.
    p_sex = models.CharField(db_column='P_sex', max_length=45)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_name', max_length=45)  # Field name made lowercase.
    p_email = models.CharField(db_column='P_email', max_length=45)  # Field name made lowercase.
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'
    
    def __str__(self):
        return self.p_id
    
    empAuth_objects= models.Manager()

    



class Prescription(models.Model):
    tests = models.CharField(max_length=100, blank=True, null=True)
    medicine = models.CharField(max_length=45, blank=True, null=True)
    p = models.ForeignKey(Patient, models.DO_NOTHING, db_column='P_Id', blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription'
    empAuth_objects= models.Manager()


class Qualification(models.Model):
    degrees = models.CharField(max_length=45, blank=True, null=True)
    d = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='D_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qualification'
    empAuth_objects= models.Manager()


class Rooms(models.Model):
    room_id = models.CharField(db_column='room_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    room_type = models.CharField(max_length=45, blank=True, null=True)
    rate = models.IntegerField()
    n_cnic = models.ForeignKey(Nurses, models.DO_NOTHING, db_column='N_cnic', blank=True, null=True)  # Field name made lowercase.
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rooms'


class TestReports(models.Model):
    r_name = models.CharField(db_column='R_name', max_length=45)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_name', max_length=45)  # Field name made lowercase.
    t_name = models.CharField(db_column='T_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=45, blank=True, null=True)  # Field name made lowercase.
    r_date = models.DateTimeField(db_column='R_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_reports'
    
    empAuth_objects= models.Manager()
    


class Tests(models.Model):
    test_id = models.CharField(db_column='Test_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    test_name = models.CharField(db_column='Test_name', max_length=45)  # Field name made lowercase.
    test_price = models.IntegerField(db_column='Test_price')  # Field name made lowercase.
    lab = models.ForeignKey(Laboratories, models.DO_NOTHING, db_column='Lab_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tests'
    def __str__(self):
        return self.test_id
    
    empAuth_objects= models.Manager()

    
