import ttkbootstrap.validation as vd
class ValidationUtils:
    button_submit= None
    #get method directly
    @staticmethod
    def check_ID(entry,check_validation):
        @vd.validator
        def validate_ID(event: vd.ValidationEvent):
            if len(event.postchangetext) == 0:
                check_validation.set(False)
                ValidationUtils.button_submit.config(state='disabled')
                return False
            check_validation.set(True)
            ValidationUtils.button_submit.config(state='normal')
            return True
        
        vd.add_validation(entry, validate_ID)
