package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class Page3Controller {

    private static String ip="";
    private Stage stage;
    private Scene scene;
    private Parent root;

    public void FastScan(ActionEvent e) throws IOException {

        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page4.fxml"));
        root = loader.load();


        Page4Controller page4controller = loader.getController();
        page4controller.setIp(ip);

        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
        System.out.println("FastScan " + ip);
    }

    public void TCP(ActionEvent e) throws IOException {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page5.fxml"));
        root = loader.load();

        Page5Controller page5controller = loader.getController();
        page5controller.setIp(ip);

        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
        System.out.println("TCP");
    }

    public void UDP(ActionEvent e) throws IOException {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page6.fxml"));
        root = loader.load();

        Page6Controller page6controller = loader.getController();
        page6controller.setIp(ip);
        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
        System.out.println("UDP");
    }

    public void setIp(String ip) {
        this.ip = ip;
    }
}
