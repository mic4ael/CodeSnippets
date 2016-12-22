package pl.dmcs.ptoish.exercise3;

public class Test implements Testable {
    private String privateField = "privateField";
    public String publicField = "publicField";

    public void test() {
        System.out.println("Test::test()");
    }
}