package pl.dmcs.ptoish.exercise1;


public class Exercise1b {
    public static void main(String []args) {
        FileGenerator generatedFile = new FileGenerator("random_data.txt", 20);
        System.out.println("Generating a file with random data");
        generatedFile.generate();

        System.out.println();
        MemoryMappedRead.read("random_data.txt");
        ChannelBufferRead.read("random_data.txt");
        BufferedRead.read("random_data.txt");
    }
}