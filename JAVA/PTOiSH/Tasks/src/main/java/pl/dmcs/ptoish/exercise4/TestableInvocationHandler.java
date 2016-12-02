package pl.dmcs.ptoish.exercise4;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;


public class TestableInvocationHandler implements InvocationHandler {
    private Object testableObject;

    public TestableInvocationHandler(Object testableObject) {
        this.testableObject = testableObject;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        Object result;
        try {
            result = method.invoke(this.testableObject, args);
        } catch (InvocationTargetException ex) {
            System.err.println("An error occurred while invoking method: " + ex.getMessage());
            throw ex;
        } catch (Exception ex) {
            System.err.println("An error occurred: " + ex.getMessage());
            throw ex;
        }

        return result;
    }
}