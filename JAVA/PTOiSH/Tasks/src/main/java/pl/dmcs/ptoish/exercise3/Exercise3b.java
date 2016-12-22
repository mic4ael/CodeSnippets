package pl.dmcs.ptoish.exercise3;

import java.lang.reflect.*;


public class Exercise3b {
    public static void main(String []args) {
        Test test = new Test();
        Class cls = test.getClass();

        try {                
            Method method = cls.getMethod("test");
            Field privateField = cls.getDeclaredField("privateField");
            privateField.setAccessible(true);
            Field publicField = cls.getDeclaredField("publicField");
            System.out.println();
            System.out.println("Calling Test.test method using reflection");
            method.invoke(test);
            System.out.println("Getting public field value via reflection: " + publicField.get(test));
            System.out.println("Getting private field value via reflection: " + privateField.get(test));
        } catch (NoSuchMethodException e) {
            System.out.println(e.toString());
        } catch (IllegalAccessException e) {
            System.out.println(e.toString());
        } catch (InvocationTargetException e) {
            System.out.println(e.toString());
        } catch (NoSuchFieldException e) {
            System.out.println(e.toString());
        }
    }
}