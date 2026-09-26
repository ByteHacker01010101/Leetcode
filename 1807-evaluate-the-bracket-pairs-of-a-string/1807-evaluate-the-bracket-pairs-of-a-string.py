class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        value_of = {key: val for key, val in knowledge}

        result = []
        key_buffer = []
        in_bracket = False

        for ch in s:
            if ch == '(':
                in_bracket = True
                key_buffer = []
            elif ch == ')':
                in_bracket = False
                key = ''.join(key_buffer)
                result.append(value_of.get(key, '?'))
            elif in_bracket:
                key_buffer.append(ch)
            else:
                result.append(ch)

        return ''.join(result)