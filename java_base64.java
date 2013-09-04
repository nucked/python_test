import sun.misc.BASE64Decoder;  
import sun.misc.BASE64Encoder; 

public class Encode_Decode {
	public static String getBase64(String s){
		if (s == null) return null;
		return(new BASE64Encoder().encodeBuffer(s.getBytes()));
	}
	public static String getBase64Decode(String s){
		if (s == null) return null;
		BASE64Decoder decoder = new BASE64Decoder(); 
		try { 
			byte[] b = decoder.decodeBuffer(s); 
			return new String(b); 
			} catch (Exception e) { 
			return null; 
			}	
		
		
	}
	
	public static void main(String args[]){
		String s = "hello world";
		String s2 = "aGVsbG8gd29ybGQ=";
		System.out.println(getBase64(s));
		System.out.println(getBase64Decode(s2));
	}

}
