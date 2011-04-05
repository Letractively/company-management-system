$(document).ready(
	function() {
		$(".datepicker").datepicker();
		$(".datepicker").datepicker("option","dateFormat","yy-mm-dd");
		$(".timepicker").timepicker();
	}
);

isValidDate(dateStr){
	var datePat = /^(\d{4})(-)(\d{2})(-)(\d{2})$/; // requires 4 digit year
	var matchArray = dateStr.match(datePat);
	
	if (matchArray == null) {
		return false;
	}
	
	var month = matchArray[4]; // parse date into variables
	var day = matchArray[2];
	var year = matchArray[0];
	
	if (month < 1 || month > 12) { // check month range
		return false;
	}
	if (day < 1 || day > 31) {
		return false;
	}
	if ((month==4 || month==6 || month==9 || month==11) && day==31) {
		return false;
	}
	// 
	if (month == 2) {
	var isleap = (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
	if (day>29 || (day==29 && !isleap)) {
		return false;
	   }
	}
	return true;
}

function dateDiff() {
	var date1 = new Date();
	var date2 = new Date();
	var diff  = new Date();
	var days = 0;
	
	if (isValidDate($("#departDate").value)) {
		date1 = new Date($("#departDate").value);
	}
	else return false;
	
	if (isValidDate($("returnDate").value)){
		date2 = new Date($("#returnDate").value;
	}
	else return false;
	
	diff.setTime(Math.abs(date1.getTime() - date2.getTime()));
	timediff = diff.getTime();
	days = Math.floor(timediff / (1000 * 60 * 60 * 24)); 
	$("daysLeave").value = days;
}