from customer_insurance_policies.models import UserPolicy
import sys

class UserPolicyDao():

    def get_userpolicy_values_by_filterdict(self, filterdict, valueslist):
        try:
            if len(filterdict) and len(valueslist):
                userpolicy_dao_dict = list(UserPolicy.objects.filter(**filterdict).values(*valueslist))
            elif len(valueslist):
                userpolicy_dao_dict = list(UserPolicy.objects.all().values(*valueslist))
            return userpolicy_dao_dict
        
        except Exception as e:
            print("get_userpolicy_values_by_filterdict() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            return None