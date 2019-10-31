$(document).ready(function() {

    // Show price of selected size for each item
    
    $("#size-select").change(function() {
        let selected_size = $(this).children("option:selected").val();

        var idArray = [];
        $('.product-price').each(function() {
            idArray.push(this.id);
        });
        
        $.each(idArray, function(i, val){
            if(val == selected_size) {
                $('.product-price').hide();
                $('#'+val).show();
            }
        });
    });
    
    // Toggle up and down caret on quote/order details
    
    $(".btn-link").on("click", function(){
        $(this).find(".fa-caret-down").toggle();
        $(this).find(".fa-caret-up").toggle();
    });
    
    // Real time calculator for superuser when entering price of commission
    // works
    
    $("#id_price_works, #id_price_travel").on("keyup keydown change", function(){
        let price_works = parseFloat($("#id_price_works").val());
        let price_travel = parseFloat($("#id_price_travel").val());
        if(isNaN(price_works)){
            price_works=0;
        }
        if(isNaN(price_travel)){
            price_travel=0;
        }
        $("#quote-total").text("Total: €" + (price_works+price_travel).toFixed(2));
    });
    
});