import java.awt.Desktop;
import java.io.*;

class Try{
	public static void main(String[] args)throws IOException,InterruptedException{
		String file_name = "whoami.txt";
		PrintStream o = new PrintStream(new File(file_name));
		File file = new File(file_name);
		System.setOut(o);
		String cmd = "python3 ../Scholz/try_scholz.py 127.0.0.1";
		Process pr = Runtime.getRuntime().exec(cmd);
		pr.waitFor();
		BufferedReader reader = new BufferedReader(new InputStreamReader(pr.getInputStream()));
		String line = "";
		while((line=reader.readLine()) !=null){
			System.out.println(line);
	}
		System.out.println("Mihir is gay");
		if(!Desktop.isDesktopSupported()){
			System.out.println("NOt supported");
		
		return;
		}
		Desktop desktop = Desktop.getDesktop();
		if(file.exists()){
			desktop.open(file);
		}
}
}
