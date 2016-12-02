package pl.dmcs.ptoish.exercise4;

import pl.dmcs.ptoish.exercise4.TestableInvocationHandler;

import java.lang.reflect.Proxy;


public class ProxyFactory {
    public static Object newInstance(Object object) {
        return Proxy.newProxyInstance(object.getClass().getClassLoader(), new Class<?>[] {Testable.class}, 
                                      new TestableInvocationHandler(object));
    }
}