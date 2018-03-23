$(document).ready(function(){          // when document is ready ....
  var form = $('#form_bying_product'); // choose a form to listen
  console.log(form)
  form.on('submit', function(e){   //adding listener on "Submit button"
    e.preventDefault();            // setup a page to prevent the default behavour (reload)
    console.log('123');
    var number = $('#number').val();     /// choose a number to listen !!!  by id <  $('#')
    console.log(number);
    var submit_btn = $('#submit_btn');
    var product_id = submit_btn.data('product_id');
    var product_name = submit_btn.data('name');
    var product_price = submit_btn.data('price')
    console.log(product_id);
    console.log(product_name);
    console.log(product_price);

        var data = {};
        data.name = product_name;
        data.number = number;
        data.price_per_item = product_price;
        var csrf_token = $('#form_bying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        console.log(data);

        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){       // if an answer was received from server //
              console.log("Okay :)");
              console.log(data.products_number_total)
              if (data.products_number_total){

                console.log(data.products_number_total)
                console.log(data.products)
                $('.basket-items ul').html("")
                $('#basket-total-number').text("("+data.products_number_total+")");
                $.each(data.products, function(key, value){
                  $('.basket-items ul').append('<li>'+value.product_name+', '+value.number+' pc. price: '+value.price_per_item+' uah.' +
                  //'<a class="delete-item" href=""> X </a>' +
                  '</li>');
                })

              }

            },
            error: function(){
              console.log("error :(");
            }
        })

    /**
    $('.basket-items ul').append('<li>'+product_name+', '+number+' pc. price: '+product_price+' uah.' +
    //'<a class="delete-item" href=""> X </a>' +
    '</li>');
    */

  });

  function showBasket(){
      //toggleClass function remove a class if it exists and add, if it doesn't
      $('.basket-items').toggleClass('hidden');
  };

  $('.basket-container').on('click', function(e){
    e.preventDefault();
    showBasket();
    //$(".basket-items").removeClass('hidden');
  });
  $('.basket-container').mouseover(function(e){
    e.preventDefault();
    showBasket();

  });
  $('.basket-container').mouseout(function(e){
    e.preventDefault();
    showBasket();
    //$(".basket-items").addClass('hidden');
  });

  $(document).on('click','.delete-item', function(e){
    e.preventDefault;
    $(this).closest('li').remove();
  })



});
