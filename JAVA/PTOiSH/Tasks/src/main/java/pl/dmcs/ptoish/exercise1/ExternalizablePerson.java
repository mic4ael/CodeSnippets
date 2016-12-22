package pl.dmcs.ptoish.exercise1;

import java.io.Externalizable;
import java.io.IOException;
import java.io.ObjectOutput;
import java.io.ObjectInput;
import java.util.Date;

class ExternalizablePerson implements Externalizable {
    private String firstName;
    private String lastName;
    private Date birthday;
    private Integer age;

    public ExternalizablePerson(String firstName, String lastName, Date birthday, Integer age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthday = birthday;
        this.age = age;
    }

    public String getFirstName() {
        return this.firstName;
    }

    public String getLastName() {
        return this.lastName;
    }

    public Date getBirthday() {
        return this.birthday;
    }

    public Integer getAge() {
        return this.age;
    }

    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeObject(this.firstName);
        out.writeObject(this.lastName);
        out.writeObject(this.birthday);
        out.writeInt(this.age);
    }

    public void readExternal(ObjectInput in) throws ClassNotFoundException, IOException {
        this.firstName = (String) in.readObject();
        this.lastName = (String) in.readObject();
        this.birthday = (Date) in.readObject();
        this.age = in.readInt();
    }
}