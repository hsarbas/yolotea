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
import java.io.File;
import java.io.IOException;

import jxl.Cell;
import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;

public final class MilkTea{
    int num;
    String name;
    String flavor;
    double teaPrice;
    String size;
    String sugarLevel;
    String sinker;
    int scoop;
    double sinkerPrice;
    double totalPrice;
    MilkTea next;
    
    /**
     *
     * @param newFlavor
     * @param newSize
     * @param newSugarLevel
     * @param newSinker
     * @param newScoop
     * @param newNum
     * @param newName
     * @throws IOException
     * @throws BiffException
     */
    public MilkTea(String newFlavor, String newSize, String newSugarLevel, String newSinker, int newScoop, int newNum, String newName) throws IOException, BiffException{
        num = newNum;
        name = newName;
        flavor = newFlavor;
        size = newSize;
        sugarLevel = newSugarLevel;
        sinker = newSinker;
        scoop = newScoop;
        teaPrice = getTeaPrice(flavor,size);
        sinkerPrice = getSinkerPrice(sinker);
        totalPrice = (teaPrice*num) + (sinkerPrice*scoop);
    }
    
    
    public String getOrderList(){
            String order;
            order = "Flavor: " + this.flavor + "\n" +
                    "Size: " + this.size + " - " + this.teaPrice + "\n" +
                    "Number: " + this.num  + "\n" +
                    "Sugar Level: " + this.sugarLevel + "\n" +
                    "Sinker: " + this.sinker  + " - " + this.sinkerPrice + "\n" +
                    "Scoops: " + this.scoop + "\n" +
                    "Customer: " + this.name + "\n" +
                    "Total Price: " + this.totalPrice + "\n";
            //order = "ORDER";
            return order;
        }
   
    
    /**
     *
     * @param flavor
     * @param size
     * @return
     * @throws IOException
     * @throws BiffException
     */
    public double getTeaPrice(String flavor, String size) throws IOException, BiffException{
        double priceData = 0.0;
        
      Workbook workbook = Workbook.getWorkbook(new File("C:\\HARVS\\YOLOTEA\\Yolotea Menu.xls"));
      Sheet sheet = workbook.getSheet(0);
      int currRow = 0;
      int currCol = 0;
      //int xcell = 0, ycell = 0;
      int rows = sheet.getRows();
      int columns = sheet.getColumns();
      
      Cell cell;
      
      while(currRow != rows){
          while(currCol != columns){
              cell = sheet.getCell(currCol,currRow);
              if(cell.getContents().equalsIgnoreCase(flavor)){
                  if(size.equalsIgnoreCase("L")){
                        priceData = Integer.parseInt(sheet.getCell((currCol+1),currRow).getContents());
                        return priceData;
                  }
                  else if(size.equalsIgnoreCase("XL")){
                        priceData = Integer.parseInt(sheet.getCell((currCol+2),currRow).getContents());
                        return priceData;
                  }
              }
              currCol = currCol + 1;
          }
          currCol = 0;
          currRow = currRow + 1;
      }
      workbook.close();
        
        return priceData;
    }
    
    /**
     *
     * @param sinker
     * @return
     * @throws IOException
     * @throws BiffException
     */
    public double getSinkerPrice(String sinker) throws IOException, BiffException{
        double priceData = 0.0;
        
      Workbook workbook = Workbook.getWorkbook(new File("C:\\HARVS\\YOLOTEA\\Yolotea Menu.xls"));
      Sheet sheet = workbook.getSheet(3);
      int currRow = 0;
      int currCol = 0;
      //int xcell = 0, ycell = 0;
      int rows = sheet.getRows();
      int columns = sheet.getColumns();
      Cell cell;
      
      while(currRow!=rows){
          while(currCol!=columns){
              cell = sheet.getCell(currCol,currRow);
              if(cell.getContents().equalsIgnoreCase(sinker)){
                  priceData = Integer.parseInt(sheet.getCell((currCol+1),currRow).getContents());
                  return priceData;
              }
              currCol = currCol + 1;
          }
          currCol = 0;
          currRow = currRow + 1;
      }
      workbook.close();  
      return priceData;
        
    } 
}
