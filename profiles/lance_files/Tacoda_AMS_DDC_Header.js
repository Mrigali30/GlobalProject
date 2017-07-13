//==============================================================================
// Title:       Global Header JavaScript
// Purpose:     Javascript code to be included at top of all web pages.
//==============================================================================

document.write('<scr'+'ipt type="text/javascript" src="http://static.btrd.net/common_scripts/jquery-1.5.min.js"><\/scr'+'ipt>');

//==============================================================================
// * (see also Tacoda_footer.js) install with channel map 06.19.07
//==============================================================================

var RANDOM_NUMBER = ("1"+(""+Math.random()).substring(2,11));

// comScore
(function() {
  var l = document.createElement('script');
  l.type = 'text/javascript';
  l.async = true;
  l.src = "http://static.btrd.net/js/bw_comscore.js";
  var s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(l,s);

  var googletag = googletag || {};
  googletag.cmd = googletag.cmd || [];
  var gads = document.createElement('script');
  gads.async = true;
  gads.type = 'text/javascript';
  gads.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'www.googletagservices.com/tag/js/gpt.js';
  var node = document.getElementsByTagName('script')[0];
  node.parentNode.insertBefore(gads, node);

})();

