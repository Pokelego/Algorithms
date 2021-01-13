#include <iostream>

struct Node{
   public:
      int data;
      Node *next;
};

class SinglyLinkedList{
   public:
   SinglyLinkedList(){
      head = NULL;
      tail = NULL;
   }

   void append(int value){
      Node *temp = new Node;
      temp->data=value;
      temp->next=NULL;

      if (head==NULL){
         // If head is null then list is empty and create the head node
         head = temp;
         tail = temp;
         temp = NULL;
      }else{
         // Else create a node at the end
         tail->next = temp;
         tail = temp;
      }
   }

   void prepend(int val){
      Node *temp = new Node;
      temp->data = val;
      temp->next = head; // the previous head is what gets pointed to 
      head = temp;
   }

   void insert(int pos, int val){
      Node* temp = new Node;
      Node *pre = new Node;
      Node *curr = new Node;

      curr = head;

      for(int i = 1; i < pos; i++){ // go through list until you get to position
         pre = curr;
         curr = curr->next;
      }

      temp->data = val;
      pre->next = temp;
      temp->next = curr;
   }

   void deleteNode(int pos){
      Node *curr = new Node;
      Node *pre = new Node;
      curr = head;

      for (int i = 1; i < pos; i++){
         pre = curr;
         curr = curr->next;
      }
      pre->next = curr->next;
   }

   void display(){
      Node *temp = new Node;
      temp = head;
      while(temp != NULL){
         std::cout << temp->data << std::endl;
         temp = temp->next;
      }
   }

   private:
   Node *head, *tail;
};

int main(){
   SinglyLinkedList lList;
   lList.append(5);
   lList.append(3);
   lList.append(5);
   lList.append(4);
   lList.append(3);
   lList.display();
   lList.prepend(5);
   lList.display();
   lList.insert(2, 21);
   lList.display();
   lList.deleteNode(4);
   lList.display();
}