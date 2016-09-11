@FunctionalInterface
interface FirstLambda {
    public void hello();
}

@FunctionalInterface
interface SecondLambda {
    public void hello(String name);
}

class Lambdas {
    private static void helloMichal(SecondLambda lambda) {
        lambda.hello("Michal");
    }

    public static void main(String args[]) {
        FirstLambda firstLambda = () -> System.out.println("Hello");
        firstLambda.hello();
        SecondLambda secondLambda = (name) -> System.out.println("Hello " + name);
        helloMichal(secondLambda);
    }
}
