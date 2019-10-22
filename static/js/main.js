$(document).ready(function() {

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
    
    $(".btn-link").on("click", function(){
        $(this).find(".fa-caret-down").toggle();
        $(this).find(".fa-caret-up").toggle();
    });
    
});