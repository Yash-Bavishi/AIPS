package sample;

import java.util.regex.Pattern;

public class PortChecker {

    private static Pattern portScannerPattern;
    private static final String portPattern = "^()([1-9]|[1-5]?[0-9]{2,4}|6[1-4][0-9]{3}|65[1-4][0-9]{2}|655[1-2][0-9]|6553[1-5])$";

    static {
        portScannerPattern = Pattern.compile(portPattern);
    }

    public static boolean isValidPortNumber(String portNumber) {
        return portScannerPattern.matcher(portNumber).find();
    }

}
