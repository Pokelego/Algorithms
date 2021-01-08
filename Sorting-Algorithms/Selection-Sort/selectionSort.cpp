#include <iostream>
#include <vector>

void selectionSort(std::vector<int>& array){
   for (int i = 0; i < array.size(); i++){
      int min_index = i;

      for(int j = i+1; j < array.size(); j++){
         if(array[j] < array[min_index]){
            min_index = j;
         }
      }
      int temp = array[i];
      array[i] = array[min_index];
      array[min_index] = temp;
   }
}