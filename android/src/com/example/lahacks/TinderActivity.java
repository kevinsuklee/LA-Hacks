package com.example.lahacks;

import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;

import android.os.AsyncTask;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
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
	String result = "";
	private HashMap<String, Boolean> preferenceMap = new HashMap<String, Boolean>();
	private int count = 0;
	private int MAX_NUM_PICS = 5;
	private ArrayList<Bitmap> imageBitmaps;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_tinder);
		getPictures();
		try {
			Thread.sleep(5000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		ImageView check_b = (ImageView) findViewById(R.id.check_button);
		ImageView cross_b = (ImageView) findViewById(R.id.x_button);
		ImageView food_pic = (ImageView) findViewById(R.id.food_image);
		
		
		
		View.OnClickListener handler_check = new View.OnClickListener() {
			@Override
			public void onClick(View arg0) {
				if (count != MAX_NUM_PICS - 1) {
					result += "1";
					changeImage();
					count++;
				}
			}
		};
		View.OnClickListener handler_cross = new View.OnClickListener() {
			@Override
			public void onClick(View arg0) {
				if (count == MAX_NUM_PICS - 1) {
					result += "0";
					changeImage();
					count++;
				}
			}
		};
		
		check_b.setOnClickListener(handler_check);
		cross_b.setOnClickListener(handler_cross);
		food_pic.setImageBitmap(imageBitmaps.get(count));
		count++;
	}
	public void changeImage() {
		ImageView food_pic = (ImageView) findViewById(R.id.food_image);
		food_pic.setImageBitmap(imageBitmaps.get(count));
	}
	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.tinder, menu);
		return true;
	}
	
	public void getPictures() {
		imageBitmaps = new ArrayList<Bitmap>(); 
		RetrieveImage getter = new RetrieveImage(imageBitmaps);
		new Thread(getter).start();
	}
	
}

	
