package pl.dmcs.ptoish.exercise2.queuesandlists;

import java.util.*;

import pl.dmcs.ptoish.benchmarking.BenchmarkClass;
import pl.dmcs.ptoish.benchmarking.BenchmarkMethod;


@BenchmarkClass(description="Testing ArrayList")
public class ArrayListBenchmarks {
    private static List<Integer> list1000 = new ArrayList<>();
    private static List<Integer> list10000 = new ArrayList<>();
    private static List<Integer> list1000000 = new ArrayList<>();

    private static void initList1000() {
        Random r = new Random();
        list1000 = new ArrayList<>();
        for (int i = 0; i <= 1000; ++i) {
            list1000.add(r.nextInt());
        }
    }

    private static void initList10000() {
        Random r = new Random();
        list10000 = new ArrayList<>();
        for (int i = 0; i <= 10000; ++i) {
            list10000.add(r.nextInt());
        }
    }

    private static void initList1000000() {
        Random r = new Random();
        list1000000 = new ArrayList<>();
        for (int i = 0; i <= 1000000; ++i) {
            list1000000.add(r.nextInt());
        }
    }

    @BenchmarkMethod(logfile="add_at_the_beginning_array_list1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void addAtTheBeginningList1000() {
        list1000.add(0, 10);
    }

    @BenchmarkMethod(logfile="add_at_the_beginning_array_list10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void addAtTheBeginningList10000() {
        list10000.add(0, 10);
    }

    @BenchmarkMethod(logfile="add_at_the_beginning_array_list1000000.txt", setupMethod="initList1000000", numberOfIterations=1)
    public static void addAtTheBeginningList1000000() {
        list1000000.add(0, 10);
    }

    @BenchmarkMethod(logfile="add_at_the_end_array_list1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void addAtTheEndList1000() {
        list1000.add(list1000.size(), 10);
    }

    @BenchmarkMethod(logfile="add_at_the_end_array_list10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void addAtTheEndList10000() {
        list10000.add(list10000.size(), 10);
    }

    @BenchmarkMethod(logfile="add_at_the_end_array_list1000000.txt", setupMethod="initList1000000", numberOfIterations=1)
    public static void addAtTheEndList1000000() {
        list1000000.add(list1000000.size(), 10);
    }

    @BenchmarkMethod(logfile="add_at_random_place_array_list1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void addAtRandomPlaceList1000() {
        list1000.add(453, 10);
    }

    @BenchmarkMethod(logfile="add_at_random_place_array_list10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void addAtRandomPlaceList10000() {
        list10000.add(4567, 10);
    }

    @BenchmarkMethod(logfile="add_at_random_place_array_list1000000.txt", setupMethod="initList1000000", numberOfIterations=1)
    public static void addAtRandomPlaceList1000000() {
        list1000000.add(987653, 10);
    }
    
    @BenchmarkMethod(logfile="remove_from_the_beginning_of_the_array_list1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void removeFromBeginningOfTheList1000() {
        list1000.remove(0);
    }

    @BenchmarkMethod(logfile="remove_from_the_beginning_of_the_array_list10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void removeFromBeginningOfTheList10000() {
        list10000.remove(0);
    }

    @BenchmarkMethod(logfile="remove_from_the_beginning_of_the_array_list1000000.txt", setupMethod="initList1000000", numberOfIterations=1)
    public static void removeFromBeginningOfTheList1000000() {
        list1000000.remove(0);
    }

    @BenchmarkMethod(logfile="remove_from_the_end_of_the_array_list1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void removeFromEndOfTheList1000() {
        list1000.remove(list1000.size() - 1);
    }

    @BenchmarkMethod(logfile="remove_from_the_end_of_the_array_list10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void removeFromEndOfTheList10000() {
        list10000.remove(list10000.size() - 1);
    }

    @BenchmarkMethod(logfile="remove_from_the_end_of_the_array_list1000000.txt", setupMethod="initList1000000", numberOfIterations=1)
    public static void removeFromEndOfTheList1000000() {
        list1000000.remove(list1000000.size() - 1);
    }

    @BenchmarkMethod(logfile="remove_random_place_in_the_array_list1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void removeFromRandomPlaceInTheList1000() {
        list1000.remove(454);
    }

    @BenchmarkMethod(logfile="remove_random_place_in_the_array_list10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void removeFromRandomPlaceInTheList10000() {
        list10000.remove(4565);
    }

    @BenchmarkMethod(logfile="remove_random_place_in_the_array_list1000000.txt", setupMethod="initList1000000", numberOfIterations=1)
    public static void removeFromRandomPlaceInTheList1000000() {
        list1000000.remove(123123);
    }

    @BenchmarkMethod(logfile="browsing_using_indexes_array_list1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void browsingUsingIndexesList1000() {
        for (int i = 0; i < list1000.size(); i++) {
            list1000.get(i);
        }
    }

    @BenchmarkMethod(logfile="browsing_using_indexes_array_list10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void browsingUsingIndexesList10000() {
        for (int i = 0; i < list10000.size(); i++) {
            list10000.get(i);
        }
    }

    @BenchmarkMethod(logfile="browsing_using_indexes_array_list1000000.txt", setupMethod="initList1000000", numberOfIterations=1)
    public static void browsingUsingIndexesList1000000() {
        for (int i = 0; i < list1000000.size(); i++) {
            list1000000.get(i);
        }
    }

    @BenchmarkMethod(logfile="browsing_using_iterator_array_list1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void browsingUsingIteratorList1000() {
        Iterator<?> it = list1000.iterator();
        while (it.hasNext()) {
            it.next();
        }
    }

    @BenchmarkMethod(logfile="browsing_using_iterator_array_list10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void browsingUsingIteratorList10000() {
        Iterator<?> it = list10000.iterator();
        while (it.hasNext()) {
            it.next();
        }
    }

    @BenchmarkMethod(logfile="browsing_using_iterator_array_list1000000.txt", setupMethod="initList1000000", numberOfIterations=1)
    public static void browsingUsingIteratorList1000000() {
        Iterator<?> it = list1000000.iterator();
        while (it.hasNext()) {
            it.next();
        }
    }
}