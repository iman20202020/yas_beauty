


   $("#category-form7-v").select(function(){
       $('#category-form7-v').empty();
       $.ajax({
            url: "{% url 'accounts:teacher_edit' %}",
            contentType: "json",
            data: {
                category_list: 1,
                  },
            success: function(result) {
                var i;
                for (i = 0; i<result.length; i++) {
                    optText = result[i]['category_name'];
                    optValue = result[i]['category'];
                    $('#syll').append(`<option value="${optValue}">${optText}</option>`);
                }
        }});
 })
      function show_confirm_key(){

          $('#confirm_edit_key').css('display','block');
          $('#teacher_search_key').css('display','none');
      }


          var learn_type_option=$('#learn_type-form7-v').find(":selected").val();

      if (learn_type_option == 1){
          $("#city_div").attr('hidden','hidden')
          }else {
          $("#city_div").removeAttr('hidden')
          }

          $("#learn_type-form7-v").change(function () {
              learn_type_option = $('#learn_type-form7-v').find(":selected").val()

              if (learn_type_option == 1) {

                  $("#city_div").attr('hidden', 'hidden')
              } else {
                  $("#city_div").removeAttr('hidden')

              }
          })

