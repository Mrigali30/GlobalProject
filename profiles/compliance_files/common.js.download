function req(variable) {
	var query = window.location.search.substring(1);
	var vars = query.split("&");
	for (var i=0;i<vars.length;i++) {
		var pair = vars[i].split("=");
		if (pair[0] == variable) {
			return pair[1];
		}
	}
}

function showHidePeopleSection(link, num, label1, label2) {
	try {
		var rows = document.getElementsByName('showHide');
		for (var i = 5; i < num; i++) {
			if (MODElement.get('row' + i).style.display == 'none') {
				MODElement.get('row' + i).style.display = '';
			} else {
				MODElement.get('row' + i).style.display = 'none';
			}
		}

		if (link.innerHTML == label1) {
			link.innerHTML = label2;
		} else {
			link.innerHTML = label1;
		}
	} catch (e) { }
};

function popwin(url,w,h,type) {
	if (!w){ w = 800; }
	if (!h){ h = 500; }
	if (url){
	if (type == 'nonav'){
		this.popWindow = window.open(url, 'pop_window', 'width='+w+',height='+h+',scrollbars=yes,menubar=0,status=no,toolbar=0,resizable=yes');
	} else {
		this.popWindow = window.open(url, 'pop_window', 'width='+w+',height='+h+',scrollbars=yes,menubar=1,status=no,toolbar=1,resizable=yes');
	}
	this.popWindow.focus();
	}
}

function ArrayLength(arr) {
	var ct = 0;
	for (var idx in arr) {
		ct++;
	}
	return ct;
}

function GetScrollTop(){
	var scrollTop = document.body.scrollTop;
	
	if (scrollTop == 0) {
		if (window.pageYOffset) {
			scrollTop = window.pageYOffset;
		} else {
			scrollTop = (document.body.parentElement) ? document.body.parentElement.scrollTop : 0;
		}
	}
		
	return scrollTop;
}

//	clearInput checks an input box to see if the current value is 
//	equal to the default value.  you can supply a default value if you choose.
//	otherwise, the default value is set to targetID.defaultValue.  this is useful
//	if you are dynamically setting a default value (such as the news pages)
function clearInput(targetID, defVal) {
	var defaultVal = "";
	defVal ? defaultVal = defVal : defaultVal = targetID.defaultValue;

	if (targetID.value == defaultVal) {
		targetID.value = "";
	}
}

//fillInput checks the value in an element and, if it matches valueToReplace, replaces that value with replacementVal
/*example:
	<input onfocus=\"javascript:fillInput(this, 'Keyword(s)', '');\" onblur=\"javascript:fillInput(this, '', 'Keyword(s)');\" />
*/ 
function fillInput(targetEl, valueToReplace, replacementVal) {
	if (targetEl.value == valueToReplace) {
		targetEl.value = replacementVal;
	}
} 

