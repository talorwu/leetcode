"""
思路：1.直接处理：（1）.如果栈中元素可以计算，先出栈并计算，（2）.否则，肯定s字符串没有处理完，先处理s,如果s[i]是digit，则连续读取数字变成int，如果栈顶是'('，直接进站
                  否则出栈计算再进栈，（3）. 如果s[i]是'(-+'直接进站，（4）. 如果s[i]是'('，如果栈的倒数第二个是'('则删除stack[-2]
      2.遇到 '(' 就把之前的结果和符号push进stack. 遇到')'就把 当前结果*stack中的符号 再加上stack中之前的结果. 
      3.转化为逆波兰表达式在求解
    public class Solution {  
        // "1 + 1"  
        public int calculate(String s) {  
            if(s==null || s.length() == 0) return 0;  
              
            Stack<Integer> stack = new Stack<Integer>();  
            int res = 0;  
            int sign = 1;  
            for(int i=0; i<s.length(); i++) {  
                char c = s.charAt(i);  
                if(Character.isDigit(c)) {  
                    int cur = c-'0';  
                    while(i+1<s.length() && Character.isDigit(s.charAt(i+1))) {  
                        cur = 10*cur + s.charAt(++i) - '0';  
                    }  
                    res += sign * cur;  
                } else if(c=='-') {  
                    sign = -1;  
                } else if(c=='+') {  
                    sign = 1;  
                } else if( c=='(') {  
                    stack.push(res);  
                    res = 0;  
                    stack.push(sign);  
                    sign = 1;  
                } else if(c==')') {  
                    res = stack.pop() * res + stack.pop();  
                    sign = 1;  
                }  
            }  
            return res;  
        }  
    }  



"""
import types
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ","")
        stack = [0]
        i = 0
        nums = '0123456789'
        while stack:
            #print stack
		#栈中元素可计算
            if len(stack) >= 4 and type(stack[-1]) is types.IntType and stack[-2] in '+-' and type(stack[-3]) is types.IntType:
                num2 = stack.pop()
                sign = stack.pop()
                num1 = stack.pop()
                #print num2,sign,num1
                newnum = 0
                if sign == '+':newnum = num1 + num2
                else: newnum = num1 - num2
                # if stack[-1] == '(':
                #     stack.pop()
                stack.append(newnum)
                continue
            if i < len(s) and s[i] in nums:
                tmp = 0
                while i< len(s) and s[i] in nums:
                    tmp = tmp*10+int(s[i])
                    i+=1
                if len(stack)<2 or stack[-1] == '(':
                    stack.append(tmp)
                else:
                    sign = stack.pop()
                    prenum = stack.pop()
                    newnum = 0
                    if sign == '+':newnum = prenum + tmp
                    else: newnum = prenum - tmp
                    stack.append(newnum)
            elif i<len(s) and s[i] in '(+-':
                stack.append(s[i])
                i+=1
            elif i< len(s):
                if stack[-2] == '(':
                    stack.pop(-2)
                i+=1
            else:
                if len(stack) <= 2:
                    return stack[-1]
                num2 = stack.pop()
                sign = stack.pop()
                num1 = stack.pop()
                newnum = 0
                if sign == '+':newnum = num1 + num2
                else: newnum = num1 - num2
                if stack[-1] == '(':
                    stack.pop()
                stack.append(newnum)
         
                    
                    
                    
                    
                
