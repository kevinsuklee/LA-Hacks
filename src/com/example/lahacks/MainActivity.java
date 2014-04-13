package com.example.lahacks;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;
import android.widget.Button;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		Button startButton = (Button) findViewById(R.id.StartButton);
		View.OnClickListener handler = new View.OnClickListener() {
			@Override
			public void onClick(View arg0) {
				Intent tinderIntent = new Intent(MainActivity.this, TinderActivity.class);
				startActivity(tinderIntent);
			}
		};
		startButton.setOnClickListener(handler);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}
