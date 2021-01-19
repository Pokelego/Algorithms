#include <iostream>
#include <string>
#include <vector>

class Stack{
private:
   int top;
   std::vector<int> arr;

public:
      Stack(){
         this->top = -1;
      }

      bool isEmpty(){
         if (this->top == -1){
            return true;
         }
         else{
            return false;
         }
      }

      bool isFull(){
         if (this->top == this->arr.size()-1){
            return true;
         }else{
            return false;
         }
      }

      void push(int val){         
         this->top++;
         this->arr.push_back(val);
      }

      int pop(){
         if (isEmpty()){
            std::cout << "Cannot Remove, Stack Is Empty\n";
            return 0;
         }else{
            int popValue = this->arr[top];
            this->arr.pop_back();
            this->top--;
            return popValue;
         }
      }

      int count(){
         return (this->top+1);
      }

      int peak(int pos){
         if(isEmpty()){
            std::cout << "Stack is Empty\n";
            return 0;
         }else{
            return this->arr[pos];
         }
      }

      void change(int pos, int val){
         this->arr[pos] = val;
      }

      void display(){
         for (int i = this->arr.size(); i >=0; i--){
            std::cout << arr[i] << std::endl;
         }
      }
};
