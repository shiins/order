//グローバル変数の定義
var listed_products = [];
var total_price = 0;

function AddToCart(b) {
  // 引数bは文字列になっている
  var product = {
    name: document.getElementById('name'+b).value,
    size: document.getElementById('size'+b).value,
    price: document.getElementById('price'+b).value,
    quantity: document.getElementById('quantity'+b).value,
  };
  //小計の計算
  var quantity = Number(product.quantity);
  var price = Number(product.price);
  total_price += quantity * price;
  //購入カートへの追加
  listed_products.push(product);

  //カートの表示文章
  var list = '';
  for(var i=0; i<listed_products.length; i++){
    list += listed_products[i].name + '(' + listed_products[i].size + ') ×' + listed_products[i].quantity + '<br>';
  }
  list += '合計金額：'+total_price;
  document.getElementById('list').innerHTML = list;

  //htmlコード
  var code = '';
  var code2 = '';

  //htmlでsubmitするためのform作成
  for(var i=0; i<listed_products.length; i++){
    code += '<input id="listed_name' + i + '" name="listed_name' + i + '">';
    code += '<input id="listed_size' + i + '" name="listed_size' + i + '">';
    code += '<input id="listed_price' + i + '" name="listed_price' + i + '">';
    code += '<input id="listed_quantity' + i + '" name="listed_quantity' + i + '">';
  }
  document.getElementById('code').innerHTML = code;

  //formへlisted_productsを代入
  for(var i=0; i<listed_products.length; i++){
    document.getElementById('listed_name'+i).value = listed_products[i].name;
    document.getElementById('listed_size'+i).value = listed_products[i].size;
    document.getElementById('listed_price'+i).value = listed_products[i].price;
    document.getElementById('listed_quantity'+i).value = listed_products[i].quantity;
  }

  //listed_productsの繰り返し回数を渡す
  code2 += '<input id="listed_products_length" name="listed_products_length">';
  document.getElementById('code2').innerHTML = code2;
  document.getElementById('listed_products_length').value = listed_products.length;
}

//カートを空にする
function DeleteCart(){
  listed_products = [];
  total_price = 0;
  document.getElementById('code').innerHTML = '';
  document.getElementById('code2').innerHTML = '';
  document.getElementById('list').innerHTML = '';
}

function InputForm(){
  let i = 0;
  while(true){
    if(!(document.getElementById('name'+i).value)){
      break;
    }
    document.getElementsByClassName('purchaser')[i].value = document.getElementById('purchaser').value;
    document.getElementsByClassName('email')[i].value = document.getElementById('email').value;
    document.getElementsByClassName('formed_name')[i].value = document.getElementById('name'+i).value;
    document.getElementsByClassName('formed_size')[i].value = document.getElementById('size'+i).value;
    document.getElementsByClassName('formed_price')[i].value = document.getElementById('price'+i).value;
    document.getElementsByClassName('formed_quantity')[i].value = document.getElementById('quantity'+i).value;
    i++;
  }
}

// Enterキーでsubmitできないようにする
$(function(){
  $('input[type=button]').click(function(){
    $('form').submit();
  });
});
