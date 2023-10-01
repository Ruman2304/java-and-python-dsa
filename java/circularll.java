class circularll{
    class Node{
       Node next;
       int data;

       public  Node(int data){
          this.data=data;
       }

    }
    int count;
    Node head,tail=null;
    public void addnode(int data){
        Node n=new Node(data);
        if(head==null){

            head=tail=n;
            n.next=head;
            return;
        }
        else{ 
            tail.next=n;
            tail=n;
            tail.next=head;


        }


    }
    public void display(){

        Node current=head;

        if(head==null){
            System.out.println("empty");
            return;
        }
        do{
            System.out.println(" "+current.data);
            current=current.next;  
        
        }while(current.next!=head);

            System.out.println();
            
        }
        public void count(){

            
            Node current=head;
            do{
                 count++;
                current=current.next;
            }
            while(current !=head);
            
            System.out.println("no of noddes" + count);
        }
    public void search(int value){

        int i;
        Node current=head;
        boolend flag=false;

        while(current !=head){
            if(current.data==value){

            }

        }
    } 
              
        
    
    public static void main(String[] args) {
        circularll i=new circularll();
        i.addnode(1);
        i.addnode(2);
        i.addnode(3);
        i.addnode(4);
         i.addnode(5);
        i.display();
        i.count();
    }
}