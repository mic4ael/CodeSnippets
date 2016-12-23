package pl.dmcs.ptoish.exercise1;

import java.io.*;
import java.util.Random;

class FileGenerator {
    private String filename;
    private Integer size;
    private Random random;

    public FileGenerator(String filename, Integer size) {
        this.random = new Random();
        this.filename = filename;
        this.size = size;
    }

    public void generate() {
        FileOutputStream fos = null;
        File outputFile = new File(this.filename);

        try {
            fos = new FileOutputStream(this.filename);

            while (outputFile.length() <= this.size * 1024 * 1024) {
                byte[] bytes = new byte[9999];
                this.random.nextBytes(bytes);
                fos.write(bytes);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            if (fos != null) {
                try {
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}