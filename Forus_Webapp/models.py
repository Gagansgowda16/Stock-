from django.db import models

class register(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	phno=models.CharField(max_length=60)
	
class register1(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	phno=models.CharField(max_length=60)
	
class empreg1(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	rpassword=models.CharField(max_length=60)
	dob=models.CharField(max_length=60)
	gender=models.CharField(max_length=60)
	phno=models.CharField(max_length=60)

class stockbin(models.Model):
	ERP_NO=models.CharField(max_length=60)
	MP_NO=models.CharField(max_length=60)
	store=models.CharField(max_length=60)
	device=models.CharField(max_length=60)
	rack=models.CharField(max_length=60)
	shelf=models.CharField(max_length=60,default=1)
	bin_card=models.CharField(max_length=60)
	date=models.CharField(max_length=60)
	pb=models.CharField(max_length=60)
	desc=models.CharField(max_length=60)
	no_received=models.CharField(max_length=60)
	no_issue=models.CharField(max_length=60)
	sb=models.CharField(max_length=60)
	sv=models.CharField(max_length=60)
	rdno=models.CharField(max_length=60,default=1)
	remarks=models.CharField(max_length=60)

class store_room(models.Model):
	str=models.CharField(max_length=60)
	rkr=models.CharField(max_length=60)
	devr1=models.CharField(max_length=60)
	shelf=models.CharField(max_length=60,default='shelf1')
	binr=models.CharField(max_length=60)


class additem(models.Model):
	name=models.CharField(max_length=60)
	total=models.CharField(max_length=60)
	pd=models.CharField(max_length=60,default=1)
	Rece=models.CharField(max_length=60,default=1)
	Iss=models.CharField(max_length=60,default=1)
	cd=models.CharField(max_length=60,default=1)
	db=models.CharField(max_length=60,default=1)
	rm1=models.CharField(max_length=60,default=1)

class deviceitem(models.Model):
	device_id=models.CharField(max_length=60,default=1)
	name=models.CharField(max_length=60)
	Previous_Date=models.CharField(max_length=60,default=1)
	Previous_Balance=models.CharField(max_length=60,default=1)
	Received=models.CharField(max_length=60,default=1)
	Issued=models.CharField(max_length=60,default=1)
	Current_Date=models.CharField(max_length=60,default=1)
	Device_Balance=models.CharField(max_length=60,default=1)
	Remarks=models.CharField(max_length=60,default=1)

	