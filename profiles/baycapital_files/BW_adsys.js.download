var BW_company = 'mgh';
var BW_division = 'bw';
var BW_adServer = '5262';
var BW_site = ''; //Channel (Site) Name
var BW_zone = ''; //Subchannel (Zone) Name
var BW_sitezone;
var BW_sector; 
var BW_size;
var BW_page = '/';
var BW_host = location.hostname.toLowerCase();
var BW_url = location.href;
var BW_queryRaw = location.search.substring(1); //Raw query string code
var BW_queryEscape = BW_queryRaw && unescape(BW_queryRaw);
var BW_query = BW_queryRaw; //Get query string
var BW_queryList = BW_queryRaw && BW_queryRaw.split('&');
var BW_isDebug = (/debug/i.test(BW_query));
var BW_env_ua = navigator.userAgent.toLowerCase(); //User-Agent
var BW_rn = ('1' + ('' + Math.random()).substring(2, 11));
var RANDOM_NUMBER = ('1' + ('' + Math.random()).substring(2, 11));

var BW_meta = (document.getElementsByTagName) ? document.getElementsByTagName("meta") : null;

var BW_siteList = [

  //Host                        Site
  ['bwads.businessweek.com',    'test'],
  ['bw1ads.businessweek.com',   'test1'],
  ['bw2ads.businessweek.com',   'test2'],
  ['bw3ads.businessweek.com',   'test3']
];

function BW_adsys_init() {
  BW_adsys_setTemp();
  BW_adsys_intervalId = setInterval(BW_adsys_interval, 250);
}

var BW_adsys_target = '_blank';
var BW_adsys_baseUrl = 'http://ad.doubleclick.net/N5262/';
var BW_adsys_isRich = (!(/mozilla\/3/.test(BW_env_ua) || (/webtv/.test(BW_env_ua)))); //Browser is not mozilla 3 or not WebTv
var BW_adsys_genCode; //Temp global holder of generated ad code
var BW_adsys_template; //Ad template number
var BW_adsys_defaultSite = 'general'; //Value used when site is not available
var BW_adsys_defaultZone = 'general'; //Value used when zone is not available
var BW_adsys_isSiteListChecked = false; //Flag to determine if BW_siteList checking was conducted
var BW_adsys_intervalId; //Id used to cancel any setTimout or setInterval threads

//Lists all ads within current web page. Will be populated during runtime.
var BW_adsys_adList = [ 
  //Position:0    Source File:1    Size:2    Tile:3    Url:4    Generated Code:5    Ticker:6
];

//Lists all possible ad positions within ad system. This list provides default properties for each ad position. This list is static.

