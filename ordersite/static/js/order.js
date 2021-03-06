function AddToCart() {
  var num = document.getElementById('number').value;
  number = parseInt(num);
  total_amount = 10000*number;
  document.getElementById('total_amount').innerHTML = total_amount;
}