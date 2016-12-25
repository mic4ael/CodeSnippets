package pl.dmcs.ptoish.exercise2.sets;

import java.util.Random;
import java.util.Set;
import java.util.HashSet;

import pl.dmcs.ptoish.benchmarking.BenchmarkClass;
import pl.dmcs.ptoish.benchmarking.BenchmarkMethod;


@BenchmarkClass(description="Benchmarks on HashSet collection")
public class HashSetBenchmark {
    private static Set<Integer> set10 = new HashSet<>();
    private static Set<Integer> set100 = new HashSet<>();
    private static Set<Integer> set1000 = new HashSet<>();
    private static Set<Integer> set10000 = new HashSet<>();
    private static Set<Integer> set10000000 = new HashSet<>();

    static {
        Random r = new Random();
        for (int i = 0; i <= 10000000; ++i) {
            set10000000.add(r.nextInt());

            if (i < 10) {
                set10.add(r.nextInt());
            }

            if (i < 100) {
                set100.add(r.nextInt());
            }

            if (i < 1000) {
                set1000.add(r.nextInt());
            }

            if (i < 10000) {
                set10000.add(r.nextInt());
            }
        }
    }

    @BenchmarkMethod(logfile="add_to_hash_set10.txt", numberOfIterations=10000)
    public static void addToSet10() {
        set10.add(999999);
    }

    @BenchmarkMethod(logfile="add_to_hash_set100.txt", numberOfIterations=10000)
    public static void addToSet100() {
        set100.add(999999);
    }

    @BenchmarkMethod(logfile="add_to_hash_set1000.txt", numberOfIterations=10000)
    public static void addToSet1000() {
        set1000.add(999999);
    }

    @BenchmarkMethod(logfile="add_to_hash_set10000.txt", numberOfIterations=10000)
    public static void addToSet10000() {
        set10000.add(999999);
    }

    @BenchmarkMethod(logfile="add_to_hash_set10000000.txt", numberOfIterations=10000)
    public static void addToset10000000() {
        set10000000.add(999999);
    }

    @BenchmarkMethod(logfile="remove_from_hash_set10.txt", numberOfIterations=10000)
    public static void removeFromSet10() {
        set10.remove(5);
    }

    @BenchmarkMethod(logfile="remove_from_hash_set100.txt", numberOfIterations=10000)
    public static void removeFromSet100() {
        set100.remove(55);
    }

    @BenchmarkMethod(logfile="remove_from_hash_set1000.txt", numberOfIterations=10000)
    public static void removeFromSet1000() {
        set1000.remove(576);
    }

    @BenchmarkMethod(logfile="remove_from_hash_set10000.txt", numberOfIterations=10000)
    public static void removeFromSet10000() {
        set10000.remove(8888);
    }

    @BenchmarkMethod(logfile="remove_from_hash_set10000000.txt", numberOfIterations=10000)
    public static void removeFromset10000000() {
        set10000000.remove(87654);
    }

    @BenchmarkMethod(logfile="get_element_from_hash_set10.txt", numberOfIterations=10000)
    public static void getElementFromSet10() {
        set10.iterator().next();
    }

    @BenchmarkMethod(logfile="get_element_from_hash_set100.txt", numberOfIterations=10000)
    public static void getElementFromSet100() {
        set100.iterator().next();
    }

    @BenchmarkMethod(logfile="get_element_from_hash_set1000.txt", numberOfIterations=10000)
    public static void getElementFromSet1000() {
        set1000.iterator().next();
    }

    @BenchmarkMethod(logfile="get_element_from_hash_set10000.txt", numberOfIterations=10000)
    public static void getElementFromSet10000() {
        set10000.iterator().next();
    }

    @BenchmarkMethod(logfile="get_element_from_hash_set10000000.txt", numberOfIterations=10000)
    public static void getElementFromset10000000() {
        set10000000.iterator().next();
    }

    @BenchmarkMethod(logfile="check_if_exists_has_set10.txt", numberOfIterations=10000)
    public static void checkIfExistsInSet10() {
        set10.contains(5);
    }

    @BenchmarkMethod(logfile="check_if_exists_has_set100.txt", numberOfIterations=10000)
    public static void checkIfExistsInSet100() {
        set100.contains(55);
    }

    @BenchmarkMethod(logfile="check_if_exists_has_set1000.txt", numberOfIterations=10000)
    public static void checkIfExistsInSet1000() {
        set1000.contains(666);
    }

    @BenchmarkMethod(logfile="check_if_exists_has_set10000.txt", numberOfIterations=10000)
    public static void checkIfExistsInSet10000() {
        set10000.contains(7665);
    }

    @BenchmarkMethod(logfile="check_if_exists_has_set10000000.txt", numberOfIterations=10000)
    public static void checkIfExistsInset10000000() {
        set10000000.contains(87878);
    }
}