$('document').ready(function() {
	$('document').ready(function() {
        $('#mastersupplier').click(function() {
          window.location="/i/ms/";
        });
        $('#masterpelanggan').click(function() {
          window.location="/i/mp/";
        });
        $('#masterbarang').click(function() {
          window.location="/i/mb/";
        });
        $('#viewmastersupplier').click(function() {
          window.location="/v/s/";
        });
        $('#viewmasterpelanggan').click(function() {
          window.location="/v/p/";
        });
        $('#viewmasterbarang').click(function() {
          window.location="/v/b/";
        });
        $('#exitwarning').click(function() {
          $('#exitwarning').hide(1000);
        })
      })
})