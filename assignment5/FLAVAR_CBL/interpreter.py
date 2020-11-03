import logging

logger = logging.getLogger("interpreter")

def with_value(c,env, state) :
    if (type(c) ==  int) | (type(c) == bool) | (type(c) == tuple) : return c
    elif (type(c) == 'function') | (type(c) == 'list'): return val_to_comp(c, env, state)
    elif type(c) == str :
        if c == '#u' : return c
        elif c == 'uint' : return c
        elif c == '#t' : return True
        elif c == '#f' : return False
        else : return c
    else : return c
    
def with_provedural_val(f, env, state):
    if type(f) == list :
        a = sym (f[0])
        if a != f[0]:
            f.insert(0, 'prim')
            return E(f, env, state)
        
        else: return val_to_comp(f, env,state)
    else : return f
      
def with_nameable(B, f) :
    if env.has_key(B) :
        temp = {}
        temp[ident] = n
        env.update(temp)
    else : err_to_comp("unbound-variable")

def val_to_comp(f,env, state):
    if type(f) == list:
        for i in range(len(f)):
            if find(f[i], env) :
                if (type(state [env[f[i]]]) == int)|(type(state [env[f[i]]]) == bool): f[i] = state [env[f[i]]]
        return f
                       
    elif type(f) == str:
        if find(f, env) : return state [env[f]]
        else : return f
        
    elif type(f) == int:
        if f > 999 : return state [f]
        else: return f
        
    else : return f

def err_to_comp(message):
    return ValueError ('error:'+ message)
    
def app(E1, E2, env, state):
    if type(E1) != str and type(E1) != list : return err_to_comp('nonprocedural-rator')
    else :
        Iv = E(E1, env, state)
        Ic = E(E2, env, state)
        Ip = with_value(Ic, env, state)
        
        if type(E1) == str :
            if find(E1, env) : state [env[E1]] = Ip
            else : extend(E1, Ip, env, state)
            return Ip
                
        if type(Iv) == str:
            if (type(Ip) == int) | (type(Ip) == bool):
                a = env.popitem()
                b = state.popitem()
                if type(b[1])==list:
                    for i in range(len(b[1])) :
                        if b[1][i] == Iv : b[1][i] = Ip

                for key in env.keys():
                    if type (state[env[key]]) == list :
                        for i in range(len(state[env[key]])):
                            if a[0] == state[env[key]][i] : state[env[key]][i] = Ip
                    elif type (state[env[key]]) == str:
                        for key in state.keys():
                                if a[0] == state[key] : state[key] = Ip
                              
            else :
                a = env.popitem()
                b = state.popitem()
                for key in env.keys():
                    if type (state[env[key]]) == list :
                        for i in range(len(state[env[key]])):
                            if a[0] == state[env[key]][i] : state[env[key]][i] = Iv
                    elif type (state[env[key]]) == str:
                        for key in state.keys():
                            if a[0] == state[key] : state[key] = Iv

                if type(b[1]) == list:
                    for i in range(len(b[1])) :
                        if b[1][i] == a[0] : b[1][i] = Iv
            return b[1]

        else :
            if (type(Ip) == int) | (type(Ip) == bool): #변수 Iv가 <- IP(상수값) 으로
                a = env.popitem()
                b = state.popitem()

                for key in env.keys():
                    if type (state[env[key]]) == list :
                        for i in range(len(state[env[key]])):
                            if a[0] == state[env[key]][i] : state[env[key]][i] = Ip
                        
                    elif type (state[env[key]]) == str:
                        for key in env.keys():
                            if a[0] == state[env[key]] : state[env[key]] = Ip

                t = []
                j = []
                for i in range(len(env)) :
                    t.append(env.popitem())
                for i in range(len(state)) :
                    j.append(state.popitem())
                    
                extend(a[0], Ip, env, state)
                
                for i in range(len(t)) : extend(t[i][0],t[i][0], env, state)
                return with_provedural_val(Iv, env, state)

            else :
                for key in env.keys():
                    if type (state[env[key]]) == list :
                        for i in range(len(state[env[key]])):
                            if Ip == state[env[key]][i] : state[env[key]][i] = Iv
                              
                    elif type (state[env[key]]) == str:
                        for key in env.keys():
                            if Ip == state[env[key]] : state[env[key]] = Iv

            
            return with_provedural_val(Ip, env, state)


