public class singlyll {
    class Node{
        Node next;
        int data;

        public Node(int data){
            this.data=data;
        }
    }
    Node head,tail=null;
    public void insert(int data){
        Node n=new Node(data);
        if(head==null){
            head=tail=n;
          
        }else{
            tail.next=n;
            tail=n;
        }}
       public void display(){

        Node current=head;
        while(current!=null){
            System.out.println(current.data+" ");
            current=current.next;
        }
       }  

       public void reverse(){
        Node previour=null;
        Node current=tail=head;
        Node next;

        while(current !=null){
            next=current.next;
            current.next=previour;
            previour=current;
            current=next;


        }
        head= previour;
       
       
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
    public static void main(String[] args) {
        singlyll s=new singlyll();
        s.insert(1);
        s.insert(2);
        s.insert(3);
        s.insert(4);
        s.display();
        s.search(2);
        s.reverse();
        s.display();
        
    }
    
}
