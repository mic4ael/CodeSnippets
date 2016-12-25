package pl.dmcs.ptoish.exercise3;

import pl.dmcs.ptoish.benchmarking.BenchmarkClass;
import pl.dmcs.ptoish.benchmarking.BenchmarkMethod;


@BenchmarkClass(description="Testing a cache implementation using HashMap")
public class HashMapCacheBenchmark {
    private static HashMapCache cache = HashMapCache.getInstance();

    @BenchmarkMethod(numberOfIterations=1000, logfile="cache_put.txt")
    public static void writingToCacheBenchmar() {
        cache.put("test", 123456);
    }

    @BenchmarkMethod(numberOfIterations=1000, logfile="cache_read.txt")
    public static void readingFromCacheBenchmark() {
        cache.get("test");
    }


    @BenchmarkMethod(numberOfIterations=1000, logfile="cache_delete.txt")
    public static void removingKeyFromCacheBenchmark() {
        cache.clear("test");
    }
}