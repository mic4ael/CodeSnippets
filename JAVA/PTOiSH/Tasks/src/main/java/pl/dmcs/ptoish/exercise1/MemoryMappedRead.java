package pl.dmcs.ptoish.exercise1;

import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.MappedByteBuffer;
import pl.dmcs.ptoish.benchmarking.*;

@BenchmarkClass(description="Testing file read via mapping it into memory")
public class MemoryMappedRead {
    static int MB = 1024 * 1024;

    public MemoryMappedRead() {}

    @BenchmarkMethod(numberOfIterations=5, arguments={"random_data.txt"})
    public static void read(String filename) {
        RandomAccessFile file = null;
        MappedByteBuffer byteBuffer = null;

        try {
            file = new RandomAccessFile(filename, "r");
            byteBuffer = file.getChannel().map(FileChannel.MapMode.READ_ONLY, 0, file.length());

            while (byteBuffer.hasRemaining()) {
                if (byteBuffer.remaining() < MemoryMappedRead.MB) {
                    byteBuffer.get(new byte[byteBuffer.remaining()]);
                } else {
                    byteBuffer.get(new byte[MemoryMappedRead.MB]);
                }
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            try {
                if (byteBuffer != null) {
                    byteBuffer.clear();
                }

                if (file != null) {
                    file.close();
                }
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }
}