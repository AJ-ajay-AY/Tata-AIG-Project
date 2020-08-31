from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    profession = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    language = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'user'

class PolicyCategory(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'policy_category'

class Policy(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    policy_product_code = models.CharField(max_length=10, blank=True, null=True, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    policy_category = models.ForeignKey("PolicyCategory", related_name='policy_id', on_delete=models.CASCADE,
                                         null=True, blank=True)
    tnc = models.CharField(max_length=500, blank=True, null=True)
    coverage_years = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.policy_product_code}"
    
    class Meta:
        db_table = 'policy'

class UserPolicy(models.Model):
    user = models.ForeignKey("User", related_name='user_id', on_delete=models.CASCADE,
                             null=True, blank=True)
    policy = models.ForeignKey("Policy", related_name='policy_id', on_delete=models.CASCADE,
                               null=True, blank=True)
    policy_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
    amount_insured = models.IntegerField()
    start_date_time = models.DateTimeField(null=True, blank=True) 
    expiry_date_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.policy_number

    class Meta:
        db_table = 'user_policy'
    
    





