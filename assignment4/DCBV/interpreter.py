import logging


logger = logging.getLogger("interpreter")

# Implement valuation functions and auxiliary functions.

def with_value(c,env) :
    if (type(c) ==  int) | (type(c) == bool) | (type(c) == tuple) : return c
    elif (type(c) == 'function') | (type(c) == 'list'): return val_to_comp(c, env)
    elif type(c) == str :
        if (c == '#u')|(c=='unit') : return 'unit'
        elif c == '#t' : return True
        elif c == '#f' : return False
        else : return c
    else : return c
    
def with_provedural_val(f,v, env):
    if type(f) == list :
        a = sym (f[0])
        if a != f[0]:
            f.insert(0, 'prim')
            return E(f, env)
        
        else: return val_to_comp(f, env)
    else : return f
      
def with_nameable(B, f) :
    if env.has_key(B) :
        temp = {}
        temp[ident] = n
        env.update(temp)
    else : err_to_comp("unbound-variable")

def val_to_comp(f,env):
    if type(f) == list:
        for i in range(len(f)):
            if find(f[i], env) :
                if (type(env[f[i]]) == int)|(type(env[f[i]]) == bool): f[i] = env[f[i]] 
                       
    elif type(f) == str:
        if find(f, env) : return env[f]
        else : return f
    else: return f

def err_to_comp(message):
    return ValueError ('error:'+ message)
    
def app(E1, E2, env):
    if type(E1) != str and type(E1) != list : return err_to_comp('nonprocedural-rator')
    else :
        Iv = E(E1, env)
        Ic = E(E2, env)
        Ip = with_value(Ic, env) 
        if type(E1) == str :
            if E1 != sym(E1) : return sym(E1)
            if find(Iv, env) : env[Iv] = Ip
            else : extend(Iv, Ip, env)
            return Ip
                
        elif type(Iv) == str:
            if (type(Ip) == int) | (type(Ip) == bool):
                a = env.popitem()
                if type(a[1])==list:
                    for i in range(len(a[1])) :
                        if a[1][i] == Iv : a[1][i] = Ip

                for key in env.keys():
                    if type (env[key]) == list :
                        for i in range(len(env[key])):
                            if a[0] == env[key][i] : env[key][i] = Ip
                    elif type (env[key]) == str:
                        for i in range(len(env[key])):
                                if a[0] == env[key][i] : env[key][i] = Ip
                              
            else :
                a = env.popitem()
                for key in env.keys():
                    if type (env[key]) == list :
                        for i in range(len(env[key])):
                            if a[0] == env[key][i] : env[key][i] = Iv
                    elif type (env[key]) == str:
                        for i in range(len(env[key])):
                                if a[0] == env[key][i] : env[key][i] = Iv

                if type(a[1]) == list:
                    for i in range(len(a[1])) :
                        if a[1][i] == a[0] : a[1][i] = Iv
            return a[1]

        else :
            if (type(Ip) == int) | (type(Ip) == bool): #변수 Iv가 <- IP(상수값) 으로
                a = env.popitem()

                for key in env.keys():
                    if type (env[key]) == list :
                        for i in range(len(env[key])):
                            if a[0] == env[key][i] : env[key][i] = Ip
                        
                    elif type (env[key]) == str:
                        for i in range(len(env[key])):
                            if a[0] == env[key][i] : env[key][i] = Ip

                t = []
                for i in range(len(env)) : t.append(env.popitem())
                    
                extend(a[0], Ip, env)
                
                for i in range(len(t)) : extend(t[i][0],t[i][0], env)
                return with_provedural_val(Iv,Ip, env)

            else :
                for key in env.keys():
                    if type (env[key]) == list :
                        for i in range(len(env[key])):
                            if Ip == env[key][i] : env[key][i] = Iv
                              
                    elif type (env[key]) == str:
                        for i in range(len(env[key])):
                            if Ip == env[key][i] : env[key][i] = Iv

            
            return with_provedural_val(Ip,Iv, env)


def lam(I, E1, env):
    if type(I) != str : return err_to_comp('unbound-variable')
    else :
        A = extend(I, I, env)
        p = E(E1, env)
        del env[I]
        a = extend(I, p, env)
        return I

