from flask import render_template, request, session
from classes.bank import Bank
from classes.branch import Branch
from classes.card import Card
from classes.customer import Customer
from classes.transaction import Transaction
from classes.userlogin import Userlogin

prev_option = ""

def obj_to_dict(obj, att):
    """Converte um objeto Python num dicionário para o template."""
    d = {}
    for a in att:
        d[a] = getattr(obj, a)
    return d

def apps_gform(cname=''):
    global prev_option
    ulogin = session.get("user")
    if ulogin is not None:
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            strobj = request.form[cl.att[0]]
            for i in range(1, len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            for i in range(1, len(cl.att)):
                setattr(obj, cl.att[i], request.form[cl.att[i]])
            cl.update(getattr(obj, cl.att[0]))
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                cl.remove(getattr(obj, cl.att[0]))
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj_dict = {cl.att[0]: 0}
            for i in range(1, len(cl.att)):
                obj_dict[cl.att[i]] = ""
        else:
            obj_dict = obj_to_dict(obj, cl.att)
        return render_template("gform.html", butshow=butshow, butedit=butedit,
                               cname=cname, obj=obj_dict, att=cl.att, des=cl.des,
                               ulogin=session.get("user"))
    else:
        return render_template("index.html", ulogin=ulogin)
