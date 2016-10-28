package algorithms;

import java.io.*;
import java.util.HashMap;

public class Main {

    static final int SAMPLESIZE = 500;

    public static void main(String [] args) {
        int [] sizes = {1000, 1500, 2000};

        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream("averages.dat"), "utf-8"))) {
            writer.write("cloudsize timeav nodecountav\n");
            for (int size : sizes) {
                Tester t = new Tester(size, 800, 55);
                HashMap<String, Float> data = t.runInstances(SAMPLESIZE);
                String toprint = String.valueOf(size) + " " +
                        data.get("timeav") + " " +
                        data.get("nodecountav") + "\n";
                System.out.println(toprint);
                writer.write(toprint);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}
