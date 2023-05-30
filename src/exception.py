import sys 

def error_messeage_detail(error,error_detail:sys):
    _,_,exc_tb  =error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_messeage = f"Error occured in python script name {file_name} line number {exc_tb.tb_lineno} error messeage {str(error)}"
    return error_messeage

class CustomException(Exception):
    def __init__(self,error_messeage,error_detail:sys):
        super().__init__(error_messeage)
        self.error_messeage = error_messeage_detail(error_messeage,error_detail=error_detail)
    
    def __str__(self):
        return self.error_messeage