import sys
import os
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from customer_insurance_policies.services.user_service import UserService
from customer_insurance_policies.services.policy_service import PolicyService
from customer_insurance_policies.services.userpolicy_service import UserPolicyService
from customer_insurance_policies.utils.generic_error_responses import ErrorResponse

class UserListAPI(APIView):
    """
    Rest API View to handle User list routes to service user_list_service()
    Returns:- JSON response
    """
    def get(self, request):
        try:
            userjson = UserService.user_list_service(self)
            if userjson:
                return JsonResponse({"data":userjson, 'status':True}, safe=False, status=200)
            else:
                return ErrorResponse.json_500()
        except Exception as e:
            print("UserListAPI() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            return ErrorResponse.json_404()
    
class UserPolicyList(APIView):
    """
    Rest API View to handle Policy list for a user routes to service user_policy_list(), 
    Returns:- JSON response
    """
    def get(self, request, usr_id):
        try:
            userpolicy_json = UserPolicyService.user_policy_list(self, usr_id)
            if userpolicy_json:
                return JsonResponse({"data":userpolicy_json, 'status':True}, safe=False, status=200)
            else:
                return ErrorResponse.json_500()
        except Exception as e:
            print("UserPolicyList() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            return ErrorResponse.json_404()

class PolicyDetail(APIView):
    """
    Rest API View to handle Policy details for a Policy routes to service policy_detail(), 
    Returns:- JSON response
    """
    def get(self, request, policy_id):
        try:
            policy_detail_json = PolicyService.policy_detail(self, policy_id)
            if policy_detail_json:
                return JsonResponse({"data":policy_detail_json, 'status':True}, safe=False, status=200)
            else:
                return ErrorResponse.json_500()
        except Exception as e:
            print("PolicyDetail() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            return ErrorResponse.json_404()

class UserPolicyDump(APIView):
    """
    Rest API View to handle User Policy Dump (currently configured  for 3  formats  xlsx,csv and json with  minimal changes) routes to service user_policy_dump(), 
    Returns:- HTTP response
    """
    def get(self, request, usr_id, format_name):
        try:
            format_dict = {"xlsx":"application/xlsx", "json":"application/json", "csv":"text/csv"}
            if format_name in format_dict:
                file_obj_name, result, message = UserPolicyService.user_policy_dump(self, usr_id, format_name)
                if file_obj_name:
                    with open(file_obj_name, "rb") as file:
                        data = file.read()
                        response = HttpResponse(data, content_type=format_dict[format_name])
                        response['Content-Length'] = os.path.getsize(file_obj_name)
                        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_obj_name)
                        return response
                else:
                    return ErrorResponse.json_500(message=message)
            else:
                return ErrorResponse.json_500(message="500 - Got an illegal format please try csv,json or xlsx")
            return ErrorResponse.json_500()
        except Exception as e:
                print("UserPolicyDump() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
                return ErrorResponse.json_404()
