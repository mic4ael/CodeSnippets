package pl.dmcs.ptoish.benchmarking;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface BenchmarkMethod {
	public int numberOfIterations() default 1;
	public String[] arguments() default {};
	public String logfile() default "";
}