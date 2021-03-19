function AddToCart(b) {
  // 引数bは文字列になっている
  var products = document.getElementById('products').value;
  var name = document.getElementById('name').value;
  var size = document.getElementById('size'+b).value;
  var price = document.getElementById('price').value;
  var number = document.getElementById('number'+b).value;
  var subtotal = price * number;

  var c = Number(b);
  document.getElementById('品名').innerHTML = name;
  document.getElementById('サイズ').innerHTML = size;
  document.getElementById('数量').innerHTML = number;
  document.getElementById('小計').innerHTML = subtotal;

  document.getElementById('test').innerHTML = b;

  // if(total === false){
  //   var total = subtotal;
  // } else{
  //   total += subtotal;
  // }
  // var product_inf = [name, number, subtotal]
  // if(products_inf === false){
  //   var products_inf = [product_inf];
  // } else{
  //   products_inf = products_inf.push(product_inf);
  // }
}