//Funtion used for Report Data Error link and panel
var reportError = function () {
	this.panel = MODElement.get("reportErrorPanel");
	this.formDiv = MODElement.get("formDiv");
	this.submitDiv = MODElement.get("sentErrorDiv");
	this.reportLink = MODElement.get("reportErrorLink");
	this.reportLink1 = MODElement.get("reportErrorLink1");
	this.capIQReportLink = MODElement.get("capIQReportErrorLink");

	this.closeBtn = MODElement.get("reportErrorCloseBtn");
	this.cancelBtn = MODElement.get("reportErrorCancelBtn");
	this.submitBtn = MODElement.get("reportErrorSubmitBtn");

	//after submit
	this.anotherLink = MODElement.get("submitAnotherLink");
	this.doneLink = MODElement.get("doneLink");

	// input fields elements
	this.inSection = MODElement.get("sectionHeader");
	this.inCompanyName = MODElement.get("companyName");
	this.inDataPoint = MODElement.get("dataPoint");
	this.inYourName = MODElement.get("yourName");
	this.inYourEmail = MODElement.get("yourEmail");
	this.inYourPhone = MODElement.get("yourPhone");
	this.inDescribe = MODElement.get("describeError");
	this.inDataCorrectionNeeded = MODElement.get("DataCorrectionNeeded");
	this.inTypeOfData = MODElement.get("typeOfData");

	//labels elements
	this.lbSection = MODElement.get("sectionHeaderLabel");
	this.lbDataPoint = MODElement.get("dataPointLabel");
	this.lbCompanyName = MODElement.get("sectionHeaderLabel");
	this.lbYourName = MODElement.get("yourNameLabel");
	this.lbYourEmail = MODElement.get("yourEmailLabel");
	this.lbYourPhone = MODElement.get("yourPhoneLabel");
	this.lbDescribe = MODElement.get("describeErrorLabel");
	this.lbDataCorrectionNeeded = "Update Needed";
	this.lbTypeOfData = "Type Of Data";

	this.fields = [];
	this.fields['sectionHeader'] = { inputEl: this.inSection, labelEl: this.lbSection, label: 'Section Header' };
	this.fields['dataPoint'] = { inputEl: this.inDataPoint, labelEl: this.lbDataPoint, label: 'Data Point' };
	this.fields['companyName'] = { inputEl: this.inCompanyName, labelEl: this.lbCompanyName, label: 'Company Name' };
	this.fields['yourName'] = { inputEl: this.inYourName, labelEl: this.lbYourName, label: 'Your Name' };
	this.fields['yourEmail'] = { inputEl: this.inYourEmail, labelEl: this.lbYourEmail, label: 'Your E-Mail Address' };
	this.fields['yourPhone'] = { inputEl: this.inYourPhone, labelEl: this.lbYourPhone, label: 'Your Phone Number' };
	this.fields['describeError'] = { inputEl: this.inDescribe, labelEl: this.lbDescribe, label: 'Descripe Update Request' };
	this.fields['dataCorrectionNeeded'] = { inputEl: this.inDataCorrectionNeeded, labelEl: this.lbDataCorrectionNeeded, label: 'Update Needed' };
	this.fields['typeOfData'] = { inputEl: this.inTypeOfData, labelEl: this.lbTypeOfData, label: 'Type of Data' };

	this.formData = [];
	this.errors = [];
	this.errorAnnouncePanel = MODElement.get("errorAnnouncePanel");
	this.errorList = MODElement.get("errorList");

	this.shouldDrag = false;

	this.cBuffer = new ContentBuffer();
}
reportError.prototype.AttachEvents = function () {
	Events.add({
		element: this.panel,
		type: "mousedown",
		handler: this.DragPanel,
		context: this
	});
	Events.add({
		element: document,
		type: "mouseup",
		handler: this.DropPanel,
		context: this
	});
	Events.add({
		element: document,
		type: "mousemove",
		handler: this.MovePanel,
		context: this
	});
	Events.add({
		element: this.reportLink,
		type: "click",
		handler: this.ShowReportErrorPanel,
		context: this
	});
	Events.add({
		element: this.capIQReportLink,
		type: "click",
		handler: this.ShowReportErrorPanel,
		context: this
	});	
	Events.add({
		element: this.reportLink1,
		type: "click",
		handler: this.ShowReportErrorPanel,
		context: this
	});
	Events.add({
		element: this.closeBtn,
		type: "click",
		handler: this.HideReportErrorPanel,
		context: this
	});
	Events.add({
		element: this.cancelBtn,
		type: "click",
		handler: this.HideReportErrorPanel,
		context: this
	});
	Events.add({
		element: this.submitBtn,
		type: "click",
		handler: this.CheckFormAndSubmit,
		context: this
	});
	Events.add({
		element: this.anotherLink,
		type: "click",
		handler: this.ResetForm,
		context: this
	});
	Events.add({
		element: this.doneLink,
		type: "click",
		handler: this.HideReportErrorPanel,
		context: this
	});
	Events.add({
		element: this.inSection,
		type: "mousemove",
		handler: this.DropPanel,
		context: this
	});
	Events.add({
		element: this.inDataPoint,
		type: "mousemove",
		handler: this.DropPanel,
		context: this
	});
	Events.add({
		element: this.inYourName,
		type: "mousemove",
		handler: this.DropPanel,
		context: this
	});
	Events.add({
		element: this.inYourEmail,
		type: "mousemove",
		handler: this.DropPanel,
		context: this
	});
	Events.add({
		element: this.inDescribe,
		type: "mousemove",
		handler: this.DropPanel,
		context: this
	});
}
reportError.prototype.ShowReportErrorPanel = function () {	
	if (this.panel.style.display != "block") {
		var scrollTop = GetScrollTop();
		var top = scrollTop + 100;
		var left = 300; //window.scrollX
		this.panel.style.top = top + "px";
		this.panel.style.left = left + "px";
		this.panel.style.display = "block";
	}
}

reportError.prototype.ResetForm = function() {
	this.ErrorReset();
	$("#reportErrorPanel input").val("");
	$("#reportErrorPanel textArea").val("");
	var inputAttrValue = $("#companyName").attr("data-default");
	$("#companyName").val(inputAttrValue);
	
	if (this.submitDiv.style.display == "block") {
		this.submitDiv.style.display = "none";
		this.formDiv.style.display = "block";
	}
}

reportError.prototype.ErrorReset = function() {
	this.errors = [];
	MODElement.removeChildNodes(this.errorList);
	this.errorAnnouncePanel.style.display = "none";
}

reportError.prototype.HideReportErrorPanel = function() {
	if (this.panel.style.display != "none") {
		this.panel.style.display = "none";
		this.ResetForm();
	}
}

