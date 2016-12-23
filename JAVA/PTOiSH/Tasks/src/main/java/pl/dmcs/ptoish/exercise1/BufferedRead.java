package pl.dmcs.ptoish.exercise1;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import pl.dmcs.ptoish.benchmarking.*;

@BenchmarkClass(description="Testing file read via buffered input stream")
public class BufferedRead {
    static int MB = 1024 * 1024;

    public BufferedRead() {}

    @BenchmarkMethod(numberOfIterations=5, arguments={"random_data.txt"})
    public static void read(String filename) {
        BufferedInputStream bis = null;
        FileInputStream fis = null;
        int available = 0;

        try {
            fis = new FileInputStream(new File(filename));
            bis = new BufferedInputStream(fis);

            while ((available = bis.available()) > 0) {
                if (available < BufferedRead.MB) {
                    bis.read(new byte[available], 0, available);
                } else {
                    bis.read(new byte[BufferedRead.MB], 0, BufferedRead.MB);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (fis != null) {
                    fis.close();
                }
                
                if (bis != null) {
                    bis.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}