//Removed_ads for GPT
//  position4:   {s: '468x60',                   n: 'Position4',    desc: 'Reader comments sponsorships. Within story pages.'}
// z02:         {s: '468x60,1x1',               n: 'Z02',          desc: 'Broker box. Companies channel.'},
var BW_adsys_posList = {

  //Position   Default Size                    Name               Description
  top:         {s: '728x90,970x66,1x1',            n: 'Top',          desc: 'Old pos10, Sizes: 728x90, 468x60'},
  specialtop:  {s: '960x90,980x115,728x90,980x250,980x115,980x418,980x66,980x110,1x1',       n: 'SpecialTop',   desc: 'Special top ad below header navigation'},
  top1:        {s: '88x31',                    n: 'Top1',         desc: ''},
  top2:        {s: '88x31',                    n: 'Top2',         desc: 'Sizes: 88x31, 120x15'},
  top3:        {s: '88x31',                    n: 'Top3',         desc: 'pos8, email a story(88x31)'},
  topleft:     {s: '1x1',                      n: 'TopLeft',      desc: ''},
  topright:    {s: '400x45,1x1',               n: 'TopRight',     desc: 'Sponship box with fixed size'},
  middle:      {s: '300x250',                  n: 'Middle',       desc: 'Right hand column in all pages. Middle ad in column (used when there are 3 - 300x250\'s or only 1-300x250).'},
  middle1:     {s: '120x40',                   n: 'Middle1',      desc: 'Story tools sponsorship. Middle1,(300x200)'},
  middle2:     {s: '120x60',                   n: 'Middle2',      desc: 'Forums, eBooks.'},
  middle3:     {s: '88x31',                    n: 'Middle3',      desc: 'Legacy printer friendly'},
  left:        {s: '120x90',                   n: 'Left',         desc: 'Left navigation column.'},
  left1:       {s: '300x25',                   n: 'Left1',        desc: 'Home page. Left column. First ad. Under Market info module'},
  circ:        {s: '300x60',                   n: 'Circ',         desc: 'Circulation and subscription sponsorship'},
  circfooter:  {s: '980x70',                   n: 'CircFooter',   desc: 'Circulation and subscription sponsorship above the footer'},
  right:       {s: '160x600',                  n: 'Right',        desc: 'Right hand column. Sizes: 140x800, 120x600, 160x600'},
  right1:      {s: '88x31',                    n: 'Right1',       desc: 'Legacy marketinfo box'},
  right2:      {s: '300x250,300x500,300x600',  n: 'Right2',       desc: 'Right hand column in all pages. Top ad in column. Old pos9.'},
  right3:      {s: '300x250,1x1',              n: 'Right3',       desc: 'Old pos9.'},
  bottom:      {s: '150x1',                    n: 'Bottom',       desc: 'Text ad lower right. Placed under Bottom1 and Bottom2.'},
  bottom1:     {s: '120x60',                   n: 'Bottom1',      desc: 'Old pos8. Left ad of pair. Lower right of page. Sizes: 120x40, 120x60.'},
  bottom2:     {s: '120x60',                   n: 'Bottom2',      desc: 'Right ad of pair. Lower right of page.'},
  bottom3:     {s: '112x54',                   n: 'Bottom3',      desc: 'Fixed size. Placed in global nav. Available for sponsorship.'},
  bottomleft:  {s: '120x60',                   n: 'BottomLeft',   desc: ''},
  bottomright: {s: '120x40',                   n: 'BottomRight',  desc: 'Used within linkedIn widget'},
  frame1:      {s: '1x1',                      n: 'Frame1',       desc: 'Presitial, popups'},
  frame2:      {s: '1x1',                      n: 'Frame2',       desc: 'Out-of-banner, pop under (no inline positioning).'},
  position1:   {s: '1x1',                      n: 'Position1',    desc: ''},
  position3:   {s: '1x1',                      n: 'Position3',    desc: ''},
  x01:         {s: '120x60,1x1',               n: 'X01',          desc: 'Broker box. Companies channel (far left)'},
  x02:         {s: '120x60,1x1',               n: 'X02',          desc: 'Broker box. Companies channel (left)'},
  x03:         {s: '120x60,1x1',               n: 'X03',          desc: 'Broker box. Companies channel (right)'},
  x04:         {s: '120x60,1x1',               n: 'X04',          desc: 'Broker box. Companies channel (far right)'},
  z01:         {s: '300x100',                  n: 'Z01',          desc: 'Special position for home page'},
  interstitial: {s: '640x480',            n: 'Interstitial',      desc: 'Interstitial Ad'},
  vp_undergrad:   {s: '300x250',    n: 'vp_undergrad',  desc: 'Veritas Prep'},
  bschool_forums: {s: '300x250,300x600,1x1',       n: 'bschool_forums',    desc: 'Veritas Prep For Forum'},
  industry_module:   {s: '300x100',               n: 'Industry_Module', desc: 'Industry Module on Companies Channel Right Rail'}
};

//Lists all current ad templates within ad system. This list is static.
var BW_adsys_tempList = [


  {
    n: 0, 
    desc: 'Represents all pages that can not be identified as any particular template.'
  },
  {
    n: 1, 
    posList: [
      'Right2,Right3,Top,TopRight,CircFooter', 
      'Right2,Right3,Frame1,Top,TopRight,CircFooter', 
      'Top,Right2,Right3,TopRight,CircFooter'
    ], 
    desc: 'Home and Search template types'
  },
  {
    n: 2, 
    posList: 'Middle1,Right2,Right3,Bottom1,Bottom2,Bottom,Position4,Frame1,Top,TopRight,CircFooter', 
    desc: 'Article template type'
  },
  {
    n: 3, 
    posList: 'Top,z02,x01,x02,x03,x04,Right2,Right3,TopRight,CircFooter',
    desc: 'Companies template type.'
  },
  {
    n: 4,
    desc: 'Newsletter template type'
  },
  {
    n: 5,
    posList: [
      'Top,Right2,TopRight,CircFooter',
      'Top,Circ,Right2,TopRight,CircFooter',
      'Top,Middle,TopRight,CircFooter',
      'Top,Circ,Middle,TopRight,CircFooter'
    ],
    desc: 'Slideshow template type'
  }
];

