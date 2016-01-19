function Wrapper() {
	// Event handlers for each button linked to the appropriate webpage.
	$('button').on('click', function() {
		if(event.target.id === 'twitch') {
			window.location.href='https://twitch.tv/jaydork'
		}
		else if(event.target.id ==='home') {
			window.location.href='view.html'
		}
		else if(event.target.id==='videos') {
			window.location.href='videos.html'
		}
		else if(event.target.id==='games') {
			window.location.href='games.html'
		}
		else if(event.target.id==='bio') {
			window.location.href='bio.html'
		}
		else if(event.target.id==='signup') {
			window.location.href='signin.html'
		}
		else if(event.target.id==='createacct') {
			window.location.href='create_acct.html'
		}
	});
}

Wrapper();




