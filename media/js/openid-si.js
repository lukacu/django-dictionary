/*
	Simple OpenID Plugin
	http://code.google.com/p/openid-selector/
	
	This code is licensed under the New BSD License.
*/

var providers_large = {
	google : {
		name : 'Google',
		url : 'https://www.google.com/accounts/o8/id'
	},
	yahoo : {
		name : 'Yahoo',
		url : 'http://me.yahoo.com/'
	},
	openid : {
		name : 'OpenID',
		label : 'Enter your OpenID.',
		url : null
	}
};

var providers_small = {
	livejournal : {
		name : 'LiveJournal',
		label : 'Enter your Livejournal username.',
		url : 'http://{username}.livejournal.com/'
	},
	flickr: {
		name: 'Flickr',        
		label: 'Enter your Flickr username.',
		url: 'http://flickr.com/{username}/'
	},
	myopenid : {
		name : 'MyOpenID',
		label : 'Enter your MyOpenID username.',
		url : 'http://{username}.myopenid.com/'
	},
	wordpress : {
		name : 'Wordpress',
		label : 'Enter your Wordpress.com username.',
		url : 'http://{username}.wordpress.com/'
	},
	blogger : {
		name : 'Blogger',
		label : 'Your Blogger account',
		url : 'http://{username}.blogspot.com/'
	},
	verisign : {
		name : 'Verisign',
		label : 'Your Verisign username',
		url : 'http://{username}.pip.verisignlabs.com/'
	},
	google_profile : {
		name : 'Google Profile',
		label : 'Enter your Google Profile username',
		url : 'http://www.google.com/profiles/{username}'
	}
};

openid.locale = 'si';
openid.sprite = 'en'; // reused in german& japan localization
openid.demo_text = 'V demo načinu. Normalno bi sledila preusmeritev OpenID:';
openid.signin_text = 'Prijavi se';
openid.image_title = 'prijavi se z {provider}';
