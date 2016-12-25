package pl.dmcs.ptoish.exercise2.queuesandlists;

import java.util.*;

import pl.dmcs.ptoish.benchmarking.BenchmarkClass;
import pl.dmcs.ptoish.benchmarking.BenchmarkMethod;;



@BenchmarkClass(description="Testing LinkedList")
public class LinkedListBenchmarks {
    private static List<Integer> list1000 = new LinkedList<>();
    private static List<Integer> list10000 = new LinkedList<>();
    private static List<Integer> list100000 = new LinkedList<>();

    private static void initList1000() {
        Random r = new Random();
        list1000 = new LinkedList<>();
        for (int i = 0; i <= 1000; ++i) {
            list1000.add(r.nextInt());
        }
    }

    private static void initList10000() {
        Random r = new Random();
        list10000 = new LinkedList<>();
        for (int i = 0; i <= 10000; ++i) {
            list10000.add(r.nextInt());
        }
    }

    private static void initList100000() {
        Random r = new Random();
        list100000 = new LinkedList<>();
        for (int i = 0; i <= 100000; ++i) {
            list100000.add(r.nextInt());
        }
    }

    @BenchmarkMethod(logfile="add_at_the_beginning_linked_list_1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void addAtTheBeginningList1000() {
        list1000.add(0, 10);
    }

    @BenchmarkMethod(logfile="add_at_the_beginning_linked_list_10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void addAtTheBeginningList10000() {
        list10000.add(0, 10);
    }

    @BenchmarkMethod(logfile="add_at_the_beginning_linked_list_100000.txt", setupMethod="initList100000", numberOfIterations=1)
    public static void addAtTheBeginningList100000() {
        list100000.add(0, 10);
    }

    @BenchmarkMethod(logfile="add_at_the_end_linked_list_1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void addAtTheEndList1000() {
        list1000.add(list1000.size(), 10);
    }

    @BenchmarkMethod(logfile="add_at_the_end_linked_list_10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void addAtTheEndList10000() {
        list10000.add(list10000.size(), 10);
    }

    @BenchmarkMethod(logfile="add_at_the_end_linked_list_100000.txt", setupMethod="initList100000", numberOfIterations=1)
    public static void addAtTheEndList100000() {
        list100000.add(list100000.size(), 10);
    }

    @BenchmarkMethod(logfile="add_at_random_place_linked_list_1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void addAtRandomPlaceList1000() {
        list1000.add(453, 10);
    }

    @BenchmarkMethod(logfile="add_at_random_place_linked_list_10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void addAtRandomPlaceList10000() {
        list10000.add(4567, 10);
    }

    @BenchmarkMethod(logfile="add_at_random_place_linked_list_100000.txt", setupMethod="initList100000", numberOfIterations=1)
    public static void addAtRandomPlaceList100000() {
        list100000.add(98765, 10);
    }
    
    @BenchmarkMethod(logfile="remove_from_the_beginning_of_the_linked_list_1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void removeFromBeginningOfTheList1000() {
        list1000.remove(0);
    }

    @BenchmarkMethod(logfile="remove_from_the_beginning_of_the_linked_list_10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void removeFromBeginningOfTheList10000() {
        list10000.remove(0);
    }

    @BenchmarkMethod(logfile="remove_from_the_beginning_of_the_linked_list_100000.txt", setupMethod="initList100000", numberOfIterations=1)
    public static void removeFromBeginningOfTheList100000() {
        list100000.remove(0);
    }

    @BenchmarkMethod(logfile="remove_from_the_end_of_the_linked_list_1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void removeFromEndOfTheList1000() {
        list1000.remove(list1000.size() - 1);
    }

    @BenchmarkMethod(logfile="remove_from_the_end_of_the_linked_list_10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void removeFromEndOfTheList10000() {
        list10000.remove(list10000.size() - 1);
    }

    @BenchmarkMethod(logfile="remove_from_the_end_of_the_linked_list_100000.txt", setupMethod="initList100000", numberOfIterations=1)
    public static void removeFromEndOfTheList100000() {
        list100000.remove(list100000.size() - 1);
    }

    @BenchmarkMethod(logfile="remove_random_place_in_the_linked_list_1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void removeFromRandomPlaceInTheList1000() {
        list1000.remove(454);
    }

    @BenchmarkMethod(logfile="remove_random_place_in_the_linked_list_10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void removeFromRandomPlaceInTheList10000() {
        list10000.remove(4565);
    }

    @BenchmarkMethod(logfile="remove_random_place_in_the_linked_list_100000.txt", setupMethod="initList100000", numberOfIterations=1)
    public static void removeFromRandomPlaceInTheList100000() {
        list100000.remove(12312);
    }

    @BenchmarkMethod(logfile="browsing_using_indexes_linked_list_1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void browsingUsingIndexesList1000() {
        for (int i = 0; i < list1000.size(); i++) {
            list1000.get(i);
        }
    }

    @BenchmarkMethod(logfile="browsing_using_indexes_linked_list_10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void browsingUsingIndexesList10000() {
        for (int i = 0; i < list10000.size(); i++) {
            list10000.get(i);
        }
    }

    @BenchmarkMethod(logfile="browsing_using_indexes_linked_list_100000.txt", setupMethod="initList100000", numberOfIterations=1)
    public static void browsingUsingIndexesList100000() {
        for (int i = 0; i < list100000.size(); i++) {
            list100000.get(i);
        }
    }

    @BenchmarkMethod(logfile="browsing_using_iterator_linked_list_1000.txt", setupMethod="initList1000", numberOfIterations=1)
    public static void browsingUsingIteratorList1000() {
        Iterator<?> it = list1000.iterator();
        while (it.hasNext()) {
            it.next();
        }
    }

    @BenchmarkMethod(logfile="browsing_using_iterator_linked_list_10000.txt", setupMethod="initList10000", numberOfIterations=1)
    public static void browsingUsingIteratorList10000() {
        Iterator<?> it = list10000.iterator();
        while (it.hasNext()) {
            it.next();
        }
    }

    @BenchmarkMethod(logfile="browsing_using_iterator_linked_list_100000.txt", setupMethod="initList100000", numberOfIterations=1)
    public static void browsingUsingIteratorList100000() {
        Iterator<?> it = list100000.iterator();
        while (it.hasNext()) {
            it.next();
        }
    }
}