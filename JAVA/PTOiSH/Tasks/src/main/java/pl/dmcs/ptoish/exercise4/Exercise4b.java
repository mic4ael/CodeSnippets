// Write a program which allows you to observe SoftReference, WeakReference and PhantomReference in action.

package pl.dmcs.ptoish.exercise4;

import java.lang.ref.*;
import java.util.*;


class Exercise4b {
    private static void printProgress(String info) {
        System.out.print("\033[2K");
        System.out.print(info + "\r");
    }

    private static void testWeakReferences() {
        Integer weakInt = new Integer(19);
        WeakReference<Integer> weakReference = new WeakReference<Integer>(weakInt);
        String info = "Checking whether weakInt has been collected";
        String dots = ".";

        weakInt = null;
        System.out.println();
        while (weakReference.get() != null) {
            printProgress(info + dots);
            System.gc();

            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {}

            if (dots.length() == 3) {
                dots = ".";
            } else {
                dots += ".";
            }
        }

        System.out.println();
        System.out.println("Weak reference doesn't point to weakInt anymore");
    }

    private static void testSoftReferences() {
        Integer softInt = new Integer(20);
        SoftReference<Integer> softReference = new SoftReference<Integer>(softInt);
        String dots = ".";
        List<String[]> strings = new LinkedList<String[]>();
        Runtime runtime = Runtime.getRuntime();

        softInt = null;
        System.out.println();
        System.out.println("Max Memory: " + runtime.maxMemory() / (1024.0 * 1024));
        while (softReference.get() != null) {
            printProgress("\rUsed memory: " + String.valueOf((runtime.totalMemory() - runtime.freeMemory()) / (1024.0 * 1024)));
            strings.add(new String[100]);

            System.gc();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {}
        }

        System.out.println();
        System.out.println("JVM was about to run out of memory");
        System.out.println("Soft reference doesn't point to softInt anymore'");
    }

    private static void testPhantomReferences() {

    }

    public static void main(String []args) {
        String type = null;

        if (args.length > 0) {
            type = args[0];
        } else {
            System.out.println("No arguments provided!");
        }

        if ("weak".equals(type)) {
            testWeakReferences();
        } else if ("soft".equals(type)) {
            testSoftReferences();
        } else if ("phantom".equals(type)) {
            testPhantomReferences();
        }
    }
}