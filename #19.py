def create_password_checker(min_uppercase,min_lowercase,min_punctuation,min_digits):
    def password_checker(psw):
        dct= {'lowercase':0,'uppercase':0,'punctuation':0,'digits':0}
        punctuation ='!@#$%^&*()_+=-.,'
        letters = 'abcdefghijklmnopqrsutvwxyz'
        digits= '1234567890'
        dct['digits'] = min_digits
        dct['lowercase'] = min_lowercase
        dct['uppercase'] = min_uppercase
        dct['punctuation'] = min_punctuation

        for i in psw:
            if i in letters:
                dct['lowercase'] -=1
            if i in letters.upper():
                dct['uppercase'] -=1
            if i in digits:
                dct['digits'] -=1
            if i in punctuation:
                dct['punctuation'] -=1
        tp = tuple()

        for i in dct.values():
            if i != 0:
                tp = (False,dct)
                return tp
            else:
                 tp = (True,dct)
                 return tp


    return password_checker

pc1 = create_password_checker(2,3,1,4)
print(pc1('Ab!1'))
print(pc1('ABcde!1234'))