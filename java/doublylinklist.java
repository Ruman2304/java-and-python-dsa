
public class doublylinklist {

    class Node{
    int data;
    Node previous;
    Node next;
   

    public Node(int data){
        this.data=data;
    }
 }

 Node head,tail=null;

 public void addnode(int data){
    Node newnode=new Node(data);

    if(head==null){
        head=tail=newnode;
        head.previous=null;
        tail.next=null;
    }
    else{
        tail.next=newnode;
        newnode.previous=tail;
        tail=newnode;
        tail.next=null;

    }
 }
 public void display(){

    Node current=head;

    if(head==null){
        System.out.println("empty linklist");
        return;
    }
   
        while(current!=null){

            System.out.println(current.data+" ");
            current=current.next;
        }
    
    }

        public void search(int value){
            int i=1;
             Node current=head;
            boolean flag=false;
           


            if(head==null){
                System.out.println("link list iss empty");
                return;

            }
            while(current!=null){
               if(current.data==value){
                flag=true;
               break;
               }
               current=current.next;
               i++;
              
            }
            if(flag){
                System.out.println("node foud at ="+i);
            }
            else{
                System.out.println("node not found");
            }
        }
        public void addattail(int data){
            Node newnode=new Node(data);

            if(head==null){
                head=tail=newnode;
                head.previous=null;
                tail.next=null;

            }
            else{
                tail.next=newnode;
                newnode.previous=tail;
                tail=newnode;
                tail.next=null;
            }
        }
        public void addatfirst(int data){
            Node newnode=new Node(data);
             if(head==null){
                head=tail=newnode;
                head.previous=null;
                tail.next=null;
            }
            else{
                head.previous=newnode;
                newnode.next=head;
                head=newnode;
                newnode.previous=null;
            }
        }        int count;
        public void count(){
    Node current=head;
    do{
        count++;
        current=current.next;
    }while(current !=null);
    System.out.println("no of nodes "+count);
          

           
        }

        public void reverse(){
            Node previous=null;
            Node current=head;
            Node next;

            while(current !=null){
               next=current.next;
               current.next=previous;
               current.previous=next;
               previous=current;
               current=next;

            }
            head=previous;
        }
 

    public static void main(String[] args) {
        doublylinklist d1=new doublylinklist();
       
        d1.addnode(1);
        d1.addnode(2);
        d1.addnode(3);
        d1.addnode(4);
        d1.display();
        d1.search(3);
        d1.addattail(7);
        d1.addatfirst(0);
        d1.display();
        d1.count();
        d1.reverse();
        d1.display();
    }
    
}
