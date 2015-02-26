$(function() {

  $( '#ri-grid' ).gridrotator( {
      rows		: 3,
      columns		: 10,
      animType	: 'fadeInOut',
      animSpeed	: 1000,
      interval	: 600,
      step		: 1,
      w320		: {
        rows	: 3,
        columns	: 4
      },
      w240		: {
        rows	: 3,
        columns	: 4
      }
  } );

});