reportError.prototype.CheckFormAndSubmit = function () {
	this.ErrorReset();
	var ct = 0;

	for (var key in this.fields) {
		var asterick = MODElement.create("span", { className: "formAsterick" }, '*');

		if (this.fields[key] && this.fields[key].inputEl && !this.fields[key].inputEl.value && key != "typeOfData") {
			if (ct == 0) {
				MODElement.addChild(this.errorList, this.fields[key].label);
			} else {
				MODElement.addChild(this.errorList, ", " + this.fields[key].label);
			}
			this.errorList.appendChild(asterick);
			if (this.fields[key].labelEl != null && typeof this.fields[key].labelEl != "undefined") {
				this.fields[key].labelEl.className = "errorLabel";
			}

			ct++;
		} else if (key == 'yourEmail' && !this.ValidateEmail(this.fields[key].inputEl.value)) {
			if (ct == 0) {
				MODElement.addChild(this.errorList, this.fields[key].label);
			} else {
				MODElement.addChild(this.errorList, ", " + this.fields[key].label);
			}
			this.errorList.appendChild(asterick);
			this.fields[key].labelEl.className = "errorLabel";
			ct++;
		} else if (key == "yourPhone" && !this.fields[key].inputEl.value){
			if (ct == 0) {
				MODElement.addChild(this.errorList, this.fields[key].label);
			} else {
				MODElement.addChild(this.errorList, ", " + this.fields[key].label);
			}
			this.errorList.appendChild(asterick);
			if (this.fields[key].labelEl != null && typeof this.fields[key].labelEl != "undefined") {
				this.fields[key].labelEl.className = "errorLabel";
			}

			ct++;
		} else {
			try {
				if (key == "typeOfData") {					
					this.formData[key] = { label: this.fields[key].label, value: $("#typeOfData option:selected").text() };
				} else {
					this.formData[key] = { label: this.fields[key].label, value: this.fields[key].inputEl.value };
				}
				if (this.fields[key].labelEl.className == "errorLabel") {
					this.fields[key].labelEl.className = "";
				}
			} catch (e) { }
		}
	}

	if (ct > 0) {
		this.errorAnnouncePanel.style.display = "block";
	} else {
		var dataStr = '';
		var ct = 0;

		for (var key in this.formData) {
			if (ct == 0) {
				dataStr = dataStr + this.formData[key].label + '::' + this.formData[key].value;
			} else {
				dataStr = dataStr + '|' + this.formData[key].label + '::' + this.formData[key].value;
			}
			ct++;
		}

		var self = this;

		self.formDiv.style.display = "none";

		var env = $("body").attr("data-env");

		$.ajax({
			type: "POST",
			url: (env == "Development" ? "/businessweek" : "") + "/research/common/buffer/reporterror_buffer.asp",
			data: { formdata: dataStr, fromurl: escape(String(window.location)) },
			success: function (html) {
				if (html == "true") {
					self.formDiv.style.display = "none";
					self.submitDiv.style.display = "block";
				}
			}
		});
	}
}

reportError.prototype.ValidateEmail = function(email) {
	var isValid = false;
	
	var filter  = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	if (filter.test(email)) {
		isValid = true;
	}
	
	return isValid;
}

reportError.prototype.SubmitSuccess = function(buffer) {
	var result = buffer.getResult();
	if (result == "true") {
		this.formDiv.style.display = "none";
		this.submitDiv.style.display = "block";
	}
}

reportError.prototype.SubmitError = function (buffer) {
	alert('test');

}

reportError.prototype.DragPanel = function(ev, el) {

	var scrollTop = GetScrollTop();

	this.panelX = parseInt(el.style.left);
	this.panelY = parseInt(el.style.top);    

	this.clickX = ev.nativeEvent.clientX;
	this.clickY = ev.nativeEvent.clientY + scrollTop;    

	this.inFromLeftDis = this.clickX - this.panelX;
	this.inFromTopDis = this.clickY - this.panelY;

	this.shouldDrag = true;
}
reportError.prototype.DropPanel = function(ev, el) {
	this.shouldDrag = false;
}

reportError.prototype.MovePanel = function(ev, el) {
	if (this.shouldDrag) {
		var scrollTop = GetScrollTop();

		var x = ev.nativeEvent.clientX - this.inFromLeftDis;
		var y = (ev.nativeEvent.clientY + scrollTop) - this.inFromTopDis;
		if (this.clickX < this.panelX) {
			x = this.panelX + 20;
		}
		if (this.clickY < this.panelY) {
			y = this.panelY + 20;
		}                

		this.panel.style.left = x + "px";
		this.panel.style.top = y + "px";  
	}
}

function InitReportError() {
	try {
		var error = new reportError();
		error.AttachEvents();
	} catch(e) {
		
	}
}

Events.add({
	element: window,
	type: 'load',
	handler: InitReportError
});