def prim(exp, env):
    op = exp.pop(0)
    val = []
    for i in range(len(exp)):
        c = E(exp[i], env)
        if type(c) == ValueError : return err_to_comp('err%d' %i)
        else : val.append(with_value(c, env))
    return O(op, val, env)

def O(op, v, env):
    if(op == 'not') :
        if type(v[0]) != bool:
            if  find(v[0], env) :
                env[v[0]] = [op, v[0]]
                return env[v[0]]
            else : return err_to_comp ('not-a-boolean')
            
        else : return (not v[0])
        
    elif((op == 'and')| (op == 'or')|(op == 'bool=?')) :
        if(len(v) != 2) : return err_to_comp (op + 'wrong-number-of-args')
        elif (type(v[0]) != bool) | (type(v[1]) != bool) :
            if find(v[0], env):
                env[v[0]] = [op, v[0], v[1]]
                return env[v[0]]
                
            elif find(v[1], env) :
                env[v[1]] = [op, v[0], v[1]]
                return env[v[1]]
                
            else : return err_to_comp ('not-a-boolean')
            
        else:
            if op == 'and' : return ( v[0] and v[1] )   
            elif op == 'or' : return ( v[0] or v[1] )
            else:
                if v[0] == v[1] : return True
                else : return False
            
        
    elif((op == '+')| (op == '-')|(op == '*')| (op == '/')|(op == '%')|(op == 'int=?')):
        if(len(v) != 2) : return err_to_comp (op + 'wrong-number-of-args')
        elif ((type (v[0]) != int) | (type(v[1]) != int)) :
            if find(v[0], env):
                env[v[0]] = [op, v[0], v[1]]
                return env[v[0]]
                
            elif find(v[1], env) :
                env[v[1]] = [op, v[0], v[1]]
                return env[v[1]]
                
            else : return err_to_comp ('not-an-integer')

        else :
            if op == '+' : return ( v[0] + v[1] )    
            elif op == '-': return ( v[0] - v[1] )    
            elif op == '*': return ( v[0] * v[1] )   
            elif op == '/':
                if v[1] != 0 :return ( v[0] // v[1] )
                else : return err_to_comp('divide-by-zero')
                
            elif op == 'int=?':
                if v[0] == v[1] : return True
                else : return False
                
            else:
                if v[1] != 0 :return ( v[0] % v[1] )
                else : return err_to_comp ('divide-by-zero')
                

        
    elif((op == '<')| (op == '<=')|(op == '=')| (op == '!=')|(op == '>=')|(op == '>')):
        if(len(v) != 2) : return err_to_comp (op + 'wrong-number-of-args')
        elif (type(v[0]) != int) | (type(v[1]) != int) :
            if find(v[0], env) :
                env[v[0]] = [op, v[0], v[1]]
                return env[v[0]]
                
            elif find(v[1], env) :
                env[v[1]] = [op, v[0], v[1]]
                return env[v[1]]
                
            else : return err_to_comp ('not-an-integer')
            
        else :
            if op == '<':
                if v[0] < v[1] : return True
                else : return False
                
            elif op == '>':
                if v[0] > v[1] : return True
                else : return False
                
            elif op == '<=':
                if v[0] <= v[1] : return True
                else : return False
                
            elif op == '=':
                if v[0] == v[1] : return True
                else : return False
                
            elif op == '!=':
                if v[0] != v[1] : return True
                else : return False
                
            else:
                if v[0] >= v[1] : return True
                else : return False
                
   
    elif((op == 'int?')| (op == 'unit?')|(op == 'bool?')| (op == 'sym?')|(op == 'pair?')|(op == 'proc?')):
        if(len(v) != 1) : return err_to_comp (op + 'wrong-number-of-args')
        elif find(v[0], env) :
            env[v[0]] = [op, v[0]]
            return env[v[0]]

        else :
            if op == 'int?':
                if  type(v[0]) == int : return True
                else : return False
                
            elif op == 'unit?':
                if ((v[0] == '#u')|(v[0]=='unit')): return True
                else : return False
                
            elif op == 'bool?':
                if type(v[0]) == bool: return True
                else : return False
                
            elif op == 'sym?':
                if sym(v[0]) == v[0] : return True
                else : False
                
            elif op == 'pair?':
                if type(v[0]) == tuple : return True
                else : return False
                
            else:
                if type(v[0]) == list | type(v[0]) == 'function': return True
                else : return False
                
    elif((op == 'unit=?')| (op == 'sym=?')|(op == 'pair=?')|(op == 'proc=?')):
        if(len(v) != 2) : return err_to_comp (op + 'wrong-number-of-args')

        else :
            if op == 'unit=?':
                if ((v[0] != '#u') |( v[1] != '#u')|(v[0]!= 'unit')|(v[1]!='unit')) : return err_to_comp ('not-an-unit')
                else : 
                    if v[0] == v[1] : return True
                    else : return False
                
            elif op == 'sym=?':
                if (sym(v[0]) != v[0]) | (sym(v[1]) != v[1]) : return err_to_comp ('not-a-symlit')
                else : 
                    if v[0] == v[1] : return True
                    else : return False
                
            elif op == 'pair=?':
                if (type(v[0]) != tuple) | (type(v[1]) != tuple) : return err_to_comp ('not-a-pair')
                else : 
                    if v[0] == v[1] : return True
                    else : return False
                
            else:
                if (type(v[0]) != list) | (type(v[1]) != list) : return err_to_comp ('not-a-proceure')
                else : 
                    if v[0] == v[1] : return True
                    else : return False
    

    elif((op == 'fst')| (op == 'snd')):
        if(len(v) != 1) : return err_to_comp (op + 'wrong-number-of-args')
        elif type(v[0]) != tuple :
            if find(v[0], env) :
                env[v[0]] = [op, v[0]]
                return env[v[0]]
            
            else : return err_to_comp ('not-a-pair')
        else:
            tup = v[0]
            if op == 'fst' : return tup[0]
            else : return tup[1]
            
    else : return
    

def ifunction(E1, E2, E3,env):
    b = E(E1, env)
    if type(b) == bool:
        if(b) : return E(E2 , env)
        else : return E(E3, env)
        
    else : return err_to_comp ('nonbool-in-if-test')

def L(L):
    if type(L) == int: return L
    elif L == '#u' : return 'unit'
    elif L == '#t' : return True
    elif L == '#f' : return False
    else : return L
        
def first(exp, inputs):
    ident = exp.pop(0)
    if len(exp) == 1 : Ebody = exp.pop(0)
    else: Ebody = exp
    a = Ebody[0]
    env ={}
    
    if(len(ident) != len(inputs)) : return ValueError('wrong-number-of-args')
    
    for i in range(len(ident)):
        env[ident[i]] = IE(inputs[i])
   
    value = E(Ebody, env)
    if type(a) == list :
        if type(value) == list:
            for i in range(len(value)):
                if type(value[i]) == ValueError : return value[i]

    if type(value) == int : return value
    elif type(value) == bool : return value
    elif type(value) == tuple : return value
    elif type(value) == list :
        a = sym (value[0])
        if a != value[0]:
            value.insert(0, 'prim')
            if find(value[2],env) :
                if type(env[value[2]]) == int: value[2] = env[value[2]]
            
            if find(value[3],env) :
                if type(env[value[3]]) == int: value[3] = env[value[3]]

            if((type(value[2]) == int) & (type(value[3]) == int)) : value = E(value, env)
            else : value = 'procedure '+str(value[2]) + value[1] + str(value[3])
            return value
                          
    elif type(value) == str :
        hah = value
        value = E(value, env)
        if a == 'lam' :
            if type(value) == list :
                value.insert(0, 'prim')
            return (lambda hah : value)
        return value
    
    else: return value


def P(exp):
    if(exp[0] == 'flk') : del exp[0]
    else : raise ValueError('NOT A FLK PROGRAM')

    return (lambda x : first(exp, x))


def extend(ident, n, env):
    if find(ident, env) :
        a = env[ident]
        env[ident] = n
        if type(a) == list :
            env[ident] = ident
            env[ident] = prim(a, env)
            
    else :
        temp = {}
        temp[ident] = n
        env.update(temp)
        if type(n) == str:
            if env.get(n) != None : env[ident] = env[n]
    return env[ident]


def IE(ie):
    if type(ie) == list :
        a = ie.pop(0)
        if a == 'pair' : 
            if len(ie) != 2 : return ValueError('not-a-pair')
            else : return tuple(IE(ie[0]), IE(ie[1]))
        elif a == 'sym' :
            if ie[0] != sym(ie[0]) : return ValueError ('wrong-number-of-args')
            else : return ie[0]
        else : return ValueError('wrong-number-of-args')
            
    else :
        if type(ie) == int: return ie
        elif type(ie) == tuple :
            if len(ie) != 2 : return ValueError('not-a-pair')
            else : return ie
        elif ie == '#u' : return ie 
        elif ie == '#t' : return True
        elif ie == '#f' : return False
        else : return ValueError('unbound-variable')


def sym(sym):
    if sym == 'not' : return err_to_comp('unbound-variable')
    elif sym == 'and' : return err_to_comp('unbound-variable')
    elif sym == 'or' : return err_to_comp('unbound-variable')
    elif sym == 'app' : return err_to_comp('unbound-variable')
    elif sym == 'error' : return err_to_comp('unbound-variable')
    elif sym == 'flk' : return err_to_comp('unbound-variable')
    elif sym == 'if' : return err_to_comp('unbound-variable')
    elif sym == 'pair' : return err_to_comp('unbound-variable')
    elif sym == 'prim' : return err_to_comp('unbound-variable')
    elif sym == 'lam' : return err_to_comp('unbound-variable')
    elif sym == 'rec' : return err_to_comp('unbound-variable')
    elif sym == '#u' : return err_to_comp('unbound-variable')
    elif sym == '#t' : return err_to_comp('unbound-variable')
    elif sym == '#f' : return err_to_comp('unbound-variable')
    elif sym == 'fst' : return err_to_comp('unbound-variable')
    elif sym == 'snd' : return err_to_comp('unbound-variable')
    elif sym == 'int' : return err_to_comp('unbound-variable')
    elif sym == 'bool' : return err_to_comp('unbound-variable')
    elif sym == 'str' : return err_to_comp('unbound-variable')
    elif sym == '+' : return err_to_comp('unbound-variable')
    elif sym == '-' : return err_to_comp('unbound-variable')
    elif sym == '%' : return err_to_comp('unbound-variable')
    elif sym == '/' : return err_to_comp('unbound-variable')
    elif sym == '*' : return err_to_comp('unbound-variable')
    elif sym == '>' :return err_to_comp('unbound-variable')
    elif sym == '<' :return err_to_comp('unbound-variable')
    elif sym == '>=' :return err_to_comp('unbound-variable')
    elif sym == '<=' :return err_to_comp('unbound-variable')
    elif sym == '=' :return err_to_comp('unbound-variable')
    elif sym == '!=' :return err_to_comp('unbound-variable')
    else : return sym



def find(exp, env):
    if exp in env.keys(): return True
    else: return False

def E(exp, env):
    if type(exp) != list:
        if find(exp, env) : return env[exp]
        else : return val_to_comp(L(exp),env)

    else :
        cmd = exp.pop(0)
        if cmd == 'prim':
            if len(exp) > 2 :
                if exp[1] == '?' :
                    exp[1] = exp[0] + exp[1]
                    exp.pop(0)
                    
                elif exp[2] == '?':
                    exp[2] = exp[0]+exp[1]+exp[2]
                    exp.pop(0)
                    exp.pop(0)
            return prim(exp, env)

        elif cmd == 'if' :
            if len(exp)!=3 : return err_to_comp('wrong-number-of-args')
            else : return  ifunction(exp[0], exp[1], exp[2],env)
            
        elif cmd == 'error' :
            if len(exp)!=1 : return err_to_comp('wrong-number-of-args')
            return  err_to_comp(exp[0], env)
        
        elif cmd == 'sym':
            if len(exp)!=1 : return err_to_comp('wrong-number-of-args')
            return sym(exp[0])
        
        elif cmd == 'app':
            if len(exp)!=2 : return err_to_comp('wrong-number-of-args')
            return app(exp[0],exp[1], env)
        
        elif cmd == 'lam':
            if len(exp)!=2 : return err_to_comp('wrong-number-of-args')
            return lam(exp[0],exp[1], env)
        
        elif cmd == 'pair':
            if len(exp)!=2 : return err_to_comp('wrong-number-of-args')
            return (E(exp[0],env), E(exp[1],env))

        elif type(cmd) == list:
            results = []
            
            results.append(E(cmd, env))
            times = len(exp)
            for i in range(times):
                cmd = exp.pop()
                results.append(E(cmd, env))
            return results
                
        else : return
