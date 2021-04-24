import java.io.*;

class Exec{
	public static void main(String[] args)throws IOException,InterruptedException{
		String cmd = "bash /home/host/Documents/Project/TP/sad.sh";
		Runtime run = Runtime.getRuntime(); 
		Process pr = run.exec(cmd);
		pr.waitFor();
		BufferedReader buf = new BufferedReader(new InputStreamReader(pr.getInputStream()));
		String line = "";
		while((line=buf.readLine())!=null){
			System.out.println(line);
	}
}
}
