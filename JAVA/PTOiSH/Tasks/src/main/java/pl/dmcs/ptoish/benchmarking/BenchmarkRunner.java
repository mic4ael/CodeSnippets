package pl.dmcs.ptoish.benchmarking;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.lang.reflect.*;
import java.text.DecimalFormat;
import java.util.*;

import javax.swing.filechooser.FileNameExtensionFilter;


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
                            DecimalFormat df = new DecimalFormat();
                            df.setMaximumFractionDigits(5);
                            df.setMinimumFractionDigits(3);
                            for (int i = 0; i < benchmarkMethodAnnotation.numberOfIterations(); ++i) {
                                long start = System.currentTimeMillis();
                                if (Modifier.isStatic(method.getModifiers())) {
                                    method.invoke(null, (Object[]) benchmarkMethodAnnotation.arguments());
                                } else {
                                    method.invoke(klass.newInstance(), (Object[]) benchmarkMethodAnnotation.arguments());
                                }
                                long end = System.currentTimeMillis() - start;
                                String message = "Iteration #" + (i + 1) + ", it took: " + (df.format(end / 1000.0)) + "s";
                                if (writer != null) {
                                    writer.write(message + System.lineSeparator());
                                }

                                System.out.print("\033[2K");
                                System.out.print(message + "\r");
                                totalTime += end;
                            }

                            System.out.println();
                            System.out.println("Average time: " + (totalTime / benchmarkMethodAnnotation.numberOfIterations() / 1000.0) + "s");
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