from customer_insurance_policies.models import Policy
from customer_insurance_policies.dao import PolicyDao

class PolicyService():
    
    def policy_detail(self, policy_id):
        values_list =  ['id', 'name', 'policy_product_code' , 'description', 'policy_category__name', 'tnc', 'coverage_years']
        policy_detail_dict = PolicyDao.get_policy_values_by_filterdict(self, {'id' : policy_id}, values_list)
        return policy_detail_dict