//Set the template type for web page. If function can not determine template type then default 0 type is given.
function BW_adsys_setTemp() {
  
  var sLP /*stringListPos*/, aTL /*arrayTemplateList*/, xPL /*variablePosList*/;
  
  aTL = BW_adsys_tempList; //Assign template list to local var
  
  //Check for any existing positions listing
  if (window.BW_listpos) { 
    sLP = BW_listpos.toLowerCase();
  } else if (window.OAS_listpos) { //Check for OAS_listpos legacy positions list
    sLP = OAS_listpos.toLowerCase();
  }
  
  //Process template type
  if (sLP) { 
    for (var i in aTL) { //Loop through all template types
      if (aTL[i]['posList']) { //posList property exists for template type
        xPL = aTL[i].posList; //Assign posList property to local var
        if (typeof(xPL) == 'object' && xPL.constructor == Array) { //posList property is an array
          for (var j in xPL) { //Loop through posList array
            if (xPL[j].toLowerCase() == sLP) { //Successful match
              BW_adsys_template = aTL[i].n; //Assign template number
              return;
            }
          }
        } else { //posList assumed string data type
          if (xPL.toLowerCase() == sLP) { //Successful match
            BW_adsys_template = aTL[i].n; //Assign template number
            return;
          }
        }
      }
    }
  } 
  
  //All above failed so set default template number
  BW_adsys_template = 0;
}


function BW_adsys(sPos, sSourceFile, sSize, sReturnType) {
  var $sFunc = 'BW_adsys'; //Special String Function: Represents the function name as string datatype
  var sMsg, oPos, sCode;
  var LEN_IS_ARRAY = 7;

  if (!sPos) { 
    throw new Error($sFunc + '(): Position argument (sPos) does not exist.');
    return '';
  }
  
  oPos = BW_adsys_posList[sPos.toLowerCase()] || null; //Use sPos object within Position List if it exists otherwise set to null  

  if (!oPos) {
    throw new Error($sFunc + '(): ' + sPos + ' does NOT exist within Ad System Position List.');
    return '';
  }
  
  sSourceFile = sSourceFile || ''; //Use sSourceFile if it exists otherwise set empty string.

  //Use sSize if it exists or use default size from position list
  if (!sSize){ 
    var adSizes = oPos.s.split(","); 
    var adList = [];
    var adSize = "";
    for (var i = 0; i < adSizes.length; ++i) {
      adSize = adSizes[i].split("x");

      adList.push([parseInt(adSize[0]), parseInt(adSize[1])]);
    }
    sSize = adList;
  }
  else{
    sSize = sSize;
  }
  
  sReturnType = sReturnType || ''; //Use sReturnType if it exists otherwise set empty string.

  sCode = BW_adsys_addAd(oPos, sSourceFile, sSize, sReturnType);

  //Assign ad position debug info
  if (BW_isDebug) {
    sCode += BW_adsys_debug(oPos, sSourceFile, sSize);
  }
  
  return sCode;
}