def lam(I, E1, env, state):
    if type(I) != str : return err_to_comp('unbound-variable')
    else :
        A = extend(I, 'unassigned', env, state)
        p = E(E1, env, state)
        if state[env[I]] == 'unassigned' : del env[I]
        a = extend(I, p, env, state)
        return I

def prim(exp, env, state):
    op = exp.pop(0)
    val = []

    for i in range(len(exp)):
        c = E(exp[i], env, state)
        if type(c) == ValueError : return err_to_comp('err%d' %i)
        else : val.append(with_value(c, env, state))

    if(op == ':='):
        if len(exp) != 2 : return err_to_comp ('wrong-number-of-args')
        if type(exp[0]) != list : 
            if find (exp[0],env) :
                state[env[exp[0]]] = val[1]
                return state[env[exp[0]]]
        
            elif find (exp[0],state) :
                state[exp[0]] = val[1]
                return state[exp[0]]
            
    elif(op == 'cell=?'):
        if len(exp) != 2 : return err_to_comp ('wrong-number-of-args')
        else :
            if ((exp[0] > 1000) & (exp[1] > 1000)) : 
                if exp[0] == exp[1] : return True
                else: return False
                
    elif(op == 'cell?'):
        if len(exp) != 1 : return err_to_comp ('wrong-number-of-args')
        else :
            if exp[0] > 999 : return True
            
    return O(op, val,env, state)

