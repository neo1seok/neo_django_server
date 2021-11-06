function show_input_enable(check_enable_id,input_class,is_enable){
    console.log('show_input_enable',check_enable_id,input_class,is_enable);
    var obj = $('.'+input_class )
    $('#'+check_enable_id).prop('checked',is_enable);

    if(is_enable){
        obj.removeAttr('disabled');
    }
    else{
        obj.attr('disabled', '');
    }
    return is_enable;

}

function get_input_enable(input_class){
    console.log('get_input_enable');
    var obj = $('.'+input_class )
    return obj.hasAttr('disabled');
}


function temp_query(url,data,
ok_process= (response) => {console.log("ok",response);},
headers={},
fail_process=function(response) {console.log("fail",response);},
err_process=function(error) {"error",console.log(error);})
{
    var sid = get_session_uid();
    data['sid'] = sid;
    console.log("query",url,sid);
    var query_time = get_cur_time()

    $.ajax({
        url: url,
         headers:headers,
        data: data,
        type: 'POST',
        dataType: "json",
        success: function(response) {
            response["taken_time"]=get_cur_time()-query_time;
            console.log("response",response);
            console.log("taken_time",response["taken_time"]);

            if(response.result == "OK"){
                ok_process(response);

            }
            else{
                console.log("fail_process");

                fail_process(response);
            }
            //console.log(response);

        },
        error: err_process
    });

}

function exception_process(response) {

    console.log("err",response.error);
    alert(response.error);
}

function confirm_form(form_id,url,msg="'변경하시겠습니까?'"){
    console.log("btn_confirm",$('#'+form_id).serializeArray());
    if(!confirm(msg)) return ;

    temp_query(url,$('#'+form_id).serializeArray(),function(response){
        console.log("confirm ok aaaa");
        location.reload();
    },exception_process,exception_process)

}

function sha256_from_hexstr(hex_str){
  var str = hex2a(hex_str);
  console.log(str);

  //
  return Sha256.hash(hex_str,{ msgFormat: 'hex-bytes', outFormat: 'hex' });
	//return crypto_util.sha256(neoutil.Text2HexString(passwd) + rn)
}


function toHex(str) {
  var result = '';
  for (var i = 0; i < str.length; i++) {
    result += str.charCodeAt(i).toString(16);
  }

  return result.toUpperCase();
}

function hex2a(hexx) {
  var hex = hexx.toString(); //force conversion
  var str = '';
  for (var i = 0; i < hex.length; i += 2)
    str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
  return str;
}
function get_cur_time(){
    var d = new Date();
    var n = d.getTime();
    return n;
}
function get_session_uid(){
    var n = get_cur_time();
    return "sid"+n;
}

function reset_message(){
console.log('reset_message');
$('#id_alert').hide();
$('#id_warning').hide();
$('#id_alert > strong').text('');
$('#id_warning > strong').text('');

}

function show_message(id,msg){
console.log('show_message',$('#'+id ));
$('#'+id ).show();
$('#'+id +" > strong").text(msg);

}

function show_dev(id) {

    var x = $("#"+id);
    console.log(x);
    if (! x.hasClass( "w3-show" )) {
        x.addClass("w3-show");
    }

//    else {
//        x.removeClass("w3-show");
//    }
}


