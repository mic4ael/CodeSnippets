package pl.dmcs.ptoish.exercise1;

import java.io.*;

public class Exercise1a {
    public static void main(String []args) {
        serializePerson();
        readSerializedPerson();
        externalizePerson();
        compareFileSize();
    }

    public static void serializePerson() {
        Person person = new Person("Michał", "Kołodziejski", new java.util.Date(), 24);
        FileOutputStream fout = null;
        ObjectOutputStream oos = null;

        try {
            fout = new FileOutputStream("person.ser");
            oos = new ObjectOutputStream(fout);
            oos.writeObject(person);
            System.out.println("Person object has been serialized");
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            if (fout != null) {
                try {
                    fout.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            if (oos != null) {
                try {
                    oos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void readSerializedPerson() {
        FileInputStream fin = null;
        ObjectInputStream ois = null;

        try {
            fin = new FileInputStream("person.ser");
            ois = new ObjectInputStream(fin);
            Person unserializedPerson = (Person) ois.readObject();

            System.out.println("Serialized Person's firstname: " + unserializedPerson.getFirstName());
            System.out.println("Serialized Person's lastName: " + unserializedPerson.getLastName());
            System.out.println("Serialized Person's age: " + unserializedPerson.getAge());
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            if (fin != null) {
                try {
                    fin.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            if (ois != null) {
                try {
                    ois.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void externalizePerson() {
        ExternalizablePerson person = new ExternalizablePerson("Michał", "Kołodziejski", new java.util.Date(), 24);
        FileOutputStream fout = null;
        ObjectOutputStream oos = null;

        try {
            fout = new FileOutputStream("person.ext");
            oos = new ObjectOutputStream(fout);
            oos.writeObject(person);
            System.out.println("Person object has been externalized");
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            if (fout != null) {
                try {
                    fout.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            if (oos != null) {
                try {
                    oos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void compareFileSize() {
        File serializedFile = new File("person.ser");
        File externalizedFile = new File("person.ext");

        System.out.println("Serialized file has " + serializedFile.length() + " bytes");
        System.out.println("Externalized file has " + externalizedFile.length() + " bytes");
    }
}