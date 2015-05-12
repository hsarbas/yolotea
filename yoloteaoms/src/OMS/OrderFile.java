/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package OMS;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;



/**
 *
 * @author harvs
 */
public class OrderFile {
    private final String content;
    private final int ctr;
    
    public OrderFile(String orderList,int fileCtr) throws IOException{
        content = orderList;
        ctr = fileCtr;
        
    }
    
    public void PrintToFile() throws IOException{
        File file;
        file = new File("orders/" + Integer.toString(ctr) + ".txt");
            FileWriter fw = new FileWriter(file.getAbsoluteFile());
        try (BufferedWriter bw = new BufferedWriter(fw)) {
            bw.write(content);
        }
    }
    
    
    
}