function download_url(filename, url) {
    var element = document.createElement('a');
    element.setAttribute('href', url);
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function download_text(filename, text) {
  download_url(filename,'data:text/plain;charset=utf-8,' + encodeURIComponent(text));



}

function setCookie(cookie_name, value, days) {
  var exdate = new Date();
  exdate.setDate(exdate.getDate() + days);
  // 설정 일수만큼 현재시간에 만료값으로 지정

  var cookie_value = escape(value) + ((days == null) ? '' : ';    expires=' + exdate.toUTCString());
  document.cookie = cookie_name + '=' + cookie_value;
}

function getCookie(cookie_name) {
  var x, y;
  var val = document.cookie.split(';');
//test
  for (var i = 0; i < val.length; i++) {
    x = val[i].substr(0, val[i].indexOf('='));
    y = val[i].substr(val[i].indexOf('=') + 1);
    x = x.replace(/^\s+|\s+$/g, ''); // 앞과 뒤의 공백 제거하기
    if (x == cookie_name) {
      return unescape(y); // unescape로 디코딩 후 값 리턴
    }
  }
}
function addCookie(id) {
  var items = getCookie('productItems'); // 이미 저장된 값을 쿠키에서 가져오기
  var maxItemNum = 5; // 최대 저장 가능한 아이템개수
  var expire = 7; // 쿠키값을 저장할 기간
  if (items) {
    var itemArray = items.split(',');
    if (itemArray.indexOf(id) != -1) {
      // 이미 존재하는 경우 종료
      console.log('Already exists.');
    }
    else {
      // 새로운 값 저장 및 최대 개수 유지하기
      itemArray.unshift(id);
      if (itemArray.length > maxItemNum ) itemArray.length = 5;
      items = itemArray.join(',');
      setCookie('productItems', items, expire);
    }
  }
  else {
    // 신규 id값 저장하기
    setCookie('productItems', id, expire);
  }
}

function open_with_dlg(btn_prefix){
    console.log("option ",g_option);
    ck_open_dlg = getCookie("open_dlg");
    console.log("ck_open_dlg ",ck_open_dlg);
    if(ck_open_dlg=='TRUE'){
        ck_cur_uid = getCookie("cur_uid");

        btnid = '#'+btn_prefix+ck_cur_uid;
        console.log("option open",btnid);
        console.log("cookie",document.cookie,ck_open_dlg);

        $(btnid).click();
        setCookie("open_dlg","",3);


    }
}

function copy_clipboard_from_input_id(input_id) {
  /* Get the text field */
  //var copyText = document.getElementById("myInput");
  var copyText = $('#'+input_id);

  /* Select the text field */
  //copyText.select();
  copyText.select();


  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Alert the copied text */
  //alert("Copied the text: " + copyText2.val());
}

function download_result(app_name,cur_uid,result="OK",sample_size=-1,type="csv"){

  if(cur_uid == null){
    alert("no select file");
    return;
  }
   // down_url = '/query_ext/'+app_name+'/download_result?cur_uid='+cur_uid+'&result='+result +'&sample_size='+sample_size;
    down_url = '/etc_ex/download_result?cur_uid='+cur_uid+'&result='+result +'&sample_size='+sample_size+'&type='+type;

    console.log("down_url",down_url,cur_uid);
    location.href = down_url;
}


function check_repeat(uid){
console.log('wki_uid',uid);
temp_query('/etc/check_repeat', {
        cur_uid: uid,
      }, function(response) {
        console.log(response);
        alert(response.msg);



      }
      , function(error) {
        console.log(error);
      }

)
}

function download_project_result(handler_name,cur_uid,extra_test_code_ctn_uid){

if(cur_uid == null){
    alert("no select file");
    return;
  }
   // down_url = '/query_ext/'+app_name+'/download_result?cur_uid='+cur_uid+'&result='+result +'&sample_size='+sample_size;
    down_url = '/etc_ex/download_project_result?cur_uid='+cur_uid+'&handler_name='+handler_name+'&extra_test_code_ctn_uid='+extra_test_code_ctn_uid;

    console.log("down_url",down_url,cur_uid);
    location.href = down_url;


}

function search_by_runtime(tr_class_selector){


$("#id_name_search").on("keyup", function() {
    var text = $(this).val()

    $(tr_class_selector).each(function(idx,e){
// >button .dropdown-toggle
        var name = $(this).find( 'td > div > button' ).text();
        console.log('work_list',name);
        if(name.toLowerCase().includes(text.toLowerCase())){
            $(this).show();
        }
        else{
            $(this).hide();
        }

    });

    console.log('#id_name_search is now visible',text);

});



}


function base64ArrayBuffer(arrayBuffer) {
  var base64    = ''
  var encodings = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

  var bytes         = new Uint8Array(arrayBuffer);
  //new Uint8Array('FUCKTEST')
  var byteLength    = bytes.length
  var byteRemainder = byteLength % 3
  var mainLength    = byteLength - byteRemainder

  var a, b, c, d
  var chunk

  console.log('base64ArrayBuffer',byteLength,arrayBuffer.length,byteLength,typeof(arrayBuffer));

  // Main loop deals with bytes in chunks of 3
  for (var i = 0; i < mainLength; i = i + 3) {
    // Combine the three bytes into a single integer
    chunk = (bytes[i] << 16) | (bytes[i + 1] << 8) | bytes[i + 2]

    // Use bitmasks to extract 6-bit segments from the triplet
    a = (chunk & 16515072) >> 18 // 16515072 = (2^6 - 1) << 18
    b = (chunk & 258048)   >> 12 // 258048   = (2^6 - 1) << 12
    c = (chunk & 4032)     >>  6 // 4032     = (2^6 - 1) << 6
    d = chunk & 63               // 63       = 2^6 - 1

    // Convert the raw binary segments to the appropriate ASCII encoding
    base64 += encodings[a] + encodings[b] + encodings[c] + encodings[d]
  }

  // Deal with the remaining bytes and padding
  if (byteRemainder == 1) {
    chunk = bytes[mainLength]

    a = (chunk & 252) >> 2 // 252 = (2^6 - 1) << 2

    // Set the 4 least significant bits to zero
    b = (chunk & 3)   << 4 // 3   = 2^2 - 1

    base64 += encodings[a] + encodings[b] + '=='
  } else if (byteRemainder == 2) {
    chunk = (bytes[mainLength] << 8) | bytes[mainLength + 1]

    a = (chunk & 64512) >> 10 // 64512 = (2^6 - 1) << 10
    b = (chunk & 1008)  >>  4 // 1008  = (2^6 - 1) << 4

    // Set the 2 least significant bits to zero
    c = (chunk & 15)    <<  2 // 15    = 2^4 - 1

    base64 += encodings[a] + encodings[b] + encodings[c] + '='
  }

  return base64
}
