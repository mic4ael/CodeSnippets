package pl.dmcs.ptoish.exercise1;

import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.MappedByteBuffer;
import pl.dmcs.ptoish.benchmarking.*;

@BenchmarkClass(description="Testing file read via NIO channels/buffers")
public class ChannelBufferRead {
    static int MB = 1024 * 1024;

    public ChannelBufferRead() {}

    @BenchmarkMethod(numberOfIterations=5, arguments={"random_data.txt"})
    public static void read(String filename) {
        RandomAccessFile file = null;
        FileChannel fileChannel = null;
        ByteBuffer byteBuffer  = null;

        try {
            file = new RandomAccessFile(filename, "r");
            fileChannel = file.getChannel();
            byteBuffer = ByteBuffer.allocate(ChannelBufferRead.MB);

            while (fileChannel.read(byteBuffer) > 0) {
                byteBuffer = ByteBuffer.allocate(ChannelBufferRead.MB);
                byteBuffer.clear();
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            try {
                if (file != null) {
                    file.close();
                }
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }
}