function BW_adsys_addAd(oPos, sSourceFile, sSize, sReturnType) {

  var sCode = '', sDefault, sBaseKeys = '', iTile, sScriptUrl, sBasicLinkUrl, sBasicImgUrl, sPosName, iTemp, sSite, sZone, rSlash, aQuery, sQuery, sTicker;

  sPosName = oPos.n.toLowerCase();  
  iTile = BW_adsys_adList.length + 1;
  iTemp = BW_adsys_template || 0;
  
  //Generate Site & Zone
  if (!BW_sitezone) { //Sitezone is not populated. This means this is the first call to this function. 
    rSlash = (/^\/|\/$/g); //Pattern to identify begining and trailing slash '/' characters
    if (!BW_site) { //Site has no value. Assign default value
      sSite = BW_adsys_defaultSite;
    } else if (/\//.test(BW_site)) { //Site contains '/'. Multiple level site value
      sSite = BW_site.replace(rSlash, ''); //Remove begining and trailing '/' characters. Ex: '/autos/specialreport/hybridbuying/'
    } else {
      sSite = BW_site;
    }
    
    if (!BW_zone) {
      sZone = BW_adsys_defaultZone;
    } else if (/\//.test(BW_zone)) {
      sZone = BW_zone.replace(rSlash, ''); //Remove begining and trailing '/' characters. Ex: '/tech/internet'
    } else {
      sZone = BW_zone;
    }
    
    BW_sitezone = sSite + '/' + sZone; //Example: tech/ceotechguide
  }
  
  //Special code to change site if current host matches site list
  if (!BW_adsys_isSiteListChecked) { //The site list has NOT been checked yet
    for (var i in BW_siteList) {
      if (BW_host.match(BW_siteList[i][0])) { //Test if code string is contained within host string
        BW_sitezone = BW_sitezone.replace(/\w+\//, BW_siteList[i][1] + '/'); //Replace site portion within BW_sitezone with site from BW_sitelist
        break;
      }
    }
    BW_adsys_isSiteListChecked = true;
  }
  
  //Generate base keys
  var sector_code = "";
  var industry_code = "";
  var sorround_id = "";
  var companies_mentioned = "";
  var krux_values = "";
  sBaseKeys += 'url=' + location.pathname + ';'; //URL path
   
  if (window.s_sectorCode) { //Sector code exists
    sector_code = 'sectr=' + s_sectorCode + ';';
  }
  
  if (window.s_industryCode) { //Industry code exists
     industry_code = 'indus=' + s_industryCode + ';';
  }
  
  if (window.surroundId) { //Surround session ID exists
    sorround_id  = 'srnd=' + surroundId + ';';
  }
  
  if (typeof  BW_Keyword !== "undefined")  { // companiesmentioned exists
    companies_mentioned = 'keyword=companiesmentioned;';
  }

 if (typeof  Krux.dfppKeyValues !== "undefined") {
   krux_values = Krux.dfppKeyValues ;
 }
  
  if (window.BW_query) { //Query string exists
    if (/(ric)|(privcapid)|(textin)|(ticker)\=/i.test(BW_query)) { //Specific Query Names Exist
      for (var j in BW_queryList) {
        aQuery = BW_queryList[j].split('=');
        if (aQuery.length > 1) { //Check to make sure query has a value
          sQuery = aQuery[0].toLowerCase(); //Assign query name to local var
          if (sQuery == 'ric' || sQuery == 'privcapid' || sQuery == 'textin' || sQuery == 'ticker') { //Specific Query names exist
            sTicker = aQuery[1].split('.')[0]; //Keep only text before dot (.) if it exists.
            break;
          }
        }
      }
      tickers = (sTicker) ? 'tickr=' + escape(sTicker) + ';' : '';
    }
  }

var BW_adSite = '/' + BW_adServer + '/' + BW_company + '.' + BW_division + '.' + BW_sitezone;

googletag.cmd.push(function() {
    var adSlot = googletag.defineSlot(BW_adSite, sSize, "ad-" + sPosName);
    adSlot.addService(googletag.pubads());
    adSlot.setTargeting('sz', sSize);
    adSlot.setTargeting('tile', iTile);
    adSlot.setTargeting('krux', krux_values);
    adSlot.setTargeting('keyword', companies_mentioned);
    adSlot.setTargeting('page', 't' + iTemp);
    adSlot.setTargeting('t' + iTemp, sPosName);
    adSlot.setTargeting('tickr', escape(sTicker));
    adSlot.setTargeting('sectr', sector_code);
    adSlot.setTargeting('url', location.pathname);
    adSlot.setTargeting('indus', industry_code);
    adSlot.setTargeting('u', 'sz=' + sSize + '|'+ '|' + 'page=t' + iTemp + '|' + 't' + iTemp + '=' + sPosName + '|' + 'sectr=' + sector_code + '|' +'indus=' + industry_code +  '|');
    googletag.pubads().collapseEmptyDivs();
    googletag.enableServices();
  });

  sCode = '<div id="ad-' + sPosName + '" class="gpt-ad">' + sCode + '<\/div>'; //Ad wrapper element to help identify ad position in page //i47:ttm
  
  return sCode;
}

//Used to display debugging info for an ad position
function BW_adsys_debug(oPos, sSourceFile, sSize) {

  var sCode = '', d1 = '<div style="height: auto; font-size: 11px;">', d2 = '<\/div>'; 
  var aAL = BW_adsys_adList[BW_adsys_adList.length-1]; //Add current ad details to local variable
  var sWidth = (/x01|x02|x03|x04/i.test(oPos.n)) ? 'width: 118px;' : 'width: 98%;';

  sCode += '<div id="AdCode-Debug-' + oPos.n + '" style="border: 1px solid #6699ff; background-color: #fff; overflow: auto; margin-top: 1px; font-size: 11px; text-align: left; ' + sWidth +'">';
  sCode += '<table style="margin: 0px; padding: 0px; border-collapse: collapse; width: 100%;">';
  sCode += '<tbody><tr>';
  sCode += '<td style="padding: 5px; background: #6699ff; font-weight: bold; font-size: 12px;">Ad Code - Debug Info<\/td>';
  sCode += '<\/tr><tr><td style="padding: 10px;">';
  sCode += d1 + '<b>Position: <\/b>' + oPos.n.toLowerCase() + d2;
  sCode += d1 + '<b>Size: <\/b>' + sSize + d2;
  sCode += d1 + '<b>Tile: <\/b>' + aAL[3] + d2;
  if (sSourceFile) {
    sCode += d1 + '<b>Source File: <\/b><a href="' + sSourceFile + '" target="_blank">' + sSourceFile + '</a>' + d2;
  }
  sCode += d1 + '<b>Description: <\/b>' + oPos.desc + d2;
  sCode += d1 + '<b>Template: <\/b>' + BW_adsys_template + d2;
  sCode += d1 + '<b>SiteZone: <\/b>' + BW_sitezone + d2;
  if (window.s_sectorCode) {
    sCode += d1 + '<b>Sector Code: <\/b>' + window.s_sectorCode + d2;
  }
  if (window.s_industryCode) {
    sCode += d1 + '<b>Industry Code: <\/b>' + window.s_industryCode + d2;
  }
  if (typeof  BW_Keyword !== "undefined")  { 
    sCode += d1 + '<b>keyword=companiesmentioned <\/b>' + d2;
  }
  if (aAL[6]) { //Ticker exists
    sCode += d1 + '<b>Ticker: <\/b>' + aAL[6] + d2;
  }
  sCode += d1 + '<b>Query: <\/b>' + BW_query + d2;
  sCode += d1 + '<b>Random #: <\/b>' + BW_rn + d2;
  sCode += d1 + '<b>Generated Code: <\/b>' + d2;
  sCode += d1 + '<a href="' + aAL[4] + '" target="_blank">' + (aAL[5]).replace(/\</g,'&lt;').replace(/\>/g,'&gt;') + '</a>' + d2;
  sCode += '<\/td><\/tr><\/tbody><\/table>' + d2;
  
  return sCode;
}

//Function to set the id and class of an ad position so it can be properly identified and styled
BW_adsys_setAdStyle = function (sAd) {
  
  var onAd, onAdWrap, oErr, sAttr, fFunc = arguments.callee;
  
  try {
    onAd = document.getElementById('ad-' + sAd);
  } catch (oErr) { //Handle exception
    return null;
  }
  if (onAd) { //Ad position exists
    onAdWrap = onAd.parentNode; //Get ad parent. Usually a div wrapper
    sAttr = onAdWrap.getAttribute('class');
    if (/ad/i.test(sAttr)) { //Element has class of ad
      onAdWrap.setAttribute('class', sAttr + ' mod'); //Add special class to identify element been modified
      if (!onAdWrap.getAttribute('id')) { //Element id does not exist
        onAdWrap.setAttribute('id', 'ad-top-wrapper');
      }
    }
    fFunc.stop = true;
  }
};

BW_adsys_setAdStyle.stop = false;

//Function that gets called repeatedly until page finishes loading
BW_adsys_interval = function () { 
  if (!('bw' in window && bw.cfg && bw.cfg.setAdStyle === false) && !BW_adsys_setAdStyle.stop) { //Check for setAdStyle flag and if setAdStyle stop flag is true
    BW_adsys_setAdStyle('top');
  } 
};

//Function that is called when page is finished loading
BW_adsys_onLoad = function () {
  clearInterval(BW_adsys_intervalId);
};

(function() {
  if (window.addEventListener) {
    window.addEventListener('load', BW_adsys_onLoad, false);
  } else if (window.attachEvent) {
    window.attachEvent('onload', BW_adsys_onLoad);
  } else {
    if (typeof(window.onload) != 'function') {
      window.onload = BW_adsys_onLoad;
    } else {
      var fOnload = window.onload;
      window.onload = (function () { fOnload(); BW_adsys_onLoad(); });
    }
  }
})();

//==============================================================================
// Initialize / Finalize
//==============================================================================

BW_adsys_init(); //Initialize

$(document).ready(function(){
  $.each($('.gpt-ad'), function(index, element){
    googletag.cmd.push(function() { googletag.display(element.id); });
  });
});

$(window).load(function(){
	$.each($('.gpt-ad'), function(index, value) 
	{
		if ($(value).css('display') == 'none'){
			$(value).parent().parent().css({'border':'none'});
		}
	});
});