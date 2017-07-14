var google_adnum = (!google_adnum)?0:google_adnum;
	
function google_ad_request_done(google_ads) {

var s = '';
var i;

if (google_ads.length == 0) {return;}


if (google_ads.length == 1) {

   s += '<div class="module textAd"><h2><a href=\"' + google_info.feedback_url + '\">Ads by Google<\/a><\/h2><ul>' +
 	'<li style="font-size:14px;line-height:1.4;text-align:center;margin:20px 0 20px 0;"><a href=\"' + google_ads[0].url + '\"> ' + google_ads[0].line1 + '<\/a><br \/>' +
   	'<span style="text-decoration:none;font-weight:normal;color:#333;"> ' +
	google_ads[0].line2 + '  ' + google_ads[0].line3 + '<\/span><br \/><a style="text-decoration:none;font-weight:normal;color:#007cd5;" href=\"' + google_ads[0].url + '\"">' +
	google_ads[0].visible_url + '<\/a><\/li><\/ul><\/div>';

}

if (google_ads.length > 1) {

   s += '<div class="module textAd"><h2><a href=\"' + google_info.feedback_url + '\">Ads by Google<\/a><\/h2><ul style="background-color:#F0F0F0;border:1px solid #E5E5E5;padding:5px;">';

for(i = 0; i < google_ads.length; ++i) {

   s += '<li><a href=\"' + google_ads[i].url + '\" style="color:#0000FF;"> ' + google_ads[i].line1 + '<\/a><br \/>' +
	'<span style="text-decoration:none;font-weight:normal;color:#000000;"> ' +
	google_ads[i].line2 + '  ' + google_ads[i].line3 + '<br \/><\/span><a style="color:#008000;text-decoration:none;font-weight:normal;"  href=\"' + google_ads[i].url + '\">' +
	google_ads[i].visible_url + '<\/a><\/li>';
	}

	s += '<\/ul><\/div>';

 }
 
 if (google_ads[0].bidtype == "CPC") {  /* insert this snippet for each ad call */
	google_adnum = google_adnum + google_ads.length;
	}

    document.write(s);
    return;
  }
google_ad_client = "pub-6185772592614621";
google_ad_channel = "4739791570+9704127894";
google_ad_output = 'js';
google_max_num_ads = '4';
google_ad_type = "text";
google_feedback = 'on';
google_skip = google_adnum;

document.write('<scr' + 'ipt type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"><\/scr' + 'ipt>');
