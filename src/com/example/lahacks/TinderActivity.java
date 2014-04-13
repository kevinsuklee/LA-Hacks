package com.example.lahacks;

import java.util.HashMap;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.view.*;

public class TinderActivity extends Activity {

	TextView _view;
	ViewGroup _root;
	private int _xDelta;
	private int _yDelta;
	private HashMap<String, Boolean> preferenceMap = new HashMap<String, Boolean>();
	private int count = 0;
	private int MAX_NUM_PICS = 5;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_tinder);
		ImageView check_b = (ImageView) findViewById(R.id.check_button);
		ImageView cross_b = (ImageView) findViewById(R.id.x_button);
		
		getPictures();
		
		View.OnClickListener handler_check = new View.OnClickListener() {
			@Override
			public void onClick(View arg0) {
				if (count == MAX_NUM_PICS - 1) {
					
				}
			}
		};
		View.OnClickListener handler_cross = new View.OnClickListener() {
			@Override
			public void onClick(View arg0) {
				if (count == MAX_NUM_PICS - 1) {
					
				}
			}
		};
		
		check_b.setOnClickListener(handler_check);
		cross_b.setOnClickListener(handler_cross);
		

	}

		
	public void getPictures() {
		try {
		    HttpClient client = new DefaultHttpClient();  
		    String getURL = "http://10.55.9.203/survey";
		    HttpGet get = new HttpGet(getURL);
		    HttpResponse responseGet = client.execute(get);  
		    HttpEntity resEntityGet = responseGet.getEntity();  
		    if (resEntityGet != null) {
		        // do something with the response
		        String response = EntityUtils.toString(resEntityGet);
		        Log.v("GET RESPONSE", response);
		    }
		} catch (Exception e) {
		    e.printStackTrace();
		}
	}
	
	
	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.tinder, menu);
		return true;
	}

}
