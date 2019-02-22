
let {PythonShell} = require('python-shell')

global.boolLock = false;

const app = require('express')();

const server = require('http').createServer(app);

const io = require('socket.io')(server);


app.get('/', function(req, res) {
	console.log("mainpage");
	console.log(boolLock);	

	if(boolLock == false){

		res.sendFile(__dirname + "/" + "test.txt");
			PythonShell.run('motor.py', null, function (err) {
  				if (err) throw err;
  				console.log('finished MOTOR');
			});
	}
	else if(boolLock == true){
		res.redirect('/locked');
		PythonShell.run('LED.py', null, function (err) {
  			if (err) throw err;
  			console.log('finished LED');
		});
	}

});

app.get('/admin', function(req, res) {
	console.log("adminpage");
	console.log(boolLock);	
	res.sendFile(__dirname + "/" + "admin.txt");

	if(boolLock == false){
		boolLock = true;
		res.redirect('/locked');	
	}
	else if(boolLock == true){
		boolLock = false;
		res.redirect('/unlocked');	
	}
});

app.get('/locked', function(req, res) {
	console.log("lockedpage");
	res.sendFile(__dirname + "/" + "locked.txt");
});


app.get('/unlocked', function(req, res) {
	console.log("unlockedpage");
	res.sendFile(__dirname + "/" + "unlocked.txt");
});


server.listen(3000);

console.log("server on");
