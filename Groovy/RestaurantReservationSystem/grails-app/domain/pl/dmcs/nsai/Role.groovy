package pl.dmcs.nsai

import groovy.transform.ToString
import groovy.transform.EqualsAndHashCode

@EqualsAndHashCode(includes='authority')
@ToString(includes='authority', includeNames=true, includePackage=true)
class Role {
    String authority

    static constraints = {
        authority(blank: false, unique: true)
    }

    static mapping = {
        cache(true)
    }
}
