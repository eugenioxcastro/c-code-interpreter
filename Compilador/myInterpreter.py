symbol_table = {}
func_table = {}


def run(p):
    global symbol_table
    if type(p) == tuple:
        # Operations and conditionals
        if p[0] == '++':
            if p[1] not in symbol_table:
                raise TypeError(
                    "Syntax error! Trying to use unary operators on non existing variable: ", p[1])
            symbol_table[p[1]]['value'] = symbol_table[p[1]]['value'] + 1
            return
        elif p[0] == '--':
            if p[1] not in symbol_table:
                raise TypeError(
                    "Syntax error! Trying to use unary operators on non existing variable: ", p[1])
            symbol_table[p[1]]['value'] = symbol_table[p[1]]['value'] - 1
            return
        elif p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '%':
            return run(p[1]) % run(p[2])
        elif p[0] == '==':
            return run(p[1]) == run(p[2])
        elif p[0] == '!=':
            return run(p[1]) != run(p[2])
        elif p[0] == '<':
            return run(p[1]) < run(p[2])
        elif p[0] == '>':
            return run(p[1]) > run(p[2])
        elif p[0] == '<=':
            return run(p[1]) <= run(p[2])
        elif p[0] == '>=':
            return run(p[1]) >= run(p[2])
        elif p[0] == '!':
            return not run(p[1])
        elif p[0] == '&&':
            return run(p[1]) and run(p[2])
        elif p[0] == '||':
            return run(p[1]) or run(p[2])
        elif p[0] == 'true':
            return True
        elif p[0] == 'false':
            return False

        # Assign
        elif p[0] == '=':
            var_name = p[1]
            var_type = symbol_table[var_name]['type']
            var_value = symbol_table[var_name]['value']
            value = run(p[2])

            if value == 'true' or value == 'false':
                modify_bool(var_name, value)
                return

            if type(var_value) == type(value):
                symbol_table[var_name]['value'] = value
                return

            # As I assign all numbers as floats, I need to do this extra magic to
            # ensure in my program I am not assigning a float to an int
            if (type(
                value).__name__ == "float"
                and (var_type == "int" or var_type == "double" or var_type == "float")
                    and is_integer_number(value)):
                symbol_table[var_name]['value'] = value
                return

            if (type(value).__name__ == "float" and var_type == "float"):
                symbol_table[var_name]['value'] = value
                return

            else:
                raise TypeError(
                    "Syntax Error! Trying to assign different type (",  type(value), value,  ") to ", var_type, var_name)

        # VARIABLES
        elif p[0] == 'var':
            return symbol_table[p[1]]['value']

        # DECLARATIONS
        elif p[0] == 'int' or p[0] == 'float' or p[0] == 'doble' or p[0] == 'char' or p[0] == 'string' or p[0] == 'bool':

            if type(p[1]) == tuple and p[1][0] != '=':
                variables = flatten_tuple(p[1])
                for var in variables:
                    initialize_var(p[0], var)
            elif type(p[1]) == tuple and p[1][0] == '=':
                symbol_table[p[1][1]] = {'type': p[0], 'value': run(p[1][2])}
            else:
                initialize_var(p[0], p[1])

        # PRINT
        elif p[0] == 'write':
            result = run(p[1])
            if type(result).__name__ == "float":
                result = convert_to_int_if_decimal_is_zero(result)
            print(result)
        elif p[0] == 'writeln':
            result = run(p[1])
            # As internally all my numbers are floats, I need to convert those values before printing
            if type(result).__name__ == "float":
                result = convert_to_int_if_decimal_is_zero(result)
            print(result)
            # extra line for writeln
            print()
        # IF
        elif p[0] == 'if':
            condition = run(p[1])
            if condition:
                statements = find_valid_tuples(p[2])
                run_statements(statements)
                return
            else:
                return None
        elif p[0] == 'if_else':
            condition = run(p[1])
            if condition:
                statements = find_valid_tuples(p[2])
                run_statements(statements)
                return
            else:
                statements = find_valid_tuples(p[3])
                run_statements(statements)
                return
        # FOR
        elif p[0] == 'for':
            run(p[1])
            cond = run(p[2])
            while (cond == True):
                statements = find_valid_tuples(p[4])
                run_statements(statements)
                run(p[3])
                cond = run(p[2])
        # WHILE
        elif p[0] == 'while':
            cond = run(p[1])
            while (cond == True):
                statements = find_valid_tuples(p[2])
                run_statements(statements)
                cond = run(p[1])
        # FUNC
        elif p[0] == 'func':
            func_table[p[1]] = {'statements': p[2]}
            # record the func var in my symbols table to avoid errors
            symbol_table[p[1]] = {'type': p[0], 'value': p[2]}
        elif p[0] == 'func_call':
            if p[1] not in func_table:
                raise TypeError(
                    "Syntax Error: Trying to call undefined function", p[1])
            statements = find_valid_tuples(func_table[p[1]]['statements'])
            run_statements(statements)

    else:
        return p


def flatten_tuple(t):
    if isinstance(t, tuple):
        flat_list = []
        for item in t:
            flat_list.extend(flatten_tuple(item))
        return flat_list
    else:
        return [t]


def initialize_var(type, var):
    if type == "int" or type == "double" or type == "float":
        symbol_table[var] = {'type': type, 'value': 0}
    elif type == "string" or type == "char":
        symbol_table[var] = {'type': type, 'value': ""}
    elif type == "bool":
        symbol_table[var] = {'type': type, 'value': False}


def modify_bool(var, bool_str):
    symbol_table[var]['value'] = bool(bool_str)


def convert_to_int_if_decimal_is_zero(num):
    if isinstance(num, float):
        if num.is_integer():
            return int(num)
    return num


def is_integer_number(num):
    if isinstance(num, (int, float)):
        return num.is_integer() if isinstance(num, float) else True
    return False


def is_valid_tuple(tup):
    return not isinstance(tup[0], tuple)


def find_valid_tuples(tup):
    valid_tuples = []
    if isinstance(tup, tuple):
        if is_valid_tuple(tup):
            valid_tuples.append(tup)
        else:
            for item in tup:
                valid_tuples.extend(find_valid_tuples(item))
    return valid_tuples


def run_statements(statements):
    for statement in statements:
        run(statement)
