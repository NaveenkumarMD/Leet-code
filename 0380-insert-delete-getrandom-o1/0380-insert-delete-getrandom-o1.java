import java.util.HashMap;

public class RandomizedSet {
    int flag;
    HashMap<Integer,Integer> map;
    public RandomizedSet() {
            this.map=new HashMap<Integer,Integer>();
            this.flag=0;
    }

    public boolean insert(int val) {
        if(this.map.containsKey(val)){
            return false;
        }
        else{
            this.map.put(val,val);
            return true;
        }
    }

    public boolean remove(int val) {
        if(this.map.containsKey(val)){
            this.map.remove(val);
            return true;
        }
        else{
            return false;
        }
    }

    public int getRandom() {
        int len= this.map.keySet().toArray().length;
         Random rand = new Random();
        return (int)this.map.values().toArray()[rand.nextInt(len)];
    }
}