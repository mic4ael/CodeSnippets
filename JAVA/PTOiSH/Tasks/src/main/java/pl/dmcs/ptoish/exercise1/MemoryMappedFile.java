package pl.dmcs.ptoish.exercise1;

import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.MappedByteBuffer;

class MemoryMappedRead {
    static int MB = 1024 * 1024;

    public static void read(String filename) {
        RandomAccessFile file = null;
        MappedByteBuffer byteBuffer = null;

        try {
            file = new RandomAccessFile(filename, "r");
            byteBuffer = file.getChannel().map(FileChannel.MapMode.READ_ONLY, 0, file.length());

            System.out.println("Reading memory mapped file");
            while (byteBuffer.hasRemaining()) {
                if (byteBuffer.remaining() < MemoryMappedRead.MB) {
                    byteBuffer.get(new byte[byteBuffer.remaining()]);
                } else {
                    byteBuffer.get(new byte[MemoryMappedRead.MB]);
                }
            }
            System.out.println("Finished");
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