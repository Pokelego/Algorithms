#include <iostream>
#include <vector>

class Queue{
private:
   std::vector<int> arr;
   int rear;
   int front;

public:
   Queue(){
      front = -1;
      rear = -1;
   }
   
   void enqueue(int val){
      if(isEmpty()){
         this->front = 0;
         this->rear = 0;
         this->arr.push_back(val);
      }else{
         rear++;
         this->arr.push_back(val);
      }
   }

   int dequeue(){
      int val;
      
      if(isEmpty()){
         std::cout << "Queue is empty\n";
         return 0;
         
      }else if(this->front == this->rear){
         val = this->arr[this->front];
         arr[front] = 0;
         this->front = -1;
         this->rear = -1;
         return val;

      }else{
         val = this->arr[this->front];
         this->arr.erase(this->arr.begin());
         this->front++;
         return val;
      }
   }

   int peak(){
      if(isEmpty()){
         std::cout << "Queue is empty\n";
         return 0;
      }else{
         return this->arr[this->front];
      }
   }

   bool isFull(){
      if (this->rear == this->arr.size()-1){
         return true;
      }else{
         return false;
      }
   }

   bool isEmpty(){
      if(this->front == -1 && this->rear == -1){
         return true;
      }else{
         return false;
      }
   }

   int count(){
      return this->arr.size();         
   }
};
