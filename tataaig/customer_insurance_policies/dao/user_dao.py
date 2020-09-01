from customer_insurance_policies.models import User
import sys

class UserDao():
    """
    User DAO -> houses all the ORM queries for User retreival from Database
    """
    def get_user_values_by_filterdict(self, filterdict, valueslist):
        try:
            if len(filterdict) and len(valueslist):
                user_dao_dict = list(User.objects.filter(**filterdict).values(*valueslist))
            elif len(valueslist):
                user_dao_dict = list(User.objects.all().values(*valueslist))
            return user_dao_dict
        
        except Exception as e:
            print("get_user_values_by_filterdict() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            return None

        

        
