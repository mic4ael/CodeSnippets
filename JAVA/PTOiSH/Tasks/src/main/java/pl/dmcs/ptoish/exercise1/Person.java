package pl.dmcs.ptoish.exercise1;

import java.io.Serializable;
import java.util.Date;

class Person implements Serializable {
    private String firstName;
    private String lastName;
    private Date birthday;
    private Integer age;

    public Person(String firstName, String lastName, Date birthday, Integer age) {
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
}