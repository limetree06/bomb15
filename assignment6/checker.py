import logging

logger = logging.getLogger("checker")


def type_check(prog, prog_type):
    result = ['=>',[]]
    env = []
   # logger.info('prog: {}'.format(prog))
   # logger.info('prog_type: {}'.format(prog_type))
    prog.pop(0)
    given = prog.pop(0)

    for i in list(given):
        env.append(i)
        if len(i) != 0 : result[1].append(i[1])
        
    result.append(flexk(prog.pop(0), env))
    print(result)

    if result == prog_type : return True
    else : return False


def flexk(Ebody, env):
    value = []
    if type(Ebody) != list :
        if type(Ebody) == int : return 'int'
        elif type(Ebody) == tuple : return 'pair'
        elif (Ebody == '#t') | (Ebody == '#f') : return 'bool'
        elif Ebody == '#u' : return 'unit'
        elif sym(Ebody):
            for i in list(env):
                if len(i)!= 0:
                    if i[0] == Ebody:
                        if (type(i[1]) == list) & (i[1][0] == '->') : return i[1][2]
                        else : return i[1]
            return 'symb'
 
        else : type(Ebody)
        
    else :
        if len(Ebody) == 0 : return
        else : cmd = Ebody.pop(0)
        if cmd == 'error': return Ebody[1]
        elif cmd == 'sym':
            for i in list(env):
                if len(i)!= 0:
                    if i[0] == cmd:
                        if (type(i[1]) == list) & (i[1][0] == '->') : return i[1][2]
                        else : return i[1]
            return 'symb'
        
        elif cmd == 'if':
            if flexk (Ebody.pop(0), env) != 'bool' :  return 'ill-type'
            value = flexk (Ebody.pop(0), env)
            return value
        
        elif (cmd == 'prim') | (cmd == '@') | (op(cmd)) :
            if (cmd == 'prim') | (cmd == '@') : return flexk (Ebody, env)
            if len(Ebody) == 1:
                E = flexk (Ebody.pop(0), env)
                if cmd == 'not' : return E
                elif (cmd == 'sym?') | (cmd == 'int?') | (cmd == 'bool?') : return 'bool'
                else : return

            E1 = flexk (Ebody.pop(0), env)
            E2 = flexk (Ebody.pop(0), env)
            if (cmd == '+') | (cmd == '-') | (cmd == '*') | (cmd == '%') | (cmd == '/') | (cmd == '+'):
                if (E1 == 'int') & (E2 == 'int') : return 'int'
            elif (cmd == '<') | (cmd == '<=') | (cmd == '=') | (cmd == '!=') | (cmd == '>=') | (cmd == '>') :
                if E1 == E2 : return 'bool'
                
            elif (cmd == 'sym=?') | (cmd == 'int=?') | (cmd == 'bool=?') :
                if E1 == E2 : return 'bool'

            elif (cmd == 'and') |(cmd == 'or'):
                if E1 == E2 : return E
            else : return

        elif cmd == 'abs':
            value = ['->']
            E = Ebody.pop(0)
            val = []
            for i in list(E):
                if len(i) == 2:
                    env.append(i)
                    val.append(i[1])
                else : val.append(flexk (i, env))
                
            value.append(val)
            
            E = Ebody.pop(0)
            value.append(flexk (E, env))
            return value

        elif cmd == 'let':
            E = Ebody.pop(0)
            for i in list(E) :
                a = flexk (i[1], env)
                env.append([i[0],a])

            E = flexk (Ebody.pop(0), env)
            return E

        elif cmd == 'letrec':
            E = Ebody.pop(0)
            for i in list(E):
                env.append([i[0],i[1]])
                flexk (i[2], env)

            E = flexk (Ebody.pop(0), env)
            return E
                        
        elif cmd == 'the':
            T = Ebody.pop(0)
            a=Ebody.pop(0)
            E = flexk (a, env)
            if T == E : return T
            else : return 'error'
            
        elif sym(cmd):
            for i in list(env):
                if len(i)!= 0:
                    if i[0] == cmd:
                        if (type(i[1]) == list) & (i[1][0] == '->') : return i[1][2]
                        else : return i[1]
                        
            E = flexk (Ebody.pop(0), env)
            env.append([cmd, E])
            return
        
        else : return 'error'

def sym(cmd):
    if cmd == 'abs': return False
    elif cmd == 'error': return False
    elif cmd == 'if': return False
    elif cmd == 'prim': return False
    elif cmd == '@': return False
    elif cmd == 'abs': return False
    elif cmd == 'let': return False
    elif cmd == 'letrec': return False
    elif cmd == 'prim': return False
    elif cmd == 'sym': return False
    elif cmd == 'the': return False
    elif cmd == '#u': return False
    elif cmd == '#t': return False
    elif cmd == '#f': return False
    elif cmd == 'flexk': return False
    elif cmd == 'not': return False
    elif cmd == 'and': return False
    elif cmd == 'or': return False
    else : return True

def op(cmd):
    if cmd == '+': return True
    elif cmd == '-': return True
    elif cmd == '*': return True
    elif cmd == '%': return True
    elif cmd == '/': return True
    elif cmd == '<': return True
    elif cmd == '<=': return True
    elif cmd == '=': return True
    elif cmd == '!=': return True
    elif cmd == '>=': return True
    elif cmd == '>': return True
    elif cmd == 'not': return True
    elif cmd == 'and': return True
    elif cmd == 'or': return True
    elif cmd == 'sym?': return True
    elif cmd == 'int?': return True
    elif cmd == 'bool?': return True
    elif cmd == 'sym=?': return True
    elif cmd == 'int=?': return True
    elif cmd == 'bool=?': return True
    else : return False


