/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package OMS;

/**
 *
 * @author harvs
 */
import java.io.IOException;
import javax.swing.JOptionPane; 
import jxl.read.biff.BiffException;

public class OMS {

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     * @throws jxl.read.biff.BiffException
     */
    
    public static void main(String[] args) throws IOException, BiffException {
        // TODO code application logic here
        int ctr = 0;
        String input;
        
        String flavor;
        String size;
        int num;
        String sugarLevel;
        String sinker;
        String name;
        String askSinker;
        int scoop;
        int fileCtr;
        fileCtr = 0;
        
        
        while(ctr == 0){
            input = JOptionPane.showInputDialog("What would you like to do?:\n 1. Order MilkTea\n "
                                                                            + "2. Order FruitTea\n "
                                                                            + "3. Order HotTea\n "
                                                                            + "4. Exit");
            switch (input) {
                case "1":
                    flavor = JOptionPane.showInputDialog("Enter flavor");
                    size = JOptionPane.showInputDialog("Enter size");
                    num = Integer.parseInt(JOptionPane.showInputDialog("Enter number"));
                    sugarLevel = JOptionPane.showInputDialog("Enter Sugar Level");
                    askSinker = JOptionPane.showInputDialog("Do you want to add Sinkers:");
                    if("y".equals(askSinker) || "Y".equals(askSinker)){
                        sinker = JOptionPane.showInputDialog("Enter sinker");
                        scoop = Integer.parseInt(JOptionPane.showInputDialog("Enter number of scoops"));
                    }
                    else{
                        sinker = "none";
                        scoop = 0;
                    }
                    name = JOptionPane.showInputDialog("Enter Customer Name");
                    MilkTea order = new MilkTea(flavor, size, sugarLevel, sinker, scoop, num, name);
                    JOptionPane.showMessageDialog(null, "Order Placement Succesful.\n\nOrder Summary\n\n" + order.getOrderList());
                    OrderFile orderFile = new OrderFile(order.getOrderList(),fileCtr);
                    orderFile.PrintToFile();
                    fileCtr = fileCtr + 1;
                    break;
                    
                case "2":
                    
                    break;
                
                case "4":
                    ctr = 1;
                    break;
            }
        }
    }
    
}
