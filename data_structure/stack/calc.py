from stack import Stack


class Calculator:
    def __init__(self):
        self.org_exp = None  # 중위 표기법
        self.postfix_exp = None  # 후위 표기법
        self.result = None

    def set_org_exp(self, org_exp):
        self.org_exp = org_exp.replace(' ', '')
        self.postfix_exp = None
        self.result = None

    def get_org_exp(self):
        return self.org_exp

    def get_weight(self, oprt):
        if oprt == '*' or oprt == '/':
            return 9
        elif oprt == '+' or oprt == '-':
            return 7
        elif oprt == '(':
            return 5
        else:
            return -1

    def convert_to_postfix(self):
        exp_list = []
        oprt_stack = Stack()

        for ch in self.get_org_exp():
            if ch.isdigit():
                exp_list.append(ch)
                # 연산자라면
            else:
                # '(' or 스택이 비었을 때
                if oprt_stack.empty() or ch == '(':
                    oprt_stack.push(ch)
                # ')'
                elif ch == ')':
                    op = oprt_stack.pop()
                    while op != '(':
                        exp_list.append(op)
                        op = oprt_stack.pop()
                # '+', '_', '*', '/'
                elif self.get_weight(ch) > self.get_weight(oprt_stack.peek()):
                    oprt_stack.push(ch)
                else:
                    while oprt_stack and self.get_weight(ch) <= self.get_weight(oprt_stack.peek()):
                        exp_list.append(oprt_stack.pop())
                    exp_list.append(ch)
        while oprt_stack:
            exp_list.append(oprt_stack.pop())

        self.postfix_exp = ''.join(exp_list)

    def get_postfix_exp(self):
        if not self.postfix_exp:
            self.convert_to_postfix()
        return self.postfix_exp

    def calc_two_pord(self, oprd1, oprd2, oprt):
        if oprt == '+':
            return oprd1 + oprd2
        elif oprt == '-':
            return oprd1 - oprd2
        elif oprt == '*':
            return oprd1 * oprd2
        elif oprt == '/':
            return oprd1 // oprd2

    def calculate(self):
        pass

    def get_result(self):
        if not self.result:
            self.calculate()
        return self.result


if __name__ == '__main__':
    calc = Calculator()

    while 1:
        exp = input("수식을 입력하세요(종료 : 0) : ")
        if exp == '0':
            break
        calc.set_org_exp(exp)
        print(calc.get_postfix_exp())
        print("{exp} = {result}".format(
            exp=calc.get_postfix_exp(),
            result=calc.get_result()
        )
        )
