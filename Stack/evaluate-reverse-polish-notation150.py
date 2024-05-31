''' You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6 '''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in '+-/*': stack.append(int(i))
            
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                
                if i == "/":
                    stack.append(int(v2/v1))
                if i == "*":
                    stack.append(v2*v1)
                if i == "+":
                    stack.append(v2+v1)
                if i == "-":
                    stack.append(v2-v1)

        return stack[0]
