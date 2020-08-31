from customer_insurance_policies.models import User
from customer_insurance_policies.dao import UserDao

class UserService():

    def user_list_service(self):
        user_list_dict = UserDao.get_user_values_by_filterdict(self, {},['id' , 'first_name', 'last_name', 'profession', 'email', 'mobile'])
        return user_list_dict
