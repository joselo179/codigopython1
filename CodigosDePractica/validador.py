#Ejemplo de un modulo personalizado

import re  # modulo default en python

def validate_email(email):
    if len(email) > 7 :
        return bool(re.match("^.+@(\[?)[a-zA-z0-9-.]+.([a-zA-z]{2,3}|[0-9]{1,3})(}?)$",email))



