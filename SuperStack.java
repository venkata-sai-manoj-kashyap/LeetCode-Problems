import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class SuperStack {
    static class Element{
        public long value;
        public long inc;
    }

    public static String push(ArrayList<Element> stack, long val){
        Element element = new Element();
        element.value = val;
        element.inc = 0;
        stack.add(element);
        return Long.toString(stack.get(stack.size()-1).value + stack.get(stack.size() - 1).inc);
    }

    public static String pop(ArrayList<Element> stack) {
        Element element = stack.remove(stack.size() - 1);
        if(stack.size() == 0){
            return "EMPTY";
        }
        Element topElement = stack.get(stack.size() - 1);
        topElement.inc = topElement.inc + element.inc;
        return Long.toString(topElement.value + topElement.inc);
    }

    public static String inc(ArrayList<Element> stack, int incCount, long value) {
        Element element = stack.get(incCount-1);
        element.inc = element.inc + value;
        if(stack.size() == 0){
            return "EMPTY";
        }
        Element topElement = stack.get(stack.size() - 1);
        return Long.toString(topElement.inc + topElement.value);
    }

    static void superStack(String[] operations) {
        ArrayList<Element> stack = new ArrayList<>();
        ArrayList<String> result = new ArrayList<>();

        for(String command: operations){
            String[] splits = command.split(" ");
            if(splits[0].equals("push")){
                long pushValue = Long.valueOf(splits[1]);
                result.add(push(stack, pushValue));
            }
            else if(splits[0].equals("pop")){
                result.add(pop(stack));
            }
            else{
                int elements = Integer.valueOf(splits[1]);
                long incValue = Long.valueOf(splits[2]);
                result.add(inc(stack, elements, incValue));
            }
        }

        for(String x: result){
            System.out.println(x);
        }
    }

    public static void main(String[] args)  {
		String[] arr = {"push 3", "pop", "push 4", "pop"};
		superStack(arr);
	}
