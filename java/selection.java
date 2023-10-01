public class selection {
    public void sele(int[] arr){

        for(int i=0;i<arr.length-1;i++){
            int index=i;
          
            for(int j=i+1;j<arr.length;j++){
                if(arr[j]<arr[index]){
                    index=j;
                }
            }
            int temp=arr[index];
            arr[index]=arr[i];
            arr[i]=temp;
        }
    }
    public static void main(String[] args) {
        int[] arr={9,7,6,5,4,3};
        selection s=new selection();
        s.sele(arr);
        for(int i=0;i<arr.length;i++){
        System.out.println(arr[i]);}

    }
    
}
