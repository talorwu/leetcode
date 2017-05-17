

"""
tow stacks
"""
class MinStack {
private:
    stack<int> s1;
    stack<int> s2;
public:
    void push(int x) {
	    s1.push(x);
	    if (s2.empty() || x <= getMin())  s2.push(x);	    
    }
    void pop() {
	    if (s1.top() == getMin())  s2.pop();
	    s1.pop();
    }
    int top() {
	    return s1.top();
    }
    int getMin() {
	    return s2.top();
    }
};

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minIndex = -1
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.minIndex == -1:self.minIndex = 0
        else:
            if self.stack[self.minIndex] > x:
                self.minIndex = len(self.stack)-1

    def pop(self):
        """
        :rtype: void
        """
        r = self.stack.pop()
        if len(self.stack) == 0:
            self.minIndex = -1
            return r
        if self.minIndex == len(self.stack):
            self.minIndex = 0
            for i in range(1,len(self.stack)):
                if self.stack[self.minIndex] > self.stack[i]:
                    self.minIndex = i
            return r
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.minIndex]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
