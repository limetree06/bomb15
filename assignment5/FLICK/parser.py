import re
import logging

logger = logging.getLogger("parser")


TOKEN_REGEX = re.compile(
    r'\s*(-?\d+|\w+|\(|\)|(\*)|\:|\^|\?|\=|\+|\-|\%|\/|\>|\<|(flick|begin|cell|lam|app|prim|error|if|pair|#t|#f|#u|snd|fst|not|and|or|!=|>=|<=)(\b|$))')

def parse(exp):
    tokens = tokenize(exp)
    token = next(tokens)
    if token != '(':
        raise ValueError('NOT A FLICK PROGRAM')
    token = next(tokens)
    if token != 'flick':
        raise ValueError('NOT A FLICK PROGRAM')
    body = parse_param_and_body(tokens, next(tokens))
    body.insert(0, token)
    logger.debug('body: {}'.format(body))
    return body

def parse_param_and_body(tokens, token):
    level = 1
    def parse_exp(token, result):
        nonlocal level
        if token == '(':
            level += 1
            # parse formal params
            result.append(parse_exp(next(tokens), []))
            # parse body
            return parse_exp(next(tokens), result)
        if token == ')':
            level -= level
            return result
        if token[0] in '0123456789':
            result.append(int(token))
            return parse_exp(next(tokens), result)
        if token != 'END':
            result.append(token)
            return parse_exp(next(tokens), result)
        
        else:
            raise ValueError('LEXICAL_ERROR')
        
    result = parse_exp(token, [])
    if level == 0:
        return result

    raise ValueError('LEXICAL_ERROR')

def tokenize(source):
    start = 0
    while start < len(source):
        m = TOKEN_REGEX.match(source, start)
        logger.debug('m: {}'.format(m))
        if m is None:
            raise ValueError('LEXICAL_ERROR')
    
        yield m.group(0).strip()
        start = m.end()
        
    yield 'END'
