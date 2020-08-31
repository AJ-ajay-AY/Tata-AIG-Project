from customer_insurance_policies.models import Policy
import sys

class PolicyDao():

    def get_policy_values_by_filterdict(self, filterdict, valueslist):
        try:
            if len(filterdict) and len(valueslist):
                policy_dao_dict = list(Policy.objects.filter(**filterdict).values(*valueslist))
            elif len(valueslist):
                policy_dao_dict = list(Policy.objects.all().values(*valueslist))
            return policy_dao_dict
        
        except Exception as e:
            print("get_policy_values_by_filterdict() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            return None