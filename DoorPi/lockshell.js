
let {PythonShell} = require('python-shell')

global.boolLock = false;

const app = require('express')();

const server = require('http').createServer(app);

app.get('/', function(req, res) {
	console.log("mainpage");
	console.log(boolLock);	

	if(boolLock == false){

		res.sendFile(__dirname + "/" + "unlocked.txt");
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


server.listen(3000);

console.log("server on");
