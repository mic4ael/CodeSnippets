package pl.dmcs.ptoish.exercise1;

import pl.dmcs.ptoish.benchmarking.BenchmarkRunner;

public class Exercise1b {
    private static String filename = "random_data.txt";

    public static void main(String []args) {
        BenchmarkRunner benchmarkRunner = new BenchmarkRunner("pl.dmcs.ptoish.exercise1");
        FileGenerator generatedFile = new FileGenerator(Exercise1b.filename, 500);

        System.out.println("Generating a file with random data");
        generatedFile.generate();
        warmUp();
        System.out.println();
        benchmarkRunner.runBenchmarks();
    }

    private static void warmUp() {
        BufferedRead.read(Exercise1b.filename);
        MemoryMappedRead.read(Exercise1b.filename);
        ChannelBufferRead.read(Exercise1b.filename);
    }
}