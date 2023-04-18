function sprintReview(args) {
	const checkAssignee = (object, name) => { // function to check if the 0bject already has the property of "name"
		return object.hasOwnProperty(name);
	};

	const number = Number(args.shift()); // gets the number of tasks from the array
	const collection = {}; // creates an object to store the data for later

	for (let i = 0; i < number; i++) {
		const tokens = args[i].split(':');  // splits the array to get all the needed info
		const assignee = tokens[0]; // gets the assignee
		const taskId = tokens[1]; // gets the task id
		const title = tokens[2]; // gets the title
		const status = tokens[3]; // gets the status
		const points = tokens[4]; // gets the points
		if (!checkAssignee(collection, assignee)) { // checks if the assignee doesn't exist and adds is with the tasks
			collection[assignee] = [[taskId, title, status, points]];
		} else {
			collection[assignee].push([taskId, title, status, points]);
		}
	}


	args.forEach((element) => { // loops through the array and gets the data
		const tokens = element.split(':'); // splits the array to get all the needed info
		let command = tokens[0]; // gets the command 

		if (command === 'Add New') {  // checks for the given command and executes whatever its needed for that command.
			let assignee = tokens[1];
			let taskId = tokens[2];
			let title = tokens[3];
			let status = tokens[4];
			let points = tokens[5];
			if (checkAssignee(collection, assignee)) {
				collection[assignee].push([taskId, title, status, points]);
			} else {
				console.log(
					`Assignee ${assignee} does not exist on the board!`
				);
			}
		} else if (command === 'Change Status') {
			let assignee = tokens[1];
			let taskId = tokens[2];
			let newStatus = tokens[3];
			if (checkAssignee(collection, assignee)) { // checks if assignee exists
				let changed = false;  // boolean to indicate if the change is made successfully
				for (let i = 0; i < collection[assignee].length; i++) {
					if (collection[assignee][i][0] === taskId) {
						collection[assignee][i][2] = newStatus;
						changed = true; // successful change
						break;
					}
				}
				if (!changed) { // here if its not successful we print this message
					console.log(
						`Task with ID ${taskId} does not exist for ${assignee}!`
					);
				}
			} else { // message if the assignee doesn't exist
				console.log(
					`Assignee ${assignee} does not exist on the board!`
				);
			}
		} else if (command === 'Remove Task') {
			let assignee = tokens[1];
			let index = tokens[2]; // gets how many array that assignee object has. Example: {Kiril: [], []} - 2 arrays here.

			if (checkAssignee(collection, assignee)) { // checks if the assignee exists
				let arrLength = collection[assignee].length; // gets the number of array that assignee
				if (index < 0 || index >= arrLength) { // checks if the index is correct / exists
					console.log('Index is out of range!');
				} else {
					collection[assignee].splice(index, 1); // uses splice method to remove the task on that index
				}
			} else {
				console.log(
					`Assignee ${assignee} does not exist on the board!`
				);
			}
		}
	});

	const results = { // creates an array of tasks names and their points
        'ToDo': 0,
        'In Progress': 0,
        'Code Review': 0,
        'Done': 0
    };
	const aggregate = { // creates an array to compare the points between the Done and Not Done tasks
        'Done': 0,
        'Not Done': 0
    };

	for (const prop in collection) { // loops through the collection (object)
		for (let el of collection[prop]) { // loops through the object[key] arrays
			let statusName = el[2];
			let points = Number(el[3]);
            results[statusName] += points;
			if (statusName === 'Done') {
                aggregate[statusName] += points;
			} else {
                aggregate['Not Done'] += points;
			}
		}
	}

	for (const prop in results) { // loops through the results object to print the results
		if (prop === 'Done') {
			console.log(`${prop} Points: ${results[prop]}pts`);
		} else {
			console.log(`${prop}: ${results[prop]}pts`);
		}
	}

	if (aggregate['Done'] >= aggregate['Not Done']) { // checks if the sprint was successful or not
		console.log('Sprint was successful!');
	} else {
		console.log('Sprint was unsuccessful...');
	}
}

sprintReview([
    '5',
    'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
    'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
    'Peter:BOP-1211:POC:Code Review:5',
    'Georgi:BOP-1212:Investigation Task:Done:2',
    'Mariya:BOP-1213:New Account Page:In Progress:13',
    'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
    'Change Status:Peter:BOP-1290:ToDo',
    'Remove Task:Mariya:1',
    'Remove Task:Joro:1',
]
)
