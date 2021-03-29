$(document).ready(function () {

    // When choosing an acquirer, display its Pay Now button
    var $payment = $("#payment_method");
    $payment.on("click", "input[name='acquirer']", function (ev) {
            var payment_id = $(ev.currentTarget).val();
            $("div.oe_sale_acquirer_button[data-id]", $payment).addClass("hidden");
            $("div.oe_sale_acquirer_button[data-id='"+payment_id+"']", $payment).removeClass("hidden");
        })
        .find("input[name='acquirer']:checked").click();

    // When clicking on payment button: create the tx using json then continue to the acquirer
    $payment.on("click", 'button[type="submit"],button[name="submit"]', function (ev) {
        ev.preventDefault();
        ev.stopPropagation();
        var $form = $(ev.currentTarget).parents('form');
        var acquirer_id = $(ev.currentTarget).parents('div.oe_sale_acquirer_button').first().data('id');
        if (! acquirer_id) {
          return false;
        }
        odoo.jsonRpc('/shop/payment/transaction/' + acquirer_id, 'call', {}).then(function (data) {
            $('html,body').css('cursor', 'wait');
            var html_content = data.replace('<button', '<button disabled="disabled"').replace('</button>', '</button><div style="display: inline;"><img src="/web/static/src/img/throbber-large.gif" style="height: 34px;"/></div>');
            $form.html(html_content);
            $form.submit();
        });
    });

    $("#client_order_ref").find("[name='client_order_ref']").on('change', function () {
        odoo.jsonRpc("/shop/order/client_order_ref", 'call', {
            'client_order_ref': $(this).val(),
        });
    });

});
