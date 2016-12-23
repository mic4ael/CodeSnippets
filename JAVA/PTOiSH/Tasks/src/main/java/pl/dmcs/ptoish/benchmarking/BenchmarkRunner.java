package pl.dmcs.ptoish.benchmarking;

import java.lang.annotation.Annotation;
import java.lang.reflect.*;
import java.util.*;
import pl.dmcs.ptoish.ClassFinder;


public class BenchmarkRunner {
    private String packageName;

    public BenchmarkRunner(String packageName) {
        this.packageName = packageName;
    }

    public void runBenchmarks() {
        List<Class<?>> packageClasses = ClassFinder.find(this.packageName);

        for (Class<?> klass : packageClasses) {
            if (klass.isAnnotationPresent(BenchmarkClass.class)) {
                BenchmarkClass benchmarkClassAnnotation = (BenchmarkClass) klass.getAnnotation(BenchmarkClass.class);
                System.out.println("Processing " + klass.getName());
                System.out.println(benchmarkClassAnnotation.description());

                for (Method method : klass.getDeclaredMethods()) {
                    if (method.isAnnotationPresent(BenchmarkMethod.class)) {
                        BenchmarkMethod benchmarkMethodAnnotation = (BenchmarkMethod) method.getAnnotation(BenchmarkMethod.class);
                        try {
                            long totalTime = 0;

                            for (int i = 0; i < benchmarkMethodAnnotation.numberOfIterations(); ++i) {
                                long start = System.currentTimeMillis();
                                if (Modifier.isStatic(method.getModifiers())) {
                                    method.invoke(null, (Object[]) benchmarkMethodAnnotation.arguments());
                                } else {
                                    method.invoke(klass.newInstance(), (Object[]) benchmarkMethodAnnotation.arguments());
                                }
                                long end = System.currentTimeMillis() - start;
                                System.out.println("Iteration #" + (i + 1) + ", it took: " + (end / 1000.0) + "s");
                                totalTime += end;
                            }

                            System.out.println("Average time: " + (totalTime / benchmarkMethodAnnotation.numberOfIterations() / 1000.0) + "s");
                        } catch (Exception ex) {
                            ex.printStackTrace();
                        }
                        
                        System.out.println();
                    }
                }
            }
        }
    }
 }