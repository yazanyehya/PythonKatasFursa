def is_valid_parentheses(s):
    temp = []
    for i in range(len(s)):
        if s[i] in '({[':
            temp.append(s[i])
        elif s[i] == ']' :
            if not temp or temp[-1] != '[':
                return False
            temp.pop()
        elif s[i] == '}' :
            if not temp or temp[-1] != '{':
                return False
            temp.pop()
        elif s[i] == ')' :
            if not temp or temp[-1] != '(':
                return False
            temp.pop()
    return not temp
if __name__ == '__main__':
    valid_input = "()[]{}"
    invalid_input1 = "(]"
    invalid_input2 = "([)]"
    valid_input_nested = "{[]()}"

    print(f"'{valid_input}' has valid parentheses: {is_valid_parentheses(valid_input)}")  # Should be True
    print(f"'{invalid_input1}' has valid parentheses: {is_valid_parentheses(invalid_input1)}")  # Should be False
    print(f"'{invalid_input2}' has valid parentheses: {is_valid_parentheses(invalid_input2)}")  # Should be False
    print(f"'{valid_input_nested}' has valid parentheses: {is_valid_parentheses(valid_input_nested)}")  # Should be True