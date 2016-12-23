package pl.dmcs.ptoish.exercise1;

import pl.dmcs.ptoish.benchmarking.BenchmarkRunner;

public class Exercise1b {
    public static void main(String []args) {
        BenchmarkRunner benchmarkRunner = new BenchmarkRunner("pl.dmcs.ptoish.exercise1");
        FileGenerator generatedFile = new FileGenerator("random_data.txt", 500);

        System.out.println("Generating a file with random data");
        generatedFile.generate();

        System.out.println();
        benchmarkRunner.runBenchmarks();
    }
}