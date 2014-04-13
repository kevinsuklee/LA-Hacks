package com.example.lahacks;

import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;
import org.json.JSONArray;
import org.json.JSONObject;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.util.Log;

public class RetrieveImage implements Runnable{
	ArrayList<Bitmap> result;
	
	public RetrieveImage(ArrayList<Bitmap> arg) {
		super();
		result = arg;
	}
	
	
	public void run() {
		try {
			ArrayList<String> imgUrls = new ArrayList<String>();
			String response = null;
		    HttpClient client = new DefaultHttpClient();  
		    String getURL = "http://10.55.9.203/survey";
		    HttpGet get = new HttpGet(getURL);
		    HttpResponse responseGet = client.execute(get);  
		    HttpEntity resEntityGet = responseGet.getEntity();  
		    if (resEntityGet != null) {
		        // do something with the response
		        response = EntityUtils.toString(resEntityGet);
		        Log.v("GET RESPONSE", response);
		    }
		    JSONObject reader = new JSONObject(response);
		    JSONArray urls = reader.getJSONArray("urls");
		    for (int i = 0; i < 5; i++) {
		    	imgUrls.add(urls.get(i).toString());
		    }
		    System.out.println("done");
		    
		    for (String imgUrl : imgUrls) {
		    	imgUrl = imgUrl.split("=")[0]+"=s1000";
		    	
		    	InputStream stream = null;
		    	Bitmap bitmap = null;
		    	try {
		    		URL url = new URL(imgUrl);
		    		HttpURLConnection connection = (HttpURLConnection) url.openConnection();
		    		connection.setRequestMethod("GET");
		    		connection.connect();
		    		if (connection.getResponseCode() == HttpURLConnection.HTTP_OK) {
	                    stream = connection.getInputStream();
		    		}
			    	bitmap = BitmapFactory.decodeStream(stream, null, null);
			    	result.add(bitmap);
			    	stream.close();
		    		
		    	} catch (Exception ex) {
		    		
		    	}

		    }
		    
		    
		    
		    
		} catch (Exception e) {
		    e.printStackTrace();
		}
	}
}
