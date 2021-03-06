package pl.dmcs.ptoish.benchmarking;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.lang.reflect.*;
import java.text.DecimalFormat;
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
                        BufferedWriter writer = null;
                        try {
                            if (benchmarkMethodAnnotation.logfile() != null && !"".equals(benchmarkMethodAnnotation.logfile())) {
                                writer = new BufferedWriter(new FileWriter(benchmarkMethodAnnotation.logfile()));
                            }
                        } catch (Exception ex) {}

                        try {
                            long totalTime = 0;
                            DecimalFormat df = new DecimalFormat("#0.000000000");
                            System.out.println("Running " + klass.getName() + "." + method.getName());
                            Method setupMethod = null;

                            if (benchmarkMethodAnnotation.setupMethod() != null && !"".equals(benchmarkMethodAnnotation.setupMethod())) {
                                setupMethod = klass.getDeclaredMethod(benchmarkMethodAnnotation.setupMethod());
                                setupMethod.setAccessible(true);
                            }
                            
                            for (int i = 0; i < benchmarkMethodAnnotation.numberOfIterations(); ++i) {
                                long start = System.nanoTime();
                                if (setupMethod != null && Modifier.isStatic(setupMethod.getModifiers())) {
                                    setupMethod.invoke(null);
                                }

                                if (Modifier.isStatic(method.getModifiers())) {
                                    method.invoke(null, (Object[]) benchmarkMethodAnnotation.arguments());
                                } else {
                                    method.invoke(klass.newInstance(), (Object[]) benchmarkMethodAnnotation.arguments());
                                }

                                long end = System.nanoTime() - start;
                                String message = "Iteration #" + (i + 1) + ", it took: " + df.format((double) (end / 1000000000.0)) + "s";
                                if (writer != null) {
                                    writer.write(message + System.lineSeparator());
                                }

                                System.out.print("\033[2K");
                                System.out.print("\r" + message);
                                totalTime += end;
                            }

                            System.out.println();
                            System.out.println("Average time: " + (df.format(totalTime / 1000000000.0 / benchmarkMethodAnnotation.numberOfIterations())) + "s");
                        } catch (Exception ex) {
                            ex.printStackTrace();
                        } finally {
                            try {
                                if (writer != null) {
                                    writer.close();
                                }
                            } catch (Exception ex) {}
                        }
                        
                        System.out.println();
                    }
                }
            }
        }
    }
 }