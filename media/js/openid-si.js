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
		label : 'Vnesi OpenID.',
		url : null
	},
    vicos : {
        name : 'ViCoS Lab',
        url : 'https://auth.vicos.si/openid/'
    }
};

var providers_small = {
	livejournal : {
		name : 'LiveJournal',
		label : 'Vnesi Livejournal uporabniško ime.',
		url : 'http://{username}.livejournal.com/'
	},
	flickr: {
		name: 'Flickr',        
		label: 'Vnesi Flickr uporabniško ime.',
		url: 'http://flickr.com/{username}/'
	},
	myopenid : {
		name : 'MyOpenID',
		label : 'Vnesi MyOpenID uporabniško ime.',
		url : 'http://{username}.myopenid.com/'
	},
	wordpress : {
		name : 'Wordpress',
		label : 'Vnesi Wordpress.com uporabniško ime.',
		url : 'http://{username}.wordpress.com/'
	},
	blogger : {
		name : 'Blogger',
		label : 'Tvoj Blogger račun',
		url : 'http://{username}.blogspot.com/'
	},
	google_profile : {
		name : 'Google Profile',
		label : 'Vnesi Google Profile uporabniško ime',
		url : 'http://www.google.com/profiles/{username}'
	}
};

openid.locale = 'si';
openid.sprite = 'en'; // reused in german& japan localization
openid.demo_text = 'V demo načinu. Normalno bi sledila preusmeritev OpenID:';
openid.signin_text = 'Prijavi se';
openid.image_title = 'prijavi se z {provider}';
