<html>
<body>
Edit this item...
<hr/>
<form action="/edit/{{id}}" method="post">
  <p>Edit Item:<input name="description" value="{{description}}"/></p>
  <p>Edit Quantity:<input name="quantity" value="{{quantity}}"/></p>
  <p><button type="submit">Update</button></p>
</form>
<hr/>
<a href="/list">Cancel</a>
</body>
</html>
