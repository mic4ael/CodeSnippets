package pl.dmcs.ptoish.exercise3;

import java.util.LinkedList;

import pl.dmcs.ptoish.benchmarking.BenchmarkClass;
import pl.dmcs.ptoish.benchmarking.BenchmarkMethod;


@BenchmarkClass(description="Testing a cache implementation using HashMap")
public class HashMapCacheBenchmark {
    private static HashMapCache cache = HashMapCache.getInstance();

    @BenchmarkMethod(numberOfIterations=1000, logfile="cache_put.txt")
    public static void writingToCacheBenchmar() {
        cache.put("test", 123456);
        cache.put("test1", "test");
        cache.put("test2", 2.0f);
        cache.put("test3", new Object());
        cache.put("test4", new LinkedList<Integer>());
        cache.put("test5", new Integer(15));
        cache.put("test5", new int[15]);
    }

    @BenchmarkMethod(numberOfIterations=1000, logfile="cache_read.txt")
    public static void readingFromCacheBenchmark() {
        cache.get("test");
        cache.get("test1");
        cache.get("test2");
        cache.get("test3");
        cache.get("test4");
        cache.get("test5");
    }


    @BenchmarkMethod(numberOfIterations=1000, logfile="cache_delete.txt")
    public static void removingKeyFromCacheBenchmark() {
        cache.clear("test");
        cache.clear("test1");
        cache.clear("test2");
        cache.clear("test3");
        cache.clear("test4");
        cache.clear("test5");
    }
}