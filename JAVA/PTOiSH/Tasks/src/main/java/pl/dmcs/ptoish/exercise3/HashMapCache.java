package pl.dmcs.ptoish.exercise3;

import java.util.*;

public class HashMapCache {
    private static HashMapCache instance;
    private static Object monitor = new Object();
    private Map<String, Object> cache = Collections.synchronizedMap(new HashMap<String, Object>());

    private HashMapCache() {}

    public void put(String key, Object value) {
        cache.put(key, value);
    }

    public Object get(String key) {
        return cache.get(key);
    }

    public void clear(String key) {
        cache.put(key, null);
    }

    public void clear() {
        cache.clear();
    }

    public static HashMapCache getInstance() {
        if (instance == null) {
            synchronized (monitor) {
                if (instance == null) {
                    instance = new HashMapCache();
                }
            }
        }
        return instance;
    }
}