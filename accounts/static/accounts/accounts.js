
function check_length() {

    var pn = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];
    var en = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

    var cache =  $('#veri_code_input').val();
    for (var i = 0; i < 10; i++) {
        var regex_fa = new RegExp(pn[i], 'g');
        cache = cache.replace(regex_fa, en[i]);
    }
    $('#veri_code_input').val(cache);
    if($('#veri_code_input').val().length === 4){
        $('#code_register').removeAttr("disabled")
    }
    else {
         $('#code_register').prop( "disabled", true )
    }
}

function check_number (submit_id,mobile_inputted) {

    var pn = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];
    var en = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

    var cache =  $('#'+mobile_inputted).val();
    for (var i = 0; i < 10; i++) {
        var regex_fa = new RegExp(pn[i], 'g');
        cache = cache.replace(regex_fa, en[i]);
    }
    $('#'+mobile_inputted).val(cache);


        let num1 = $("#"+mobile_inputted).val();
        const pattern = /(0|)([ ]|-|[()]){0,2}9[0|1|2|3|4|9]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}/ig;
        if (pattern.test(num1) && 9<num1.length < 12) {
            $('#'+submit_id).removeAttr("disabled")
        }
        else{
             $('#'+submit_id ).prop( "disabled", true )
            }
    }

function check_pass_reset_match() {
    var pass_1 = $('#pass_1').val()
    var pass_2 = $('#pass_2').val()
    if (pass_1 == pass_2){
        $('#submit_pass_match').removeClass('d-none')
        }
    else{
         $('#submit_pass_match').addClass('d-none')

        }



}