def O(op, v, env, state):
    if(op == '^'):
        if len(v) != 1 : return err_to_comp ('wrong-number-of-args')
        else :
            if v[0] > 999 : return state[v[0]]
            else : return err_to_comp('not-a-cell')
        
    elif(op == 'cell=?'):
        if len(v) != 2 : return err_to_comp ('wrong-number-of-args')
        else :
            if ((v[0] < 1000) |(v[1] < 1000)) : return err_to_comp('not-a-cell')
            else :
                if v[0] == v[1] : return True
                else: return False
                
    elif(op == ':='):
        if len(v) != 2 : return err_to_comp ('wrong-number-of-args')
        if v[0] > 999 : state[v[0]] = v[1]
        return state[v[0]]
        
    elif(op == 'cell?'):
        if len(v) != 1 : return err_to_comp ('wrong-number-of-args')
        else :
            if v[0] > 999 : return True
            else : return False
    
    elif(op == 'not') :
        if type(v[0]) != bool:
            if  find(v[0], env) :
                state[env[v[0]]] = [op, v[0]]
                return state[env[v[0]]]
            else : return err_to_comp ('not-a-boolean')
            
        else : return (not v[0])
        
    elif((op == 'and')| (op == 'or')|(op == 'bool=?')) :
        if(len(v) != 2) : return err_to_comp (op + 'wrong-number-of-args')
        elif (type(v[0]) != bool) | (type(v[1]) != bool) :
            if find(v[0], env):
                state[env[v[0]]] = [op, v[0], v[1]]
                return state[env[v[0]]]
                
            elif find(v[1], env) :
                state[env[v[1]]] = [op, v[0], v[1]]
                return state[env[v[1]]]
                
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
                state[env[v[0]]] = [op, v[0], v[1]]
                return state[env[v[0]]]
                
            elif find(v[1], env) :
                state[env[v[1]]] = [op, v[0], v[1]]
                return state[env[v[1]]]
                
            else : return err_to_comp ('not-a-integer')

        else :
            if op == '+' : return ( v[0] + v[1] )    
            elif op == '-': return ( v[0] - v[1] )    
            elif op == '*': return ( v[0] * v[1] )   
            elif op == '/':
                if v[1] != 0 :return ( v[0] // v[1] )
                else : return err_to_comp ('divide-by-zero')
                
            elif op == 'int=?':
                if v[0] == v[1] : return True
                else : return False
                
            else:
                if v[1] != 0 :return ( v[0] % v[1] )
                else : return err_to_comp ('divide-by-zero')
                

        
    elif((op == '<')| (op == '<=')|(op == '=')| (op == '!=')|(op == '>=')|(op == '>')):
        if(len(v) != 2) : return err_to_comp (op + 'wrong-number-of-args')
        elif (type(v[0]) != int) | (type(v[1]) != int):
            if find(v[0], env) :
                state[env[v[0]]] = [op, v[0], v[1]]
                return state[env[v[0]]]
                
            elif find(v[1], env) :
                state[env[v[1]]] = [op, v[0], v[1]]
                return state[env[v[1]]]
                
            else : return err_to_comp ('not-a-integer')
            
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
            state[env[v[0]]] = [op, v[0]]
            return state[env[v[0]]]

        else :
            if op == 'int?':
                if  type(v[0]) == int : return True
                else : return False
                
            elif op == 'unit?':
                if v[0] == '#u': return True
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
                if (v[0] != '#u' | v[1] != '#u') : return err_to_comp ('not-a-unit')
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
                state[env[v[0]]] = [op, v[0]]
                return state[env[v[0]]]
            
            else : return err_to_comp ('not-a-pair')
        else:
            tup = v[0]
            if op == 'fst' : return tup[0]
            else : return tup[1]
            
    else : return
    

def ifunction(E1, E2, E3,env, state):
    b = E(E1, env, state)
    if type(b) == bool:
        if(b) : return E(E2 , env, state)
        else : return E(E3, env, state)
        
    else : return err_to_comp ('not-a-boolean')

def L(L):
    if type(L) == int: return L
    elif L == '#u' : return 'unit'
    elif L == '#t' : return True
    elif L == '#f' : return False
    else : return L
        
def first(exp, inputs):
    exp.pop(0)
    ident = exp.pop(0)
    if len(exp) == 1 : Ebody = exp.pop(0)
    else: Ebody = exp
    
    if(len(ident) != len(inputs)) : return err_to_comp('wrong-number-of-args')
    
    env = {}
    state = {}
    
    for i in range(len(ident)):
        env[ident[i]] = 1000+i
        state[1000+i] = IE(inputs[i])

    value = val_to_comp(E(Ebody, env, state), env, state)

    count = 0
    if (type(value) == list) :
        for i in range(len(value)):
            if type(value[i]) == int : count = count + 1
        if len(value)-1 == count: return with_provedural_val(value, env, state)
        
    if type(value) == int : return value
    elif type(value) == bool : return value
    elif type(value) == tuple : return value
    elif type(value) == list :
        val = 'procedure ' + str(value[1]) + value[0] + str(value[2])
        return val   
    else : return value
    
def P(exp):
    return (lambda x : first(exp, x))


def extend(ident, n, env, state):
    if find(ident, env) :
        a = state [env[ident]]
        state [env[ident]] = n
        if type(a) == list :
            state[env[ident]] = ident
            state[env[ident]] = prim(a, env, state)
    else :
        temp = {}
        temp[ident] = 1000 + len(state)
        env.update(temp)
        temp2 = {}
        temp2[temp[ident]] = n
        state.update(temp2)

        if type(n) == str:
            if env.get(n) != None : state[env[ident]] = state[env[n]]
            
    return state[env[ident]]


def IE(ie):
    if type(ie) == list :
        a = ie.pop(0)
        if a == 'pair' : 
            if len(ie) != 2 : return err_to_comp('not-a-pair')
            else : return tuple(IE(ie[0]), IE(ie[1]))
        elif a == 'sym' :
            if ie[0] != sym(ie[0]) : return err_to_comp('wrong-number-of-args')
            else : return ie[0]
        else : return err_to_comp('wrong-number-of-args')
            
    else :
        if type(ie) == int: return ie
        elif type(ie) == tuple :
            if len(ie) != 2 : return err_to_comp('not-a-pair')
            else : return ie
        elif ie == 'unit' : return ie
        elif ie == '#u' : return ie 
        elif ie == '#t' : return True
        elif ie == '#f' : return False
        else : return err_to_comp('wrong-number-of-args')

        

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

def begin(exp, env, state):
    a = E(exp[0], env, state)
    value = E(exp[1], env, state)
    return value


def cell(exp,env, state):
    value = E(exp, env, state)
    location = 1000 + len(state)
    state[location] = value
    return location

def seet(I,exp, env, state):
    value = E(exp, env, state)
    if find(I, env): state[env[I]] = value
    else : extend(I, value, env, state)
    return value

def find(exp,env):
    if exp in env.keys(): return True
    else: return False
    

def E(exp,env, state):
    if type(exp) != list:
        if find(exp, env) :
            if state [env[exp]] == 'unassigned' : return exp
            else : return state [env[exp]]

        elif find(exp, state):
            if state [exp] == 'unassigned' : return exp
            else : return state [exp]
            
        else : return val_to_comp(L(exp), env, state)

    else :
        if len(exp) == 0 : return exp 
        cmd = exp.pop(0)
        if (cmd == 'prim'):
            if len(exp) > 2 :
                if exp[1] == '?' :
                    exp[1] = exp[0] + exp[1]
                    exp.pop(0)
                    
                elif exp[2] == '?':
                    exp[2] = exp[0]+exp[1]+exp[2]
                    exp.pop(0)
                    exp.pop(0)
                    
                elif exp[0] == ':':
                    exp[1] = exp[0] + exp[1]
                    exp.pop(0)
                    
            return prim(exp, env, state)

        elif cmd == 'if' :
            if len(exp) < 2 : return err_to_comp('wrong-number-of-args')
            elif len(exp) == 2 :  return  ifunction(exp[0], exp[1], None ,env, state)
            else : return  ifunction(exp[0], exp[1], exp[2],env, state)
            
        elif cmd == 'error' :
            if len(exp)!=1 : return err_to_comp('wrong-number-of-args')
            return  err_to_comp(exp[0])
        
        elif cmd == 'sym':
            if len(exp)!=1 : return err_to_comp('wrong-number-of-args')
            return sym(exp[0])
        
        elif cmd == 'app':
            if len(exp)!=2 : return err_to_comp('wrong-number-of-args')
            return app(exp[0],exp[1], env, state)
        
        elif cmd == 'lam':
            if len(exp)!=2 : return err_to_comp('wrong-number-of-args')
            return lam(exp[0],exp[1], env, state)
        
        elif cmd == 'pair':
            if len(exp)!=2 : return err_to_comp('wrong-number-of-args')
            return (E(exp[0],env, state), E(exp[1],env, state))

        elif cmd == 'begin':
            if len(exp)!=2 : return err_to_comp('wrong-number-of-args')
            return begin(exp, env , state)

        elif cmd == 'cell':
            if len(exp)!=1 : return err_to_comp('wrong-number-of-args')
            return cell(exp[0], env, state)

        elif cmd == 'set':
            if len(exp)!=3 : return err_to_comp('wrong-number-of-args')
            return seet(exp[1], exp[2], env, state)

        elif type(cmd) == list:
            results = []
            results.append(E(cmd, env, state))
            times = len(exp)
            for i in range(times):
                cmd = exp.pop()
                results.append(E(cmd, env, state))
            return results
    
        else : return
