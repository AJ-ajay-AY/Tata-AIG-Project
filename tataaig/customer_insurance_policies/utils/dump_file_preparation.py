import sys
import pandas as pd
from django.conf import settings
from datetime import datetime

class DumpFilePrepUtilities():

    @staticmethod
    def data_creation_for_pandas(list_of_dict, column_names):
        try:
            data_list_of_tuples = [(policy['user__first_name'] ,policy['user_id'], policy['policy_id'],  policy['policy__name'], policy['policy_number'], datetime.strftime(policy['start_date_time'], "%d %B, %Y"), datetime.strftime(policy['expiry_date_time'],"%d %B, %Y")) for policy in list_of_dict]
            if (len(data_list_of_tuples[0])==len(column_names)) and len(data_list_of_tuples):
                data_frame_result = DumpFilePrepUtilities._data_frame_generator(data_list_of_tuples, column_names)
                return data_frame_result, True, "Success"
            else:
                return {}, False, "Column count Not matching with Data"
        except Exception as e:
            print("data_creation_for_pandas() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            return {}, False, "Error"

    @staticmethod
    def _data_frame_generator(data_list_of_tuples, column_names):
        data_frame = pd.DataFrame(data_list_of_tuples, columns=column_names)
        return data_frame

    @staticmethod
    def excel_file_obj_creation(data_frame , filename, extension, column_cells=False, column_width=False):
        try:
            file_name = "{}.{}".format(settings.BASE_DIR + '/media/' + filename, extension)
            if extension == 'xlsx':
                writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
                data_frame.to_excel(writer, index=False, startrow=0, sheet_name=filename)
                worksheet = writer.sheets[filename]
                if column_cells and column_width:
                    for cell in column_cells:
                        worksheet.set_column(cell, column_width)
                    writer.save()
            elif extension == 'json':
                data_frame.to_json(file_name)
            elif extension == 'csv':
                data_frame.to_csv(file_name)
            return file_name
        except Exception as e:
            print("excel_file_obj_creation() line number of error is {}".format(sys.exc_info()[-1].tb_lineno), e)
            return None




