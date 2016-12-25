package pl.dmcs.ptoish.exercise2.queuesandlists;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Random;
import java.util.Iterator;

import pl.dmcs.ptoish.benchmarking.BenchmarkClass;
import pl.dmcs.ptoish.benchmarking.BenchmarkMethod;


@BenchmarkClass(description="Testing Deque")
public class ArrayDequeBenchmarks {
    private static Queue<Integer> deque1000 = new ArrayDeque<>();
    private static Queue<Integer> deque10000 = new ArrayDeque<>();
    private static Queue<Integer> deque1000000 = new ArrayDeque<>();

    private static void initDeque1000() {
        Random r = new Random();
        deque1000 = new ArrayDeque<>();
        for (int i = 0; i <= 1000; ++i) {
            deque1000.add(r.nextInt());
        }
    }

    private static void initDeque10000() {
        Random r = new Random();
        deque10000 = new ArrayDeque<>();
        for (int i = 0; i <= 10000; ++i) {
            deque10000.add(r.nextInt());
        }
    }

    private static void initDeque1000000() {
        Random r = new Random();
        deque1000000 = new ArrayDeque<>();
        for (int i = 0; i <= 1000000; ++i) {
            deque1000000.add(r.nextInt());
        }
    }

    @BenchmarkMethod(logfile="add_at_the_beginning_array_deque1000.txt", setupMethod="initDeque1000", numberOfIterations=1)
    public static void addAtTheBeginningdeque1000() {
        deque1000.add(1);
    }

    @BenchmarkMethod(logfile="add_at_the_beginning_array_deque10000.txt", setupMethod="initDeque10000", numberOfIterations=1)
    public static void addAtTheBeginningdeque10000() {
        deque10000.add(10);
    }

    @BenchmarkMethod(logfile="add_at_the_beginning_array_deque1000000.txt", setupMethod="initDeque1000000", numberOfIterations=1)
    public static void addAtTheBeginningdeque1000000() {
        deque1000000.add(10);
    }

    @BenchmarkMethod(logfile="remove_from_the_beginning_of_the_array_deque1000.txt", setupMethod="initDeque1000", numberOfIterations=1)
    public static void removeFromBeginningOfThedeque1000() {
        deque1000.remove();
    }

    @BenchmarkMethod(logfile="remove_from_the_beginning_of_the_array_deque10000.txt", setupMethod="initDeque10000", numberOfIterations=1)
    public static void removeFromBeginningOfThedeque10000() {
        deque10000.remove();
    }

    @BenchmarkMethod(logfile="remove_from_the_beginning_of_the_array_deque1000000.txt", setupMethod="initDeque1000000", numberOfIterations=1)
    public static void removeFromBeginningOfThedeque1000000() {
        deque1000000.remove();
    }

    @BenchmarkMethod(logfile="browsing_using_iterator_array_deque1000.txt", setupMethod="initDeque1000", numberOfIterations=1)
    public static void browsingUsingIteratordeque1000() {
        Iterator<?> it = deque1000.iterator();
        while (it.hasNext()) {
            it.next();
        }
    }

    @BenchmarkMethod(logfile="browsing_using_iterator_array_deque10000.txt", setupMethod="initDeque10000", numberOfIterations=1)
    public static void browsingUsingIteratordeque10000() {
        Iterator<?> it = deque10000.iterator();
        while (it.hasNext()) {
            it.next();
        }
    }

    @BenchmarkMethod(logfile="browsing_using_iterator_array_deque1000000.txt", setupMethod="initDeque1000000", numberOfIterations=1)
    public static void browsingUsingIteratordeque1000000() {
        Iterator<?> it = deque1000000.iterator();
        while (it.hasNext()) {
            it.next();
        }
    }
}