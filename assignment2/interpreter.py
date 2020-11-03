import operator
from parser import parse_program
import logging

logger = logging.getLogger("interpreter")

class Irreducible(Exception):
    pass

def run(prog, inputs):
    cmd_seq, stack = IF(prog, inputs)
    if len(cmd_seq)== 0 and len(stack)==0: return 'error'

    logger.info('initial config: <{}, {}>'.format(cmd_seq, stack))

    while len(cmd_seq) > 0:
        try:
            execute(cmd_seq, stack)
            logger.info('config: <{}, {}>'.format(cmd_seq, stack))
        except Irreducible:
            return 'error'

    logger.info('final config: <{}, {}>'.format(cmd_seq, stack))

    return OF(cmd_seq, stack)

## AUGMENT THIS FUNCTION
def IF(prog, inputs):
    n, cmd_seq = parse_program(prog)
    return cmd_seq, inputs

## AUGMENT THIS FUNCTION
def OF(cmd_seq, stack):
    if len(stack) == 0 : return 'error'
    elif isinstance(stack[0], int) : return stack[0]
    else : return 'error'

## AUGMENT THIS FUNCTION
def execute(cmd_seq, stack):
    cmd = cmd_seq.pop(0)
    if isinstance(cmd, int) or (type(cmd)== type(stack)) :
        stack.insert(0, cmd)

    else:
        if len(stack) == 0 : raise Irreducible
        
        if cmd == 'pop' : stack.pop(0)

        elif cmd == 'exec':
            if type(stack[0]) != type(stack): raise Irreducible
                
            else :
                arr = stack.pop(0)
                while len(arr) > 0 : cmd_seq.insert(0,arr.pop())
             
        else:
            if cmd == 'nget':
                if isinstance(stack[0], int):
                    index = stack.pop(0)
                    
                    if isinstance(index, int) and len(stack) > index - 1:
                        stack.insert(0,stack[index-1])

                    else : raise Irreducible
                    
                else : raise Irreducible
                

            elif cmd == 'sel':
                if len(stack) < 3 : raise Irreducible
                else:
                    v1 = stack.pop(0)
                    v2 = stack.pop(0)
                    v3 = stack.pop(0)
                    
                    if isinstance(v3, int):
                        if v3 == 0 : stack.insert(0, v1)
                        else : stack.insert(0, v2)

                    else : raise Irreducible

            else :
                if len(stack) < 2 : raise Irreducible
                else :
                    v1 = stack.pop(0)
                    v2 = stack.pop(0)

                    if cmd == 'swap' :
                       stack.insert(0, v1)
                       stack.insert(0, v2)

                    elif isinstance(v1, int) and isinstance(v2, int):
                        if cmd =='add' : stack.insert(0, v2 + v1)
                        if cmd =='sub' : stack.insert(0, v2 - v1)
                        if cmd =='mul' : stack.insert(0, v2 * v1)
                        if cmd =='div' : 
                            if v1 == 0: raise Irreducible
                            elif v1* v2>0 : stack.insert(0, v2//v1) 
                            else: stack.insert(0, v2 // v1 +1)

                        if cmd =='rem' : stack.insert(0, v2 % v1)
                        
                        if cmd == 'eq' :
                            if v1==v2 : stack.insert(0, 1)
                            else : stack.insert(0, 0)

                        if cmd == 'ne' :
                            if v1!=v2 : stack.insert(0, 1)
                            else : stack.insert(0, 0)

                        if cmd == 'lt' :
                            if v1>v2 : stack.insert(0, 1)
                            else : stack.insert(0, 0)
                            
                        if cmd == 'le' :

                            if v1 >= v2 : stack.insert(0, 1)
                            else : stack.insert(0, 0)
                            
                        if cmd == 'gt' :

                            if v1<v2 : stack.insert(0, 1)
                            else : stack.insert(0, 0)
                            
                        if cmd == 'ge' :

                            if v1 <= v2 : stack.insert(0, 1)
                            else : stack.insert(0, 0)

                    else : raise Irreducible
