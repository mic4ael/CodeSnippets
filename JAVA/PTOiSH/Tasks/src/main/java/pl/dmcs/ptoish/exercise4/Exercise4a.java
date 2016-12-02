package pl.dmcs.ptoish.exercise4;


public class Exercise4a {
    public static void main(String []args) {
        Testable firstTestableObject = (Testable) ProxyFactory.newInstance(new Test1());
        firstTestableObject.test();
        Testable secondTestableObject = (Testable) ProxyFactory.newInstance(new Test2());
        secondTestableObject.test();
    }
}