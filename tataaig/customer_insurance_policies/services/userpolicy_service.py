from customer_insurance_policies.models import UserPolicy
from customer_insurance_policies.dao import UserPolicyDao
import sys
from customer_insurance_policies.utils.dump_file_preparation import DumpFilePrepUtilities

class UserPolicyService():

    def user_policy_list(self, user_id):
        values_list= ['user_id' ,'policy_id', 'policy__name' , 'policy_number', 'start_date_time', 'expiry_date_time']
        userpolicy_list_dict = UserPolicyDao.get_userpolicy_values_by_filterdict(self, {'user_id':user_id}, values_list)
        return userpolicy_list_dict

    def user_policy_dump(self, user_id, format_name):
        try:
            columns = ['User Name','User id', 'Policy id', 'Policy Name', 'Policy Number', 'Start of Policy', 'Expiry of Policy']
            width_adjust_cells = ['C:C', 'D:D', 'E:E', 'F:F']
            values_list= ['user__first_name' ,'user_id' ,'policy_id', 'policy__name' , 'policy_number', 'start_date_time', 'expiry_date_time']
            userpolicy_list_dict = UserPolicyDao.get_userpolicy_values_by_filterdict(self, {'user_id':user_id}, values_list)
            file_name = f"UserPolicies-{userpolicy_list_dict[0]['user_id']}-{userpolicy_list_dict[0]['user__first_name']}"
            data_frame_result, result, message = DumpFilePrepUtilities.data_creation_for_pandas(userpolicy_list_dict, columns)
            if result:
                if format_name == 'xlsx':
                    file_name_obj = DumpFilePrepUtilities.excel_file_obj_creation(data_frame_result, file_name, format_name, width_adjust_cells, 25)
                elif format_name == 'json':
                    file_name_obj = DumpFilePrepUtilities.excel_file_obj_creation(data_frame_result, file_name, format_name)
                elif format_name == 'csv':
                    file_name_obj = DumpFilePrepUtilities.excel_file_obj_creation(data_frame_result, file_name, format_name)
                return file_name_obj,result,message
            else:
                return False, result, message
        except Exception as e:
            print("user_policy_dump() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            return False


        