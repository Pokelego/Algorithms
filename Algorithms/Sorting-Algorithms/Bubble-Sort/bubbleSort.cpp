#include<iostream>
#include<vector>

void bubbleSort(std::vector<int>& array){
   bool isSorted = false;
   int lastUnsorted = array.size()-1;

   while(isSorted == false){
      isSorted = true;
      for(int i = 0; i < lastUnsorted; i++){
         if(array[i] > array[i+1]){
            int temp = array[i];
            array[i] = array[i+1];
            array[i+1] = temp;
            isSorted = false;
         }
      }
      lastUnsorted--;
   }
}